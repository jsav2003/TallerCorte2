
"""
Módulo que define la clase Circulo.
"""
from figura2d import Figura2d

class Circulo(Figura2d):
    """Clase para representar un círculo. Hereda de Figura2d."""

    def __init__(self, radio):
        super().__init__("Circulo")
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return 3.14159 * self.radio ** 2

    def calcular_perimetro(self):
        """Calcula el perímetro del círculo."""
        return 2 * 3.14159 * self.radio
