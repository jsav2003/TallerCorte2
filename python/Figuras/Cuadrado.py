"""
Clase Cuadrado - Figura bidimensional
"""
# pylint: disable=invalid-name
from Figura2d import Figura2d

class Cuadrado(Figura2d):
    """Clase que representa un cuadrado"""

    def __init__(self, lado: float, id_figura: int):
        """
        Constructor de la clase Cuadrado

        Args:
            lado (float): Longitud del lado del cuadrado
            id_figura (int): Identificador único de la figura
        
        Raises:
            ValueError: Si el lado es menor o igual a cero
        """
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que cero")
        super().__init__("Cuadrado", id_figura)
        self._lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del cuadrado"""
        return self._lado ** 2

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del cuadrado"""
        return 4 * self._lado

    def get_lado(self) -> float:
        """Obtiene la longitud del lado del cuadrado"""
        return self._lado

    def set_lado(self, lado: float) -> None:
        """Establece la longitud del lado del cuadrado"""
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que cero")
        self._lado = lado

    def __str__(self) -> str:
        """Representación en cadena del cuadrado"""
        return f"Cuadrado(id={self.get_id()}, lado={self._lado:.2f})"

    def __repr__(self) -> str:
        """Representación técnica del cuadrado"""
        return f"Cuadrado(lado={self._lado}, id_figura={self.get_id()})"
