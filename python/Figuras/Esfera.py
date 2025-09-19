"""
Clase Esfera - Figura tridimensional
"""
# pylint: disable=invalid-name
import math
from Figura3d import Figura3d

class Esfera(Figura3d):
    """Clase que representa una esfera"""

    def __init__(self, radio: float, id_figura: int):
        """
        Constructor de la clase Esfera

        Args:
            radio (float): Radio de la esfera
            id_figura (int): Identificador único de la figura
        """
        super().__init__("Esfera", id_figura)
        self._radio = radio

    def calcular_volumen(self) -> float:
        """Calcula el volumen de la esfera"""
        return (4/3) * math.pi * (self._radio ** 3)

    def calcular_area_superficie(self) -> float:
        """Calcula el área de superficie de la esfera"""
        return 4 * math.pi * (self._radio ** 2)

    def get_radio(self) -> float:
        """Obtiene el radio de la esfera"""
        return self._radio

    def set_radio(self, radio: float) -> None:
        """Establece el radio de la esfera"""
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self._radio = radio

    def __str__(self) -> str:
        """Representación en cadena de la esfera"""
        return f"Esfera(id={self.get_id()}, radio={self._radio:.2f})"

    def __repr__(self) -> str:
        """Representación técnica de la esfera"""
        return f"Esfera(radio={self._radio}, id_figura={self.get_id()})"
