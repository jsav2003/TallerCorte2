

"""
Módulo que define la clase Cuadrado.
"""
from figura2d import Figura2d

class Cuadrado(Figura2d):
    """Clase para representar un cuadrado. Hereda de Figura2d."""

    def __init__(self, lado):
        """Constructor de la clase Cuadrado."""
        super().__init__("Cuadrado")
        self.lado = lado

    def calcular_area(self):
        """Calcula el área del cuadrado."""
        return self.lado ** 2

    def calcular_perimetro(self):
        """Calcula el perímetro del cuadrado."""
        return 4 * self.lado
