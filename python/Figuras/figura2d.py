

"""
MÃ³dulo que define la clase abstracta Figura2d.
"""
from abc import ABC, abstractmethod
from figura import Figura

class Figura2d(Figura, ABC):
    """Clase abstracta para figuras geomÃ©tricas 2D. Hereda de Figura."""

    def __init__(self, nombre, id_figura=None):
        """
        Constructor de la clase Figura2d.

        Args:
            nombre (str): Nombre de la figura
            id_figura (int, optional): ID especÃ­fico para la figura
        """
        super().__init__(nombre, "2D", id_figura)

    @abstractmethod
    def calcular_area(self):
        """MÃ©todo abstracto para calcular el Ã¡rea de la figura 2D."""
        raise NotImplementedError("Subclases deben implementar calcular_area()")

    @abstractmethod
    def calcular_perimetro(self):
        """MÃ©todo abstracto para calcular el perÃ­metro de la figura 2D."""
        raise NotImplementedError("Subclases deben implementar calcular_perimetro()")
