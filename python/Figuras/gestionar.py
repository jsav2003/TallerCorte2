
"""
Módulo para gestionar la interacción con el usuario y las figuras geométricas.
"""
from cubo import Cubo
from esfera import Esfera
from circulo import Circulo
from cuadrado import Cuadrado

class Gestionar:
    """Clase para gestionar el menú y la creación de figuras geométricas."""

    def __init__(self):
        pass

    def mostrar_menu(self):
        """Muestra las opciones del menú."""
        print("\n" + "="*40)
        print("    GESTOR DE FIGURAS GEOMÉTRICAS")
        print("="*40)
        print("1. Crear Cubo")
        print("2. Crear Esfera")
        print("3. Crear Circulo")
        print("4. Crear Cuadrado")
        print("5. Salir")
        print("-"*40)

    def obtener_opcion(self):
        """Obtiene y valida la opción del usuario."""
        while True:
            try:
                opcion = input("Seleccione una opcion (1-5): ")
                if opcion in ("1", "2", "3", "4", "5"):
                    return opcion
                print("❌ Error: Ingrese una opción válida (1-5)")
            except KeyboardInterrupt:
                print("\n¡Programa interrumpido!")
                return "5"

    def obtener_numero_positivo(self, mensaje):
        """Obtiene un número positivo del usuario."""
        while True:
            try:
                valor = float(input(mensaje))
                if valor > 0:
                    return valor
                print("❌ Error: El valor debe ser mayor que 0")
            except ValueError:
                print("❌ Error: Ingrese un número válido")
            except KeyboardInterrupt:
                print("\n¡Programa interrumpido!")
                return None

    def crear_cubo(self):
        """Crea y muestra información de un cubo."""
        lado = self.obtener_numero_positivo("Ingrese la longitud del lado del cubo: ")
        if lado is not None:
            cubo = Cubo(lado)
            print(f"✓ Volumen del cubo: {cubo.calcular_volumen():.2f} unidades³")

    def crear_esfera(self):
        """Crea y muestra información de una esfera."""
        radio = self.obtener_numero_positivo("Ingrese el radio de la esfera: ")
        if radio is not None:
            esfera = Esfera(radio)
            print(f"✓ Volumen de la esfera: {esfera.calcular_volumen():.2f} unidades³")

    def crear_circulo(self):
        """Crea y muestra información de un círculo."""
        radio = self.obtener_numero_positivo("Ingrese el radio del círculo: ")
        if radio is not None:
            circulo = Circulo(radio)
            print(f"✓ Área del círculo: {circulo.calcular_area():.2f} unidades²")
            print(f"✓ Perímetro del círculo: {circulo.calcular_perimetro():.2f} unidades")

    def crear_cuadrado(self):
        """Crea y muestra información de un cuadrado."""
        lado = self.obtener_numero_positivo("Ingrese la longitud del lado del cuadrado: ")
        if lado is not None:
            cuadrado = Cuadrado(lado)
            print(f"✓ Área del cuadrado: {cuadrado.calcular_area():.2f} unidades²")
            print(f"✓ Perímetro del cuadrado: {cuadrado.calcular_perimetro():.2f} unidades")

    def procesar_opcion(self, opcion):
        """Procesa la opción seleccionada por el usuario."""
        if opcion == "1":
            self.crear_cubo()
        elif opcion == "2":
            self.crear_esfera()
        elif opcion == "3":
            self.crear_circulo()
        elif opcion == "4":
            self.crear_cuadrado()
        elif opcion == "5":
            print("\n¡Gracias por usar el programa!")
            print("¡Hasta luego! 👋")
            return False
        return True

    def pausar(self):
        """Pausa el programa hasta que el usuario presione Enter."""
        try:
            input("\nPresiona Enter para continuar...")
        except KeyboardInterrupt:
            pass

    def ejecutar(self):
        """Método principal que ejecuta el programa."""
        print("¡Bienvenido al Gestor de Figuras Geométricas!")
        while True:
            self.mostrar_menu()
            opcion = self.obtener_opcion()

            continuar = self.procesar_opcion(opcion)
            if not continuar:
                break
            self.pausar()
