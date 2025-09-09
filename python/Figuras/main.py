

"""
Módulo principal para ejecutar el gestor de figuras geométricas.
Clase Main siguiendo el patrón similar a Java.
"""
from gestionar import Gestionar

class Main:
    """Clase principal de la aplicación."""
    
    @staticmethod
    def main():
        """
        Método principal de la aplicación.
        Equivalente al main(String[] args) de Java.
        """
        gestor = Gestionar()
        gestor.ejecutar()

if __name__ == "__main__":
    Main.main()
