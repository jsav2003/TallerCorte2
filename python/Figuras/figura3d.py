

"""
MÃ³dulo que define la clase abstracta Figura3d.
"""
from abc import ABC, abstractmethod
from figura import Figura

class Figura3d(Figura, ABC):
    """Clase abstracta para figuras geomÃ©tricas 3D. Hereda de Figura."""

    def __init__(self, nombre, id_figura=None):
        """
        Constructor de la clase Figura3d.

        Args:
            nombre (str): Nombre de la figura
            id_figura (int, optional): ID especÃ­fico para la figura
        """
        super().__init__(nombre, "3D", id_figura)

    @abstractmethod
    def calcular_volumen(self):
        """MÃ©todo abstracto para calcular el volumen de la figura 3D."""
        raise NotImplementedError("Subclases deben implementar calcular_volumen()")
