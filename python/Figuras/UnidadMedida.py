"""
Enumeración para unidades de medida
"""
from enum import Enum
from typing import Dict


class UnidadMedida(Enum):
    """Enumeración de unidades de medida disponibles"""
    
    METROS = "m"
    CENTIMETROS = "cm"
    MILIMETROS = "mm"
    PULGADAS = "in"
    PIES = "ft"
    
    def get_factor_conversion(self) -> float:
        """
        Obtiene el factor de conversión a metros
        
        Returns:
            float: Factor de conversión a metros
        """
        factores = {
            UnidadMedida.METROS: 1.0,
            UnidadMedida.CENTIMETROS: 0.01,
            UnidadMedida.MILIMETROS: 0.001,
            UnidadMedida.PULGADAS: 0.0254,
            UnidadMedida.PIES: 0.3048
        }
        return factores[self]
    
    def get_simbolo(self) -> str:
        """
        Obtiene el símbolo de la unidad
        
        Returns:
            str: Símbolo de la unidad
        """
        return self.value
    
    def get_nombres_completos(self) -> Dict[str, str]:
        """
        Obtiene un diccionario con los nombres completos de las unidades
        
        Returns:
            Dict[str, str]: Diccionario con nombres completos
        """
        return {
            UnidadMedida.METROS.value: "metros",
            UnidadMedida.CENTIMETROS.value: "centímetros",
            UnidadMedida.MILIMETROS.value: "milímetros",
            UnidadMedida.PULGADAS.value: "pulgadas",
            UnidadMedida.PIES.value: "pies"
        }