"""
Clase Circulo - Figura bidimensional
"""
import math
from .Figura2d import Figura2d


class Circulo(Figura2d):
    """Clase que representa un círculo"""
    
    def __init__(self, radio: float, id_figura: int):
        """
        Constructor de la clase Circulo
        
        Args:
            radio (float): Radio del círculo
            id_figura (int): Identificador único de la figura
        """
        super().__init__("Círculo", id_figura)
        self._radio = radio
    
    def calcular_area(self) -> float:
        """Calcula el área del círculo"""
        return math.pi * self._radio ** 2
    
    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del círculo"""
        return 2 * math.pi * self._radio
    
    def get_radio(self) -> float:
        """Obtiene el radio del círculo"""
        return self._radio
    
    def set_radio(self, radio: float) -> None:
        """Establece el radio del círculo"""
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self._radio = radio
    
    def __str__(self) -> str:
        """Representación en cadena del círculo"""
        return f"Círculo(id={self.get_id()}, radio={self._radio:.2f})"
    
    def __repr__(self) -> str:
        """Representación técnica del círculo"""
        return f"Circulo(radio={self._radio}, id_figura={self.get_id()})"