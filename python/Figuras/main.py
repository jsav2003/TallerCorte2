"""
Clase principal del programa - Punto de entrada
"""
from .Gestionar import Gestionar


class Main:
    """Clase principal del programa"""
    
    @staticmethod
    def main() -> None:
        """Método principal para iniciar la aplicación"""
        gestor = Gestionar()
        gestor.ejecutar()
        


# Punto de entrada cuando se ejecuta el módulo directamente
if __name__ == "__main__":
    Main.main()
    1
    