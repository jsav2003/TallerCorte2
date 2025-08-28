

"""
Módulo que define la clase Esfera.
"""
from figura3d import Figura3d

class Esfera(Figura3d):
    """Clase para representar una esfera. Hereda de Figura3d."""

    def __init__(self, radio):
        super().__init__("Esfera")
        self.radio = radio

    def calcular_volumen(self):
        """Calcula el volumen de la esfera."""
        return (4/3) * 3.14159 * self.radio ** 3
