"""
Factory para crear figuras geométricas
"""
from typing import Union, List
from .Figura import Figura
from .Circulo import Circulo
from .Cuadrado import Cuadrado
from .Cubo import Cubo
from .Esfera import Esfera
from .GeneradorID import GeneradorID


class FiguraFactory:
    """Factory para crear diferentes tipos de figuras geométricas"""
    
    @staticmethod
    def crear_figura(tipo: str, dimensiones: Union[float, List[float]]) -> Figura:
        """
        Crea una figura según el tipo especificado
        
        Args:
            tipo (str): Tipo de figura ('circulo', 'cuadrado', 'cubo', 'esfera')
            dimensiones (Union[float, List[float]]): Dimensiones de la figura
            
        Returns:
            Figura: Instancia de la figura creada
            
        Raises:
            ValueError: Si el tipo de figura no es válido
        """
        tipo = tipo.lower()
        id_figura = GeneradorID.obtener_siguiente_id()
        
        if tipo == "circulo":
            if isinstance(dimensiones, list):
                radio = dimensiones[0]
            else:
                radio = dimensiones
            return Circulo(radio, id_figura)
        
        elif tipo == "cuadrado":
            if isinstance(dimensiones, list):
                lado = dimensiones[0]
            else:
                lado = dimensiones
            return Cuadrado(lado, id_figura)
        
        elif tipo == "cubo":
            if isinstance(dimensiones, list):
                lado = dimensiones[0]
            else:
                lado = dimensiones
            return Cubo(lado, id_figura)
        
        elif tipo == "esfera":
            if isinstance(dimensiones, list):
                radio = dimensiones[0]
            else:
                radio = dimensiones
            return Esfera(radio, id_figura)
        
        else:
            raise ValueError(f"Tipo de figura no válido: {tipo}")
    
    @staticmethod
    def tipos_disponibles() -> List[str]:
        """
        Retorna una lista de los tipos de figuras disponibles
        
        Returns:
            List[str]: Lista de tipos de figuras disponibles
        """
        return ["circulo", "cuadrado", "cubo", "esfera"]