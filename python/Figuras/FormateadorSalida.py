"""
Clase para formatear la salida hacia el usuario
"""
from typing import List, Dict, Any
from .Figura import Figura
from .Figura2d import Figura2d
from .Figura3d import Figura3d
from .UnidadMedida import UnidadMedida
from .UnidadAdapter import UnidadAdapter


class FormateadorSalida:
    """Clase para formatear y presentar información al usuario"""
    
    @staticmethod
    def formatear_menu(titulo: str, opciones: List[str], info: str = None) -> str:
        """
        Formatea un menú para mostrar al usuario
        
        Args:
            titulo (str): Título del menú
            opciones (List[str]): Lista de opciones del menú
            info (str): Información adicional (opcional)
            
        Returns:
            str: Menú formateado
        """
        linea_separadora = "=" * 50
        resultado = [linea_separadora]
        resultado.append(f" {titulo.center(48)} ")
        resultado.append(linea_separadora)
        
        if info:
            resultado.append(f"ℹ️  {info}")
            resultado.append("")
        
        for i, opcion in enumerate(opciones, 1):
            resultado.append(f"{i:2d}. {opcion}")
        
        resultado.append(linea_separadora)
        
        return "\n".join(resultado)
    
    @staticmethod
    def formatear_figura(figura: Figura, unidad: UnidadMedida) -> str:
        """
        Formatea la información de una figura
        
        Args:
            figura (Figura): Figura a formatear
            unidad (UnidadMedida): Unidad de medida a usar
            
        Returns:
            str: Información formateada de la figura
        """
        resultado = []
        resultado.append(f"📐 Figura ID: {figura.get_id()}")
        resultado.append(f"   Tipo: {figura.get_nombre()}")
        resultado.append(f"   Categoría: {figura.get_tipo()}")
        
        # Mostrar dimensiones específicas
        if hasattr(figura, 'get_radio'):
            radio_convertido = UnidadAdapter.convertir(figura.get_radio(), UnidadMedida.METROS, unidad)
            resultado.append(f"   Radio: {UnidadAdapter.formatear_con_unidad(radio_convertido, unidad)}")
        elif hasattr(figura, 'get_lado'):
            lado_convertido = UnidadAdapter.convertir(figura.get_lado(), UnidadMedida.METROS, unidad)
            resultado.append(f"   Lado: {UnidadAdapter.formatear_con_unidad(lado_convertido, unidad)}")
        
        # Mostrar cálculos
        if isinstance(figura, Figura2d):
            area = figura.calcular_area()
            perimetro = figura.calcular_perimetro()
            
            # Convertir área (unidad²) y perímetro
            factor = unidad.get_factor_conversion()
            area_convertida = area / (factor ** 2)
            perimetro_convertido = UnidadAdapter.convertir(perimetro, UnidadMedida.METROS, unidad)
            
            resultado.append(f"   Área: {area_convertida:.2f} {unidad.get_simbolo()}²")
            resultado.append(f"   Perímetro: {UnidadAdapter.formatear_con_unidad(perimetro_convertido, unidad)}")
        
        elif isinstance(figura, Figura3d):
            volumen = figura.calcular_volumen()
            
            # Convertir volumen (unidad³)
            factor = unidad.get_factor_conversion()
            volumen_convertido = volumen / (factor ** 3)
            
            resultado.append(f"   Volumen: {volumen_convertido:.2f} {unidad.get_simbolo()}³")
            
            if hasattr(figura, 'calcular_area_superficie'):
                area_superficie = figura.calcular_area_superficie()
                area_convertida = area_superficie / (factor ** 2)
                resultado.append(f"   Área superficie: {area_convertida:.2f} {unidad.get_simbolo()}²")
        
        return "\n".join(resultado)
    
    @staticmethod
    def formatear_lista_figuras(figuras: List[Figura], unidad: UnidadMedida) -> str:
        """
        Formatea una lista de figuras
        
        Args:
            figuras (List[Figura]): Lista de figuras
            unidad (UnidadMedida): Unidad de medida a usar
            
        Returns:
            str: Lista formateada de figuras
        """
        if not figuras:
            return "📭 No hay figuras para mostrar."
        
        resultado = []
        resultado.append(f"📊 Total de figuras: {len(figuras)}")
        resultado.append("=" * 50)
        
        for i, figura in enumerate(figuras, 1):
            resultado.append(f"\n{i}. {FormateadorSalida.formatear_figura(figura, unidad)}")
        
        return "\n".join(resultado)
    
    @staticmethod
    def formatear_estadisticas(estadisticas: Dict[str, Any]) -> str:
        """
        Formatea las estadísticas del repositorio
        
        Args:
            estadisticas (Dict[str, Any]): Diccionario con estadísticas
            
        Returns:
            str: Estadísticas formateadas
        """
        resultado = []
        resultado.append("📈 ESTADÍSTICAS DEL REPOSITORIO")
        resultado.append("=" * 40)
        resultado.append(f"Total de figuras: {estadisticas.get('total', 0)}")
        resultado.append("")
        resultado.append("Distribución por tipo:")
        
        tipos = ['círculo', 'cuadrado', 'cubo', 'esfera']
        for tipo in tipos:
            cantidad = estadisticas.get(tipo, 0)
            if cantidad > 0:
                porcentaje = (cantidad / estadisticas['total']) * 100 if estadisticas['total'] > 0 else 0
                resultado.append(f"  • {tipo.capitalize()}: {cantidad} ({porcentaje:.1f}%)")
        
        return "\n".join(resultado)
    
    @staticmethod
    def mostrar_error(mensaje: str) -> str:
        """
        Formatea un mensaje de error
        
        Args:
            mensaje (str): Mensaje de error
            
        Returns:
            str: Mensaje de error formateado
        """
        return f"❌ Error: {mensaje}"
    
    @staticmethod
    def mostrar_exito(mensaje: str) -> str:
        """
        Formatea un mensaje de éxito
        
        Args:
            mensaje (str): Mensaje de éxito
            
        Returns:
            str: Mensaje de éxito formateado
        """
        return f"✅ {mensaje}"
    
    @staticmethod
    def mostrar_info(mensaje: str) -> str:
        """
        Formatea un mensaje informativo
        
        Args:
            mensaje (str): Mensaje informativo
            
        Returns:
            str: Mensaje informativo formateado
        """
        return f"ℹ️  {mensaje}"