

"""
Módulo que define la clase abstracta Figura2d.
"""
from abc import ABC, abstractmethod
from figura import Figura

class Figura2d(Figura, ABC):
    """Clase abstracta para figuras geométricas 2D. Hereda de Figura."""

    def __init__(self, nombre):
        """Constructor de la clase Figura2d."""
        super().__init__(nombre, "2D")

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de la figura 2D."""
        raise NotImplementedError()

    @abstractmethod
    def calcular_perimetro(self):
        """Método abstracto para calcular el perímetro de la figura 2D."""
        raise NotImplementedError()
