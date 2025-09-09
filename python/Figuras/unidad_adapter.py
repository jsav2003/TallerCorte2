"""
Módulo que implementa el patrón Adapter para conversión de unidades de medida.
"""
from abc import ABC, abstractmethod

class UnidadMedida:
    """Enum-like class para las unidades de medida soportadas."""
    CENTIMETROS = "cm"
    METROS = "m"
    PULGADAS = "in"
    PIES = "ft"
    
    @classmethod
    def get_unidades_disponibles(cls):
        """Retorna lista de unidades disponibles."""
        return [cls.CENTIMETROS, cls.METROS, cls.PULGADAS, cls.PIES]
    
    @classmethod
    def get_nombres_completos(cls):
        """Retorna diccionario con nombres completos de unidades."""
        return {
            cls.CENTIMETROS: "centímetros",
            cls.METROS: "metros", 
            cls.PULGADAS: "pulgadas",
            cls.PIES: "pies"
        }

class IConversorUnidades(ABC):
    """Interfaz para conversores de unidades."""
    
    @abstractmethod
    def convertir(self, valor, unidad_origen, unidad_destino):
        """Convierte un valor entre unidades."""
        pass

class ConversorLongitud(IConversorUnidades):
    """Conversor para unidades de longitud."""
    
    # Factores de conversión a metros como unidad base
    FACTORES_A_METROS = {
        UnidadMedida.CENTIMETROS: 0.01,
        UnidadMedida.METROS: 1.0,
        UnidadMedida.PULGADAS: 0.0254,
        UnidadMedida.PIES: 0.3048
    }
    
    def convertir(self, valor, unidad_origen, unidad_destino):
        """
        Convierte un valor de longitud entre unidades.
        
        Args:
            valor (float): Valor a convertir
            unidad_origen (str): Unidad de origen
            unidad_destino (str): Unidad de destino
            
        Returns:
            float: Valor convertido
        """
        if unidad_origen == unidad_destino:
            return valor
            
        # Convertir a metros primero, luego a la unidad destino
        valor_metros = valor * self.FACTORES_A_METROS[unidad_origen]
        valor_convertido = valor_metros / self.FACTORES_A_METROS[unidad_destino]
        
        return valor_convertido

class ConversorArea(IConversorUnidades):
    """Conversor para unidades de área."""
    
    # Factores de conversión a metros cuadrados como unidad base
    FACTORES_A_METROS2 = {
        UnidadMedida.CENTIMETROS: 0.0001,  # cm²
        UnidadMedida.METROS: 1.0,          # m²
        UnidadMedida.PULGADAS: 0.00064516, # in²
        UnidadMedida.PIES: 0.092903        # ft²
    }
    
    def convertir(self, valor, unidad_origen, unidad_destino):
        """Convierte un valor de área entre unidades."""
        if unidad_origen == unidad_destino:
            return valor
            
        valor_metros2 = valor * self.FACTORES_A_METROS2[unidad_origen]
        valor_convertido = valor_metros2 / self.FACTORES_A_METROS2[unidad_destino]
        
        return valor_convertido

class ConversorVolumen(IConversorUnidades):
    """Conversor para unidades de volumen."""
    
    # Factores de conversión a metros cúbicos como unidad base
    FACTORES_A_METROS3 = {
        UnidadMedida.CENTIMETROS: 0.000001,    # cm³
        UnidadMedida.METROS: 1.0,              # m³
        UnidadMedida.PULGADAS: 0.000016387,    # in³
        UnidadMedida.PIES: 0.028317            # ft³
    }
    
    def convertir(self, valor, unidad_origen, unidad_destino):
        """Convierte un valor de volumen entre unidades."""
        if unidad_origen == unidad_destino:
            return valor
            
        valor_metros3 = valor * self.FACTORES_A_METROS3[unidad_origen]
        valor_convertido = valor_metros3 / self.FACTORES_A_METROS3[unidad_destino]
        
        return valor_convertido

