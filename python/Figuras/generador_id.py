"""
Generador de IDs Ãºnicos para figuras geomÃ©tricas.
Implementa el patrÃ³n Singleton para garantizar IDs Ãºnicos globalmente.
"""

class GeneradorID:
    """
    Clase responsable de generar IDs Ãºnicos para figuras.
    Implementa el patrÃ³n Singleton para garantizar consistencia.
    """

    _instancia = None
    _contador = 0

    def __new__(cls):
        """ImplementaciÃ³n del patrÃ³n Singleton."""
        if cls._instancia is None:
            cls._instancia = super(GeneradorID, cls).__new__(cls)
        return cls._instancia

    def obtener_siguiente_id(self) -> int:
        """
        Genera el siguiente ID Ãºnico.

        Returns:
            int: Nuevo ID Ãºnico
        """
        self._contador += 1
        return self._contador

    def obtener_id_actual(self) -> int:
        """
        Obtiene el ID actual sin incrementar.

        Returns:
            int: ID actual
        """
        return self._contador

    def establecer_contador(self, valor: int) -> None:
        """
        Establece el contador en un valor especÃ­fico.
        Ãštil para sincronizar con IDs existentes.

        Args:
            valor (int): Nuevo valor del contador
        """
        if valor < 0:
            raise ValueError("El contador no puede ser negativo")
        self._contador = valor

    def establecer_siguiente_id(self, valor: int) -> None:
        """
        Establece el prÃ³ximo ID que se asignarÃ¡.

        Args:
            valor (int): PrÃ³ximo ID a asignar
        """
        if valor <= 0:
            raise ValueError("El prÃ³ximo ID debe ser mayor que 0")
        self._contador = valor - 1

    def reiniciar_contador(self) -> None:
        """
        Reinicia el contador a 0.
        Ãštil para testing.
        """
        self._contador = 0

    def actualizar_si_mayor(self, id_existente: int) -> None:
        """
        Actualiza el contador si el ID existente es mayor.
        Ãštil al cargar figuras desde archivo.

        Args:
            id_existente (int): ID a comparar
        """
        if id_existente >= self._contador:
            self._contador = id_existente
