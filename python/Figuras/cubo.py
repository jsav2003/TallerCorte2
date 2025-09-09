

"""
MÃ³dulo que define la clase Cubo.
"""
from figura3d import Figura3d

class Cubo(Figura3d):
    """Clase para representar un cubo. Hereda de Figura3d."""

    def __init__(self, lado, id_figura=None):
        """
        Constructor de la clase Cubo.

        Args:
            lado (float): Longitud del lado del cubo (debe ser validado externamente)
            id_figura (int, optional): ID especÃ­fico para la figura
        """
        super().__init__("Cubo", id_figura)
        self.lado = float(lado)

    def calcular_volumen(self):
        """Calcula el volumen del cubo."""
        return self.lado ** 3

    def calcular_area_superficie(self):
        """Calcula el Ã¡rea de superficie del cubo."""
        return 6 * self.lado ** 2

    def get_lado(self):
        """Retorna el lado del cubo."""
        return self.lado

    def set_lado(self, lado):
        """
        Establece un nuevo lado para el cubo.

        Args:
            lado (float): Nuevo lado (debe ser validado externamente)
        """
        self.lado = float(lado)

    def __str__(self):
        """RepresentaciÃ³n en string del cubo."""
        return (f"Cubo ID:{self.get_id()} - "
                f"Lado: {self.lado:.2f}, "
                f"Volumen: {self.calcular_volumen():.2f}, "
                f"Ãrea superficie: {self.calcular_area_superficie():.2f}")

    def __repr__(self):
        """RepresentaciÃ³n tÃ©cnica del cubo."""
        return f"Cubo(lado={self.lado}, id_figura={self.get_id()})"
