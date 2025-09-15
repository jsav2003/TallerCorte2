"""
Clase para manejar la entrada de datos del usuario
"""


class LectorEntrada:
    """Clase para leer y validar entrada del usuario"""
    
    @staticmethod
    def leer_entero(mensaje: str, minimo: int = None, maximo: int = None) -> int:
        """
        Lee un número entero del usuario con validación
        
        Args:
            mensaje (str): Mensaje a mostrar al usuario
            minimo (int): Valor mínimo permitido (opcional)
            maximo (int): Valor máximo permitido (opcional)
            
        Returns:
            int: Número entero válido ingresado por el usuario
        """
        while True:
            try:
                valor = int(input(mensaje))
                
                if minimo is not None and valor < minimo:
                    print(f"El valor debe ser mayor o igual a {minimo}")
                    continue
                
                if maximo is not None and valor > maximo:
                    print(f"El valor debe ser menor o igual a {maximo}")
                    continue
                
                return valor
                
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
    
    @staticmethod
    def leer_flotante(mensaje: str, minimo: float = None) -> float:
        """
        Lee un número flotante del usuario con validación
        
        Args:
            mensaje (str): Mensaje a mostrar al usuario
            minimo (float): Valor mínimo permitido (opcional)
            
        Returns:
            float: Número flotante válido ingresado por el usuario
        """
        while True:
            try:
                valor = float(input(mensaje))
                
                if minimo is not None and valor < minimo:
                    print(f"El valor debe ser mayor o igual a {minimo}")
                    continue
                
                return valor
                
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    @staticmethod
    def leer_cadena(mensaje: str) -> str:
        """
        Lee una cadena de texto del usuario
        
        Args:
            mensaje (str): Mensaje a mostrar al usuario
            
        Returns:
            str: Cadena ingresada por el usuario
        """
        while True:
            valor = input(mensaje).strip()
            if valor:
                return valor
            print("Por favor, ingrese un valor válido.")
    
    @staticmethod
    def confirmar_accion(mensaje: str) -> bool:
        """
        Solicita confirmación del usuario (s/n)
        
        Args:
            mensaje (str): Mensaje de confirmación
            
        Returns:
            bool: True si el usuario confirma, False en caso contrario
        """
        while True:
            respuesta = input(f"{mensaje} (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                return True
            elif respuesta in ['n', 'no']:
                return False
            else:
                print("Por favor, responda 's' para sí o 'n' para no.")
    
    @staticmethod
    def seleccionar_opcion(mensaje: str, opciones: list) -> int:
        """
        Permite al usuario seleccionar una opción de una lista
        
        Args:
            mensaje (str): Mensaje a mostrar
            opciones (list): Lista de opciones disponibles
            
        Returns:
            int: Índice de la opción seleccionada (base 0)
        """
        print(mensaje)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        
        while True:
            try:
                seleccion = int(input("Seleccione una opción: "))
                if 1 <= seleccion <= len(opciones):
                    return seleccion - 1
                else:
                    print(f"Por favor, seleccione un número entre 1 y {len(opciones)}")
            except ValueError:
                print("Por favor, ingrese un número válido.")