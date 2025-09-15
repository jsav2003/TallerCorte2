"""
Generador de IDs únicos para las figuras
"""


class GeneradorID:
    """Clase para generar identificadores únicos para las figuras"""
    
    _contador_id = 0
    
    @classmethod
    def obtener_siguiente_id(cls) -> int:
        """
        Obtiene el siguiente ID disponible
        
        Returns:
            int: Siguiente ID único
        """
        cls._contador_id += 1
        return cls._contador_id
    
    @classmethod
    def actualizar_si_mayor(cls, id_figura: int) -> None:
        """
        Actualiza el contador si el ID proporcionado es mayor
        
        Args:
            id_figura (int): ID a comparar con el contador actual
        """
        if id_figura > cls._contador_id:
            cls._contador_id = id_figura
    
    @classmethod
    def resetear(cls) -> None:
        """Resetea el contador de IDs a cero"""
        cls._contador_id = 0
    
    @classmethod
    def obtener_contador_actual(cls) -> int:
        """
        Obtiene el valor actual del contador sin incrementarlo
        
        Returns:
            int: Valor actual del contador
        """
        return cls._contador_id