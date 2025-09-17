"""
Manejo de persistencia de datos en archivos
"""
# pylint: disable=invalid-name
import json
import os
from typing import List, Dict, Any
from Figura import Figura
from FiguraFactory import FiguraFactory

class PersistenciaArchivos:
    """Clase para manejar la persistencia de figuras en archivos JSON"""

    @staticmethod
    def guardar_en_archivo(figuras: Dict[int, Figura], archivo: str) -> bool:
        """
        Guarda las figuras en un archivo JSON

        Args:
            figuras (Dict[int, Figura]): Diccionario de figuras a guardar
            archivo (str): Ruta del archivo donde guardar

        Returns:
            bool: True si se guardó exitosamente, False en caso contrario
        """
        try:
            # Crear directorio si no existe
            directorio = os.path.dirname(archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)

            # Convertir figuras a formato serializable
            datos_figuras = []
            for figura in figuras.values():
                datos_figura = PersistenciaArchivos._figura_a_dict(figura)
                datos_figuras.append(datos_figura)

            # Guardar en archivo JSON
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(datos_figuras, f, indent=2, ensure_ascii=False)

            return True

        except Exception as e:
            print(f"Error al guardar archivo: {e}")
            return False

    @staticmethod
    def cargar_desde_archivo(archivo: str) -> List[Figura]:
        """
        Carga figuras desde un archivo JSON

        Args:
            archivo (str): Ruta del archivo a cargar

        Returns:
            List[Figura]: Lista de figuras cargadas
        """
        figuras = []

        try:
            if not os.path.exists(archivo):
                return figuras

            with open(archivo, 'r', encoding='utf-8') as f:
                datos_figuras = json.load(f)

            for datos in datos_figuras:
                figura = PersistenciaArchivos._dict_a_figura(datos)
                if figura:
                    figuras.append(figura)

        except Exception as e:
            print(f"Error al cargar archivo: {e}")

        return figuras

    @staticmethod
    def _figura_a_dict(figura: Figura) -> Dict[str, Any]:
        """
        Convierte una figura a diccionario para serialización

        Args:
            figura (Figura): Figura a convertir

        Returns:
            Dict[str, Any]: Diccionario con datos de la figura
        """
        datos = {
            'id': figura.get_id(),
            'nombre': figura.get_nombre(),
            'tipo': figura.get_tipo()
        }

        # Agregar atributos específicos según el tipo
        if hasattr(figura, 'get_radio'):
            datos['radio'] = figura.get_radio()
        elif hasattr(figura, 'get_lado'):
            datos['lado'] = figura.get_lado()

        return datos

    @staticmethod
    def _dict_a_figura(datos: Dict[str, Any]) -> Figura:
        """
        Convierte un diccionario a figura

        Args:
            datos (Dict[str, Any]): Diccionario con datos de la figura

        Returns:
            Figura: Figura creada o None si hay error
        """
        try:
            nombre = datos['nombre'].lower()

            if 'radio' in datos:
                if nombre == 'círculo':
                    from Circulo import Circulo
                    figura = Circulo(datos['radio'], datos['id'])
                elif nombre == 'esfera':
                    from Esfera import Esfera
                    figura = Esfera(datos['radio'], datos['id'])
                else:
                    return None
            elif 'lado' in datos:
                if nombre == 'cuadrado':
                    from Cuadrado import Cuadrado
                    figura = Cuadrado(datos['lado'], datos['id'])
                elif nombre == 'cubo':
                    from Cubo import Cubo
                    figura = Cubo(datos['lado'], datos['id'])
                else:
                    return None
            else:
                return None

            return figura

        except Exception as e:
            print(f"Error al convertir datos a figura: {e}")
            return None
