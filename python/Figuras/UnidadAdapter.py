"""
Adaptador para conversión entre unidades de medida
"""
# pylint: disable=invalid-name
from UnidadMedida import UnidadMedida

class UnidadAdapter:
    """Adaptador para conversión entre diferentes unidades de medida"""

    @staticmethod
    def convertir(valor: float, desde: UnidadMedida, hacia: UnidadMedida) -> float:
        """
        Convierte un valor de una unidad a otra

        Args:
            valor (float): Valor a convertir
            desde (UnidadMedida): Unidad de origen
            hacia (UnidadMedida): Unidad de destino

        Returns:
            float: Valor convertido
        """
        if desde == hacia:
            return valor

        # Convertir a metros primero
        valor_en_metros = valor * desde.get_factor_conversion()

        # Convertir de metros a la unidad destino
        factor_destino = hacia.get_factor_conversion()
        valor_convertido = valor_en_metros / factor_destino

        return valor_convertido

    @staticmethod
    def formatear_con_unidad(valor: float, unidad: UnidadMedida) -> str:
        """
        Formatea un valor con su unidad

        Args:
            valor (float): Valor a formatear
            unidad (UnidadMedida): Unidad del valor

        Returns:
            str: Valor formateado con unidad
        """
        return f"{valor:.2f} {unidad.get_simbolo()}"

    @staticmethod
    def obtener_unidades_disponibles() -> list:
        """
        Obtiene una lista de todas las unidades disponibles

        Returns:
            list: Lista de unidades disponibles
        """
        return list(UnidadMedida)
