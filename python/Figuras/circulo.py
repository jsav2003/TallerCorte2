
"""
Módulo que define la clase Circulo.
"""
import math
from figura2d import Figura2d

class Circulo(Figura2d):
    """Clase para representar un círculo. Hereda de Figura2d."""

    def __init__(self, radio, id_figura=None):
        """
        Constructor de la clase Circulo.
        
        Args:
            radio (float): Radio del círculo (debe ser validado externamente)
            id_figura (int, optional): ID específico para la figura
        """
        super().__init__("Circulo", id_figura)
        self.radio = float(radio)

    def calcular_area(self):
        """Calcula el área del círculo usando π."""
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        """Calcula el perímetro del círculo usando π."""
        return 2 * math.pi * self.radio
    
    def get_radio(self):
        """Retorna el radio del círculo."""
        return self.radio
    
    def set_radio(self, radio):
        """
        Establece un nuevo radio para el círculo.
        
        Args:
            radio (float): Nuevo radio (debe ser validado externamente)
        """
        self.radio = float(radio)
    
    def __str__(self):
        """Representación en string del círculo."""
        return (f"Círculo ID:{self.get_id()} - "
                f"Radio: {self.radio:.2f}, "
                f"Área: {self.calcular_area():.2f}, "
                f"Perímetro: {self.calcular_perimetro():.2f}")
    
    def __repr__(self):
        """Representación técnica del círculo."""
        return f"Circulo(radio={self.radio}, id_figura={self.get_id()})"
