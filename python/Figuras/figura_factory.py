"""
MÃ³dulo que implementa el patrÃ³n Factory Method para la creaciÃ³n de figuras.
"""
from circulo import Circulo
from cuadrado import Cuadrado
from cubo import Cubo
from esfera import Esfera
from io_figuras import ValidadorEntrada

class FiguraFactory:
    """
    Factory para crear figuras geomÃ©tricas.
    Implementa el patrÃ³n creacional Factory Method.
    """

    @staticmethod
    def crear_figura(tipo_figura, **kwargs):
        """
        Crea una figura del tipo especificado con los parÃ¡metros dados.

        Args:
            tipo_figura (str): Tipo de figura ('circulo', 'cuadrado', 'cubo', 'esfera')
            **kwargs: ParÃ¡metros especÃ­ficos para cada figura
                - radio: para cÃ­rculo y esfera
                - lado: para cuadrado y cubo
                - id_figura: ID especÃ­fico (opcional)

        Returns:
            Figura: Instancia de la figura creada

        Raises:
            ValueError: Si el tipo de figura no es vÃ¡lido o faltan parÃ¡metros
        """
        tipo_figura = tipo_figura.lower().strip()
        # Validar parÃ¡metros comunes
        id_figura = kwargs.get('id_figura', None)

        if tipo_figura == 'circulo':
            radio = kwargs.get('radio')
            if radio is None:
                raise ValueError("Se requiere el parÃ¡metro 'radio' para cÃ­rculo")
            radio_validado = ValidadorEntrada.validar_radio(radio)
            return Circulo(radio_validado, id_figura)

        if tipo_figura == 'cuadrado':
            lado = kwargs.get('lado')
            if lado is None:
                raise ValueError("Se requiere el parÃ¡metro 'lado' para cuadrado")
            lado_validado = ValidadorEntrada.validar_lado(lado)
            return Cuadrado(lado_validado, id_figura)

        if tipo_figura == 'cubo':
            lado = kwargs.get('lado')
            if lado is None:
                raise ValueError("Se requiere el parÃ¡metro 'lado' para cubo")
            lado_validado = ValidadorEntrada.validar_lado(lado)
            return Cubo(lado_validado, id_figura)

        if tipo_figura == 'esfera':
            radio = kwargs.get('radio')
            if radio is None:
                raise ValueError("Se requiere el parÃ¡metro 'radio' para esfera")
            radio_validado = ValidadorEntrada.validar_radio(radio)
            return Esfera(radio_validado, id_figura)

        raise ValueError(f"Tipo de figura no vÃ¡lido: {tipo_figura}. "
                         f"Tipos vÃ¡lidos: circulo, cuadrado, cubo, esfera")

    @staticmethod
    def get_tipos_disponibles():
        """Retorna la lista de tipos de figuras disponibles."""
        return ['circulo', 'cuadrado', 'cubo', 'esfera']

    @staticmethod
    def validar_parametros(tipo_figura, **kwargs):
        """
        Valida que los parÃ¡metros proporcionados sean correctos para el tipo de figura.

        Args:
            tipo_figura (str): Tipo de figura
            **kwargs: ParÃ¡metros a validar

        Returns:
            bool: True si los parÃ¡metros son vÃ¡lidos

        Raises:
            ValueError: Si los parÃ¡metros no son vÃ¡lidos
        """
        tipo_figura = tipo_figura.lower().strip()

        if tipo_figura not in FiguraFactory.get_tipos_disponibles():
            raise ValueError(f"Tipo de figura no vÃ¡lido: {tipo_figura}")

        if tipo_figura in ['circulo', 'esfera']:
            radio = kwargs.get('radio')
            if radio is None:
                raise ValueError(f"Se requiere el parÃ¡metro 'radio' para {tipo_figura}")
            ValidadorEntrada.validar_radio(radio)

        elif tipo_figura in ['cuadrado', 'cubo']:
            lado = kwargs.get('lado')
            if lado is None:
                raise ValueError(f"Se requiere el parÃ¡metro 'lado' para {tipo_figura}")
            ValidadorEntrada.validar_lado(lado)

        return True