class UnidadAdapter:
    """
    Adapter que facilita la conversión de medidas de figuras geométricas.
    Implementa el patrón estructural Adapter.
    """
    
    def __init__(self):
        """Inicializa el adapter con los conversores necesarios."""
        self.conversor_longitud = ConversorLongitud()
        self.conversor_area = ConversorArea()
        self.conversor_volumen = ConversorVolumen()
    
    def convertir_medidas_figura(self, figura, unidad_origen, unidad_destino):
        """
        Convierte todas las medidas relevantes de una figura.
        
        Args:
            figura: Instancia de figura geométrica
            unidad_origen (str): Unidad original de las medidas
            unidad_destino (str): Unidad a la cual convertir
            
        Returns:
            dict: Diccionario con las medidas convertidas
        """
        if unidad_origen not in UnidadMedida.get_unidades_disponibles():
            raise ValueError(f"Unidad de origen no válida: {unidad_origen}")
            
        if unidad_destino not in UnidadMedida.get_unidades_disponibles():
            raise ValueError(f"Unidad de destino no válida: {unidad_destino}")
        
        medidas = {}
        
        # Obtener dimensiones base convertidas
        if hasattr(figura, 'radio'):
            medidas['radio'] = self.conversor_longitud.convertir(
                figura.radio, unidad_origen, unidad_destino
            )
        
        if hasattr(figura, 'lado'):
            medidas['lado'] = self.conversor_longitud.convertir(
                figura.lado, unidad_origen, unidad_destino
            )
        
        # Calcular y convertir medidas derivadas
        if hasattr(figura, 'calcular_area'):
            area_original = figura.calcular_area()
            medidas['area'] = self.conversor_area.convertir(
                area_original, unidad_origen, unidad_destino
            )
        
        if hasattr(figura, 'calcular_perimetro'):
            perimetro_original = figura.calcular_perimetro()
            medidas['perimetro'] = self.conversor_longitud.convertir(
                perimetro_original, unidad_origen, unidad_destino
            )
        
        if hasattr(figura, 'calcular_volumen'):
            volumen_original = figura.calcular_volumen()
            medidas['volumen'] = self.conversor_volumen.convertir(
                volumen_original, unidad_origen, unidad_destino
            )
        
        return medidas
    
    def formatear_medidas(self, medidas, unidad, precision=2):
        """
        Formatea las medidas para mostrar al usuario.
        
        Args:
            medidas (dict): Diccionario con las medidas
            unidad (str): Unidad de medida
            precision (int): Decimales a mostrar
            
        Returns:
            dict: Medidas formateadas como strings
        """
        simbolos_unidad = {
            'radio': unidad,
            'lado': unidad,
            'perimetro': unidad,
            'area': f"{unidad}²",
            'volumen': f"{unidad}³"
        }
        
        medidas_formateadas = {}
        for medida, valor in medidas.items():
            simbolo = simbolos_unidad.get(medida, unidad)
            medidas_formateadas[medida] = f"{valor:.{precision}f} {simbolo}"
        
        return medidas_formateadas
    
    @staticmethod
    def validar_unidad(unidad):
        """Valida que una unidad sea soportada."""
        if unidad not in UnidadMedida.get_unidades_disponibles():
            unidades = ", ".join(UnidadMedida.get_unidades_disponibles())
            raise ValueError(f"Unidad no válida: {unidad}. Unidades disponibles: {unidades}")
        return True
    
    def convertir(self, valor, unidad_origen, unidad_destino):
        """
        Convierte un valor de longitud entre unidades.
        
        Args:
            valor (float): Valor a convertir
            unidad_origen: Unidad de origen
            unidad_destino: Unidad de destino
            
        Returns:
            float: Valor convertido
        """
        return self.conversor_longitud.convertir(valor, unidad_origen, unidad_destino)
    
    def convertir_area(self, valor, unidad_origen, unidad_destino):
        """
        Convierte un valor de área entre unidades.
        
        Args:
            valor (float): Valor a convertir
            unidad_origen: Unidad de origen
            unidad_destino: Unidad de destino
            
        Returns:
            float: Valor convertido
        """
        return self.conversor_area.convertir(valor, unidad_origen, unidad_destino)
    
    def convertir_volumen(self, valor, unidad_origen, unidad_destino):
        """
        Convierte un valor de volumen entre unidades.
        
        Args:
            valor (float): Valor a convertir
            unidad_origen: Unidad de origen
            unidad_destino: Unidad de destino
            
        Returns:
            float: Valor convertido
        """
        return self.conversor_volumen.convertir(valor, unidad_origen, unidad_destino)
