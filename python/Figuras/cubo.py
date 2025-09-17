"""
Clase Cubo - Figura tridimensional
"""
# pylint: disable=invalid-name
from Figura3d import Figura3d

class Cubo(Figura3d):
    """Clase que representa un cubo"""

    def __init__(self, lado: float, id_figura: int):
        """
        Constructor de la clase Cubo

        Args:
            lado (float): Longitud del lado del cubo
            id_figura (int): Identificador único de la figura
        """
        super().__init__("Cubo", id_figura)
        self._lado = lado

    def calcular_volumen(self) -> float:
        """Calcula el volumen del cubo"""
        return self._lado ** 3

    def calcular_area_superficie(self) -> float:
        """Calcula el área de superficie del cubo"""
        return 6 * (self._lado ** 2)

    def get_lado(self) -> float:
        """Obtiene la longitud del lado del cubo"""
        return self._lado

    def set_lado(self, lado: float) -> None:
        """Establece la longitud del lado del cubo"""
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que cero")
        self._lado = lado

    def __str__(self) -> str:
        """Representación en cadena del cubo"""
        return f"Cubo(id={self.get_id()}, lado={self._lado:.2f})"

    def __repr__(self) -> str:
        """Representación técnica del cubo"""
        return f"Cubo(lado={self._lado}, id_figura={self.get_id()})"
