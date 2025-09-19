"""
Clase abstracta para figuras bidimensionales
"""
# pylint: disable=invalid-name
from abc import abstractmethod
from Figura import Figura

class Figura2d(Figura):
    """Clase abstracta para figuras bidimensionales"""

    def __init__(self, nombre: str, id_figura: int):
        """
        Constructor de la clase Figura2d

        Args:
            nombre (str): Nombre de la figura
            id_figura (int): Identificador único de la figura
        """
        super().__init__(nombre, "2D", id_figura)

    @abstractmethod
    def calcular_area(self) -> float:
        """Calcula el área de la figura 2D"""

    @abstractmethod
    def calcular_perimetro(self) -> float:
        """Calcula el perímetro de la figura 2D"""
