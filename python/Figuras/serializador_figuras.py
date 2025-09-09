"""
Módulo para serialización y deserialización de figuras.
Se encarga exclusivamente de convertir figuras a/desde formatos persistentes.
"""
import json
from typing import Dict, Any, List, Tuple
from figura import Figura
from generador_id import GeneradorID

class SerializadorFiguras:
    """Clase responsable de la serialización y deserialización de figuras."""
    
    @staticmethod
    def figura_a_dict(figura: Figura) -> Dict[str, Any]:
        """
        Convierte una figura a diccionario para persistencia.
        
        Args:
            figura: Instancia de figura
            
        Returns:
            Dict: Representación de la figura como diccionario
        """
        figura_dict = {
            'id_figura': figura.get_id(),
            'nombre': figura.get_nombre(),
            'tipo': figura.get_tipo()
        }
        
        # Añadir propiedades específicas según el tipo
        if hasattr(figura, 'radio'):
            figura_dict['radio'] = figura.radio
        
        if hasattr(figura, 'lado'):
            figura_dict['lado'] = figura.lado
            
        return figura_dict
    
    @staticmethod
    def dict_a_figura(figura_dict: Dict[str, Any]):
        """
        Convierte un diccionario a figura usando el factory.
        
        Args:
            figura_dict: Diccionario con datos de figura
            
        Returns:
            Figura: Instancia de figura creada
        """
        from figura_factory import FiguraFactory
        
        tipo = figura_dict['nombre'].lower()
        id_figura = figura_dict['id_figura']
        
        # Actualizar el generador de IDs con el ID máximo encontrado
        generador = GeneradorID()
        generador.actualizar_si_mayor(id_figura)
        
        kwargs = {'id_figura': id_figura}
        
        if 'radio' in figura_dict:
            kwargs['radio'] = figura_dict['radio']
        
        if 'lado' in figura_dict:
            kwargs['lado'] = figura_dict['lado']
        
        return FiguraFactory.crear_figura(tipo, **kwargs)
    
    @staticmethod
    def figuras_a_json(figuras: List[Figura]) -> str:
        """
        Convierte una lista de figuras a JSON.
        
        Args:
            figuras: Lista de figuras a serializar
            
        Returns:
            str: JSON con las figuras serializadas
        """
        figuras_dict = []
        
        for figura in figuras:
            figuras_dict.append(SerializadorFiguras.figura_a_dict(figura))
        
        # Obtener el contador actual del GeneradorID
        from generador_id import GeneradorID
        generador = GeneradorID()
        contador_actual = generador._contador  # El último ID asignado
        
        datos = {
            'figuras': figuras_dict,
            'contador_id': contador_actual,
            'version': '1.0'
        }
        
        return json.dumps(datos, indent=2, ensure_ascii=False)
    
    @staticmethod
    def json_a_figuras(json_str: str) -> Tuple[List[Figura], bool]:
        """
        Convierte JSON a lista de figuras.
        
        Args:
            json_str: String JSON con figuras serializadas
            
        Returns:
            Tuple: (lista_figuras, exito)
        """
        try:
            datos = json.loads(json_str)
            figuras = []
            
            # Restaurar contador de IDs en el GeneradorID
            if 'contador_id' in datos:
                from generador_id import GeneradorID
                generador = GeneradorID()
                generador.establecer_siguiente_id(datos['contador_id'] + 1)
            
            # Deserializar figuras
            if 'figuras' in datos:
                for figura_dict in datos['figuras']:
                    try:
                        figura = SerializadorFiguras.dict_a_figura(figura_dict)
                        figuras.append(figura)
                    except Exception as e:
                        print(f"⚠️ Error al deserializar figura {figura_dict.get('id_figura', 'desconocida')}: {e}")
            
            return figuras, True
            
        except Exception as e:
            print(f"❌ Error al deserializar JSON: {e}")
            return [], False

class PersistenciaArchivos:
    """Clase para manejo de persistencia en archivos."""
    
    @staticmethod
    def guardar_figuras_archivo(figuras: List[Figura], archivo: str) -> bool:
        """
        Guarda una lista de figuras en un archivo JSON.
        
        Args:
            figuras: Lista de figuras a guardar
            archivo: Ruta del archivo
            
        Returns:
            bool: True si se guardó exitosamente
        """
        try:
            json_data = SerializadorFiguras.figuras_a_json(figuras)
            
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(json_data)
            
            return True
            
        except Exception as e:
            print(f"❌ Error al guardar figuras en archivo: {e}")
            return False
    
    @staticmethod
    def cargar_figuras_archivo(archivo: str) -> Tuple[List[Figura], bool]:
        """
        Carga figuras desde un archivo JSON.
        
        Args:
            archivo: Ruta del archivo
            
        Returns:
            Tuple: (lista_figuras, exito)
        """
        import os
        
        if not os.path.exists(archivo):
            return [], False
        
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                json_data = f.read()
            
            return SerializadorFiguras.json_a_figuras(json_data)
            
        except Exception as e:
            print(f"❌ Error al cargar figuras desde archivo: {e}")
            return [], False
    
    @staticmethod
    def archivo_existe(archivo: str) -> bool:
        """
        Verifica si un archivo existe.
        
        Args:
            archivo: Ruta del archivo
            
        Returns:
            bool: True si el archivo existe
        """
        import os
        return os.path.exists(archivo)
    
    @staticmethod
    def obtener_info_archivo(archivo: str) -> Dict[str, Any]:
        """
        Obtiene información sobre un archivo de persistencia.
        
        Args:
            archivo: Ruta del archivo
            
        Returns:
            Dict: Información del archivo
        """
        import os
        
        info = {
            'archivo': archivo,
            'existe': os.path.exists(archivo),
            'tamaño': 0,
            'modificado': None
        }
        
        if info['existe']:
            try:
                stat = os.stat(archivo)
                info['tamaño'] = stat.st_size
                info['modificado'] = stat.st_mtime
            except Exception:
                pass
        
        return info
