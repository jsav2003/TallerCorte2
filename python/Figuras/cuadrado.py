

"""
Módulo que define la clase Cuadrado.
"""
from figura2d import Figura2d

class Cuadrado(Figura2d):
    """Clase para representar un cuadrado. Hereda de Figura2d."""

    def __init__(self, lado, id_figura=None):
        """
        Constructor de la clase Cuadrado.
        
        Args:
            lado (float): Longitud del lado del cuadrado (debe ser validado externamente)
            id_figura (int, optional): ID específico para la figura
        """
        super().__init__("Cuadrado", id_figura)
        self.lado = float(lado)

    def calcular_area(self):
        """Calcula el área del cuadrado."""
        return self.lado ** 2

    def calcular_perimetro(self):
        """Calcula el perímetro del cuadrado."""
        return 4 * self.lado
    
    def get_lado(self):
        """Retorna el lado del cuadrado."""
        return self.lado
    
    def set_lado(self, lado):
        """
        Establece un nuevo lado para el cuadrado.
        
        Args:
            lado (float): Nuevo lado (debe ser validado externamente)
        """
        self.lado = float(lado)
    
    def __str__(self):
        """Representación en string del cuadrado."""
        return (f"Cuadrado ID:{self.get_id()} - "
                f"Lado: {self.lado:.2f}, "
                f"Área: {self.calcular_area():.2f}, "
                f"Perímetro: {self.calcular_perimetro():.2f}")
    
    def __repr__(self):
        """Representación técnica del cuadrado."""
        return f"Cuadrado(lado={self.lado}, id_figura={self.get_id()})"
