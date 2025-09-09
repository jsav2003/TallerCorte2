

"""
MÃ³dulo principal para ejecutar el gestor de figuras geomÃ©tricas.
Clase Main siguiendo el patrÃ³n similar a Java.
"""
from gestionar import Gestionar

class Main:
    """Clase principal de la aplicaciÃ³n."""

    @staticmethod
    def main():
        """
        MÃ©todo principal de la aplicaciÃ³n.
        Equivalente al main(String[] args) de Java.
        """
        gestor = Gestionar()
        gestor.ejecutar()

if __name__ == "__main__":
    Main.main()
