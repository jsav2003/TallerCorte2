

"""
Módulo que define la clase abstracta Figura2d.
"""
from abc import ABC, abstractmethod
from figura import Figura

class Figura2d(Figura, ABC):
    """Clase abstracta para figuras geométricas 2D. Hereda de Figura."""

    def __init__(self, nombre, id_figura=None):
        """
        Constructor de la clase Figura2d.
        
        Args:
            nombre (str): Nombre de la figura
            id_figura (int, optional): ID específico para la figura
        """
        super().__init__(nombre, "2D", id_figura)

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de la figura 2D."""
        raise NotImplementedError("Subclases deben implementar calcular_area()")

    @abstractmethod
    def calcular_perimetro(self):
        """Método abstracto para calcular el perímetro de la figura 2D."""
        raise NotImplementedError("Subclases deben implementar calcular_perimetro()")
