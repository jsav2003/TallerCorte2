

"""
Módulo que define la clase Cubo.
"""
from figura3d import Figura3d

class Cubo(Figura3d):
    """Clase para representar un cubo. Hereda de Figura3d."""

    def __init__(self, lado):
        """Constructor de la clase Cubo."""
        super().__init__("Cubo")
        self.lado = lado

    def calcular_volumen(self):
        """Calcula el volumen del cubo."""
        return self.lado ** 3
