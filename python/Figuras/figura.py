"""
Clase base abstracta Figura
"""
# pylint: disable=invalid-name
from abc import ABC

class Figura(ABC):
    """Clase abstracta base para todas las figuras geométricas"""

    def __init__(self, nombre: str, tipo: str, id_figura: int):
        """
        Constructor de la clase Figura

        Args:
            nombre (str): Nombre de la figura
            tipo (str): Tipo de figura
            id_figura (int): Identificador único de la figura
        """
        self._nombre = nombre
        self._tipo = tipo
        self._id_figura = id_figura

    def get_nombre(self) -> str:
        """Obtiene el nombre de la figura"""
        return self._nombre

    def get_tipo(self) -> str:
        """Obtiene el tipo de la figura"""
        return self._tipo

    def get_id(self) -> int:
        """Obtiene el ID de la figura"""
        return self._id_figura

    def set_nombre(self, nombre: str) -> None:
        """Establece el nombre de la figura"""
        self._nombre = nombre

    def set_tipo(self, tipo: str) -> None:
        """Establece el tipo de la figura"""
        self._tipo = tipo
