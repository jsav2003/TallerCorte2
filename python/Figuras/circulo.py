
"""
MÃ³dulo que define la clase Circulo.
"""
import math
from figura2d import Figura2d

class Circulo(Figura2d):
    """Clase para representar un cÃ­rculo. Hereda de Figura2d."""

    def __init__(self, radio, id_figura=None):
        """
        Constructor de la clase Circulo.

        Args:
            radio (float): Radio del cÃ­rculo (debe ser validado externamente)
            id_figura (int, optional): ID especÃ­fico para la figura
        """
        super().__init__("Circulo", id_figura)
        self.radio = float(radio)

    def calcular_area(self):
        """Calcula el Ã¡rea del cÃ­rculo usando Ï€."""
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        """Calcula el perÃ­metro del cÃ­rculo usando Ï€."""
        return 2 * math.pi * self.radio

    def get_radio(self):
        """Retorna el radio del cÃ­rculo."""
        return self.radio

    def set_radio(self, radio):
        """
        Establece un nuevo radio para el cÃ­rculo.

        Args:
            radio (float): Nuevo radio (debe ser validado externamente)
        """
        self.radio = float(radio)

    def __str__(self):
        """RepresentaciÃ³n en string del cÃ­rculo."""
        return (f"CÃ­rculo ID:{self.get_id()} - "
                f"Radio: {self.radio:.2f}, "
                f"Ãrea: {self.calcular_area():.2f}, "
                f"PerÃ­metro: {self.calcular_perimetro():.2f}")

    def __repr__(self):
        """RepresentaciÃ³n tÃ©cnica del cÃ­rculo."""
        return f"Circulo(radio={self.radio}, id_figura={self.get_id()})"
