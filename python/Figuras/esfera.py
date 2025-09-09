

"""
MÃ³dulo que define la clase Esfera.
"""
import math
from figura3d import Figura3d

class Esfera(Figura3d):
    """Clase para representar una esfera. Hereda de Figura3d."""

    def __init__(self, radio, id_figura=None):
        """
        Constructor de la clase Esfera.

        Args:
            radio (float): Radio de la esfera (debe ser validado externamente)
            id_figura (int, optional): ID especÃ­fico para la figura
        """
        super().__init__("Esfera", id_figura)
        self.radio = float(radio)

    def calcular_volumen(self):
        """Calcula el volumen de la esfera usando Ï€."""
        return (4/3) * math.pi * self.radio ** 3

    def calcular_area_superficie(self):
        """Calcula el Ã¡rea de superficie de la esfera."""
        return 4 * math.pi * self.radio ** 2

    def get_radio(self):
        """Retorna el radio de la esfera."""
        return self.radio

    def set_radio(self, radio):
        """
        Establece un nuevo radio para la esfera.

        Args:
            radio (float): Nuevo radio (debe ser validado externamente)
        """
        self.radio = float(radio)

    def __str__(self):
        """RepresentaciÃ³n en string de la esfera."""
        return (f"Esfera ID:{self.get_id()} - "
                f"Radio: {self.radio:.2f}, "
                f"Volumen: {self.calcular_volumen():.2f}, "
                f"Ãrea superficie: {self.calcular_area_superficie():.2f}")

    def __repr__(self):
        """RepresentaciÃ³n tÃ©cnica de la esfera."""
        return f"Esfera(radio={self.radio}, id_figura={self.get_id()})"
