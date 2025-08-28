

"""
Módulo que define la clase abstracta Figura3d.
"""
from abc import ABC, abstractmethod
from figura import Figura

class Figura3d(Figura, ABC):
    """Clase abstracta para figuras geométricas 3D. Hereda de Figura."""

    def __init__(self, nombre):
        """Constructor de la clase Figura3d."""
        super().__init__(nombre, "3D")

    @abstractmethod
    def calcular_volumen(self):
        """Método abstracto para calcular el volumen de la figura 3D."""
        raise NotImplementedError()
