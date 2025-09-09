"""
Módulo que implementa el patrón Factory Method para la creación de figuras.
"""
from circulo import Circulo
from cuadrado import Cuadrado
from cubo import Cubo
from esfera import Esfera
from io_figuras import ValidadorEntrada

class FiguraFactory:
    """
    Factory para crear figuras geométricas.
    Implementa el patrón creacional Factory Method.
    """
    
    @staticmethod
    def crear_figura(tipo_figura, **kwargs):
        """
        Crea una figura del tipo especificado con los parámetros dados.
        
        Args:
            tipo_figura (str): Tipo de figura ('circulo', 'cuadrado', 'cubo', 'esfera')
            **kwargs: Parámetros específicos para cada figura
                - radio: para círculo y esfera
                - lado: para cuadrado y cubo
                - id_figura: ID específico (opcional)
        
        Returns:
            Figura: Instancia de la figura creada
            
        Raises:
            ValueError: Si el tipo de figura no es válido o faltan parámetros
        """
        tipo_figura = tipo_figura.lower().strip()
        
        # Validar parámetros comunes
        id_figura = kwargs.get('id_figura', None)
        
        if tipo_figura == 'circulo':
            radio = kwargs.get('radio')
            if radio is None:
                raise ValueError("Se requiere el parámetro 'radio' para círculo")
            radio_validado = ValidadorEntrada.validar_radio(radio)
            return Circulo(radio_validado, id_figura)
            
        elif tipo_figura == 'cuadrado':
            lado = kwargs.get('lado')
            if lado is None:
                raise ValueError("Se requiere el parámetro 'lado' para cuadrado")
            lado_validado = ValidadorEntrada.validar_lado(lado)
            return Cuadrado(lado_validado, id_figura)
            
        elif tipo_figura == 'cubo':
            lado = kwargs.get('lado')
            if lado is None:
                raise ValueError("Se requiere el parámetro 'lado' para cubo")
            lado_validado = ValidadorEntrada.validar_lado(lado)
            return Cubo(lado_validado, id_figura)
            
        elif tipo_figura == 'esfera':
            radio = kwargs.get('radio')
            if radio is None:
                raise ValueError("Se requiere el parámetro 'radio' para esfera")
            radio_validado = ValidadorEntrada.validar_radio(radio)
            return Esfera(radio_validado, id_figura)
            
        else:
            raise ValueError(f"Tipo de figura no válido: {tipo_figura}. "
                           f"Tipos válidos: circulo, cuadrado, cubo, esfera")
    
    @staticmethod
    def get_tipos_disponibles():
        """Retorna la lista de tipos de figuras disponibles."""
        return ['circulo', 'cuadrado', 'cubo', 'esfera']
    
    @staticmethod
    def validar_parametros(tipo_figura, **kwargs):
        """
        Valida que los parámetros proporcionados sean correctos para el tipo de figura.
        
        Args:
            tipo_figura (str): Tipo de figura
            **kwargs: Parámetros a validar
            
        Returns:
            bool: True si los parámetros son válidos
            
        Raises:
            ValueError: Si los parámetros no son válidos
        """
        tipo_figura = tipo_figura.lower().strip()
        
        if tipo_figura not in FiguraFactory.get_tipos_disponibles():
            raise ValueError(f"Tipo de figura no válido: {tipo_figura}")
        
        if tipo_figura in ['circulo', 'esfera']:
            radio = kwargs.get('radio')
            if radio is None:
                raise ValueError(f"Se requiere el parámetro 'radio' para {tipo_figura}")
            ValidadorEntrada.validar_radio(radio)
                
        elif tipo_figura in ['cuadrado', 'cubo']:
            lado = kwargs.get('lado')
            if lado is None:
                raise ValueError(f"Se requiere el parámetro 'lado' para {tipo_figura}")
            ValidadorEntrada.validar_lado(lado)
        
        return True
