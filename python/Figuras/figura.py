
"""
Módulo que define la clase base Figura.
"""

class Figura:
    """Clase madre para figuras geométricas 2D y 3D."""

    def __init__(self, nombre, tipo):
        """Constructor de la clase Figura."""
        self.nombre = nombre
        self.tipo = tipo

    def get_nombre(self):
        """Retorna el nombre de la figura."""
        return self.nombre

    def get_tipo(self):
        """Retorna el tipo de la figura."""
        return self.tipo

    def set_nombre(self, nombre):
        """Establece el nombre de la figura."""
        self.nombre = nombre

    def set_tipo(self, tipo):
        """Establece el tipo de la figura."""
        self.tipo = tipo
