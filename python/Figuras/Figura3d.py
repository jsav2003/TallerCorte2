"""
Clase abstracta para figuras tridimensionales
"""
# pylint: disable=invalid-name
from abc import abstractmethod
from Figura import Figura

class Figura3d(Figura):
    """Clase abstracta para figuras tridimensionales"""

    def __init__(self, nombre: str, id_figura: int):
        """
        Constructor de la clase Figura3d

        Args:
            nombre (str): Nombre de la figura
            id_figura (int): Identificador único de la figura
        """
        super().__init__(nombre, "3D", id_figura)

    @abstractmethod
    def calcular_volumen(self) -> float:
        """Calcula el volumen de la figura 3D"""
        pass
