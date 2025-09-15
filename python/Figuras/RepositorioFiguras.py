"""
Repositorio para manejar la colección de figuras
"""
from typing import Dict, List, Optional
from .Figura import Figura
from .PersistenciaArchivos import PersistenciaArchivos
from .GeneradorID import GeneradorID


class RepositorioFiguras:
    """Repositorio para gestionar la colección de figuras geométricas"""
    
    def __init__(self, archivo_persistencia: str = "figuras.json", auto_guardar: bool = True):
        """
        Constructor del repositorio
        
        Args:
            archivo_persistencia (str): Archivo para persistencia de datos
            auto_guardar (bool): Si debe guardar automáticamente al modificar
        """
        self._figuras: Dict[int, Figura] = {}
        self._archivo_persistencia = archivo_persistencia
        self._persistencia = PersistenciaArchivos()
        self._auto_guardar = auto_guardar
        
        # Cargar figuras existentes
        self.cargar_figuras()
    
    def almacenar_figura(self, figura: Figura) -> int:
        """
        Almacena una figura en el repositorio
        
        Args:
            figura (Figura): Figura a almacenar
            
        Returns:
            int: ID de la figura almacenada
        """
        id_figura = figura.get_id()
        self._figuras[id_figura] = figura
        
        # Actualizar el generador de ID si es necesario
        GeneradorID.actualizar_si_mayor(id_figura)
        
        if self._auto_guardar:
            self.guardar_figuras()
        
        return id_figura
    
    def obtener_figura(self, figura_id: int) -> Optional[Figura]:
        """
        Obtiene una figura por su ID
        
        Args:
            figura_id (int): ID de la figura a buscar
            
        Returns:
            Optional[Figura]: Figura encontrada o None
        """
        return self._figuras.get(figura_id)
    
    def obtener_todas_figuras(self) -> List[Figura]:
        """
        Obtiene todas las figuras del repositorio
        
        Returns:
            List[Figura]: Lista de todas las figuras
        """
        return list(self._figuras.values())
    
    def eliminar_figura(self, figura_id: int) -> bool:
        """
        Elimina una figura del repositorio
        
        Args:
            figura_id (int): ID de la figura a eliminar
            
        Returns:
            bool: True si se eliminó, False si no existía
        """
        if figura_id in self._figuras:
            del self._figuras[figura_id]
            
            if self._auto_guardar:
                self.guardar_figuras()
            
            return True
        
        return False
    
    def contar_figuras(self) -> int:
        """
        Cuenta el número total de figuras
        
        Returns:
            int: Número de figuras en el repositorio
        """
        return len(self._figuras)
    
    def buscar_por_tipo(self, tipo: str) -> List[Figura]:
        """
        Busca figuras por tipo
        
        Args:
            tipo (str): Tipo de figura a buscar
            
        Returns:
            List[Figura]: Lista de figuras del tipo especificado
        """
        tipo_lower = tipo.lower()
        figuras_tipo = []
        
        for figura in self._figuras.values():
            if figura.get_nombre().lower() == tipo_lower:
                figuras_tipo.append(figura)
        
        return figuras_tipo
    
    def limpiar_repositorio(self) -> None:
        """Elimina todas las figuras del repositorio"""
        self._figuras.clear()
        GeneradorID.resetear()
        
        if self._auto_guardar:
            self.guardar_figuras()
    
    def guardar_figuras(self) -> bool:
        """
        Guarda las figuras en el archivo de persistencia
        
        Returns:
            bool: True si se guardó exitosamente
        """
        return self._persistencia.guardar_en_archivo(self._figuras, self._archivo_persistencia)
    
    def cargar_figuras(self) -> bool:
        """
        Carga las figuras desde el archivo de persistencia
        
        Returns:
            bool: True si se cargó exitosamente
        """
        try:
            figuras_cargadas = self._persistencia.cargar_desde_archivo(self._archivo_persistencia)
            
            for figura in figuras_cargadas:
                self._figuras[figura.get_id()] = figura
                GeneradorID.actualizar_si_mayor(figura.get_id())
            
            return True
            
        except Exception as e:
            print(f"Error al cargar figuras: {e}")
            return False
    
    def obtener_estadisticas(self) -> Dict[str, int]:
        """
        Obtiene estadísticas del repositorio
        
        Returns:
            Dict[str, int]: Diccionario con estadísticas
        """
        estadisticas = {
            'total': len(self._figuras),
            'círculo': 0,
            'cuadrado': 0,
            'cubo': 0,
            'esfera': 0
        }
        
        for figura in self._figuras.values():
            nombre = figura.get_nombre().lower()
            if nombre in estadisticas:
                estadisticas[nombre] += 1
        
        return estadisticas