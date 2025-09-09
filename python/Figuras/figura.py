
"""
MÃ³dulo que define la clase base Figura.
"""
from generador_id import GeneradorID

class Figura:
    """Clase madre para figuras geomÃ©tricas 2D y 3D."""

    def __init__(self, nombre, tipo, id_figura=None):
        """
        Constructor de la clase Figura.

        Args:
            nombre (str): Nombre de la figura
            tipo (str): Tipo de figura (2D/3D)
            id_figura (int, optional): ID especÃ­fico, si no se proporciona se genera automÃ¡ticamente
        """
        self.nombre = nombre
        self.tipo = tipo

        # Usar el generador de IDs para obtener un ID Ãºnico
        generador = GeneradorID()

        if id_figura is None:
            self.id_figura = generador.obtener_siguiente_id()
        else:
            self.id_figura = id_figura
            # Actualizar el generador si el ID proporcionado es mayor
            generador.actualizar_si_mayor(id_figura)

    def get_nombre(self):
        """Retorna el nombre de la figura."""
        return self.nombre

    def get_tipo(self):
        """Retorna el tipo de la figura."""
        return self.tipo

    def get_id(self):
        """Retorna el ID Ãºnico de la figura."""
        return self.id_figura

    def set_nombre(self, nombre):
        """Establece el nombre de la figura."""
        self.nombre = nombre

    def set_tipo(self, tipo):
        """Establece el tipo de la figura."""
        self.tipo = tipo
