"""
Módulo para manejo de entrada y salida de datos.
Se encarga exclusivamente de validar entradas y formatear salidas.
"""
from typing import Dict, Any, Union
from figura import Figura

class ValidadorEntrada:
    """Clase responsable de validar entradas de datos para figuras."""
    
    @staticmethod
    def validar_numero_positivo(valor: Union[int, float], nombre_parametro: str) -> float:
        """
        Valida que un valor sea un número positivo.
        
        Args:
            valor: Valor a validar
            nombre_parametro: Nombre del parámetro para mensajes de error
            
        Returns:
            float: Valor validado
            
        Raises:
            ValueError: Si el valor no es válido
        """
        if not isinstance(valor, (int, float)):
            raise ValueError(f"El {nombre_parametro} debe ser un número")
        
        if valor <= 0:
            raise ValueError(f"El {nombre_parametro} debe ser mayor que 0")
        
        return float(valor)
    
    @staticmethod
    def validar_radio(radio: Union[int, float]) -> float:
        """
        Valida un radio.
        
        Args:
            radio: Radio a validar
            
        Returns:
            float: Radio validado
        """
        return ValidadorEntrada.validar_numero_positivo(radio, "radio")
    
    @staticmethod
    def validar_lado(lado: Union[int, float]) -> float:
        """
        Valida un lado.
        
        Args:
            lado: Lado a validar
            
        Returns:
            float: Lado validado
        """
        return ValidadorEntrada.validar_numero_positivo(lado, "lado")
    
    @staticmethod
    def validar_entero_positivo(valor: Union[int, str], nombre_parametro: str) -> int:
        """
        Valida que un valor sea un entero positivo.
        
        Args:
            valor: Valor a validar
            nombre_parametro: Nombre del parámetro para mensajes de error
            
        Returns:
            int: Valor validado
            
        Raises:
            ValueError: Si el valor no es válido
        """
        try:
            valor_int = int(valor)
        except (ValueError, TypeError):
            raise ValueError(f"El {nombre_parametro} debe ser un número entero")
        
        if valor_int <= 0:
            raise ValueError(f"El {nombre_parametro} debe ser mayor que 0")
        
        return valor_int
    
    @staticmethod
    def validar_opcion_menu(opcion: str, min_opcion: int, max_opcion: int) -> int:
        """
        Valida una opción de menú.
        
        Args:
            opcion: Opción a validar
            min_opcion: Opción mínima válida
            max_opcion: Opción máxima válida
            
        Returns:
            int: Opción validada
            
        Raises:
            ValueError: Si la opción no es válida
        """
        try:
            opcion_int = int(opcion.strip())
        except (ValueError, AttributeError):
            raise ValueError(f"Ingrese un número válido entre {min_opcion} y {max_opcion}")
        
        if not (min_opcion <= opcion_int <= max_opcion):
            raise ValueError(f"La opción debe estar entre {min_opcion} y {max_opcion}")
        
        return opcion_int

class LectorEntrada:
    """Clase para leer y procesar entradas del usuario."""
    
    @staticmethod
    def leer_numero_positivo(mensaje: str, permite_decimales: bool = True) -> float:
        """
        Lee un número positivo del usuario con validación.
        
        Args:
            mensaje: Mensaje a mostrar al usuario
            permite_decimales: Si acepta números decimales
            
        Returns:
            float: Número ingresado y validado
        """
        while True:
            try:
                entrada = input(mensaje).strip()
                if entrada == "":
                    print("❌ No puede estar vacío. Intente de nuevo.")
                    continue
                    
                valor = float(entrada) if permite_decimales else int(entrada)
                return ValidadorEntrada.validar_numero_positivo(valor, "valor")
                
            except ValueError as e:
                print(f"❌ Error: {e}")
            except KeyboardInterrupt:
                print("\n⚠️ Operación cancelada por el usuario.")
                raise
    
    @staticmethod
    def leer_opcion_menu(mensaje: str, min_opcion: int, max_opcion: int) -> int:
        """
        Lee una opción de menú del usuario.
        
        Args:
            mensaje: Mensaje a mostrar
            min_opcion: Opción mínima válida
            max_opcion: Opción máxima válida
            
        Returns:
            int: Opción seleccionada
        """
        while True:
            try:
                entrada = input(mensaje).strip()
                if entrada == "":
                    print(f"❌ Seleccione una opción entre {min_opcion} y {max_opcion}.")
                    continue
                    
                return ValidadorEntrada.validar_opcion_menu(entrada, min_opcion, max_opcion)
                
            except ValueError as e:
                print(f"❌ Error: {e}")
            except KeyboardInterrupt:
                print("\n⚠️ Operación cancelada por el usuario.")
                raise
    
    @staticmethod
    def leer_confirmacion(mensaje: str, opciones_si: list = None) -> bool:
        """
        Lee una confirmación del usuario.
        
        Args:
            mensaje: Mensaje de confirmación
            opciones_si: Lista de opciones que se consideran afirmativas
            
        Returns:
            bool: True si el usuario confirma
        """
        if opciones_si is None:
            opciones_si = ['s', 'si', 'sí', 'yes', 'y']
        
        try:
            respuesta = input(mensaje).strip().lower()
            return respuesta in opciones_si
        except KeyboardInterrupt:
            print("\n⚠️ Operación cancelada por el usuario.")
            return False
    
    @staticmethod
    def leer_texto(mensaje: str, permitir_vacio: bool = False) -> str:
        """
        Lee un texto del usuario.
        
        Args:
            mensaje: Mensaje a mostrar
            permitir_vacio: Si permite texto vacío
            
        Returns:
            str: Texto ingresado
        """
        while True:
            try:
                texto = input(mensaje).strip()
                if not permitir_vacio and texto == "":
                    print("❌ No puede estar vacío. Intente de nuevo.")
                    continue
                return texto
            except KeyboardInterrupt:
                print("\n⚠️ Operación cancelada por el usuario.")
                raise

class FormateadorSalida:
    """Clase responsable de formatear la salida de información de figuras."""
    
    @staticmethod
    def formatear_figura_basica(figura: Figura) -> str:
        """
        Formatea información básica de una figura.
        
        Args:
            figura: Instancia de figura
            
        Returns:
            str: Información formateada
        """
        info = f"ID: {figura.get_id()}, Tipo: {figura.get_nombre()} ({figura.get_tipo()})"
        
        if hasattr(figura, 'radio'):
            info += f", Radio: {figura.radio:.2f}"
        if hasattr(figura, 'lado'):
            info += f", Lado: {figura.lado:.2f}"
            
        return info
    
    @staticmethod
    def formatear_figura_completa(figura: Figura) -> str:
        """
        Formatea información completa de una figura.
        
        Args:
            figura: Instancia de figura
            
        Returns:
            str: Información detallada formateada
        """
        lineas = []
        lineas.append(f"🆔 ID: {figura.get_id()}")
        lineas.append(f"📐 Tipo: {figura.get_nombre()} ({figura.get_tipo()})")
        
        # Dimensiones
        if hasattr(figura, 'radio'):
            lineas.append(f"📏 Radio: {figura.radio:.2f}")
        if hasattr(figura, 'lado'):
            lineas.append(f"📏 Lado: {figura.lado:.2f}")
        
        # Medidas calculadas
        if hasattr(figura, 'calcular_area'):
            lineas.append(f"📦 Área: {figura.calcular_area():.2f}")
        if hasattr(figura, 'calcular_perimetro'):
            lineas.append(f"📏 Perímetro: {figura.calcular_perimetro():.2f}")
        if hasattr(figura, 'calcular_volumen'):
            lineas.append(f"🧊 Volumen: {figura.calcular_volumen():.2f}")
        
        return "\n".join(lineas)
    
    @staticmethod
    def formatear_lista_figuras(figuras: list, mostrar_detalle: bool = False) -> str:
        """
        Formatea una lista de figuras.
        
        Args:
            figuras: Lista de figuras
            mostrar_detalle: Si mostrar información detallada
            
        Returns:
            str: Lista formateada
        """
        if not figuras:
            return "📋 No hay figuras para mostrar."
        
        lineas = [f"📋 FIGURAS ({len(figuras)} total)"]
        lineas.append("=" * 60)
        
        for figura in sorted(figuras, key=lambda f: f.get_id()):
            if mostrar_detalle:
                lineas.append(FormateadorSalida.formatear_figura_completa(figura))
                lineas.append("-" * 60)
            else:
                lineas.append(FormateadorSalida.formatear_figura_basica(figura))
        
        return "\n".join(lineas)
    
    @staticmethod
    def formatear_estadisticas(stats: Dict[str, Any]) -> str:
        """
        Formatea estadísticas del sistema.
        
        Args:
            stats: Diccionario con estadísticas
            
        Returns:
            str: Estadísticas formateadas
        """
        lineas = []
        lineas.append("📊 ESTADÍSTICAS DEL SISTEMA")
        lineas.append("=" * 40)
        lineas.append(f"Total de figuras: {stats.get('total_figuras', 0)}")
        
        if 'tipos_figuras' in stats and stats['tipos_figuras']:
            lineas.append("\nDistribución por tipo:")
            for tipo, cantidad in stats['tipos_figuras'].items():
                lineas.append(f"  • {tipo}: {cantidad}")
        
        if 'ids_disponibles' in stats and stats['ids_disponibles']:
            ids = sorted(stats['ids_disponibles'])
            lineas.append(f"\nIDs en uso: {ids}")
        
        if 'archivo_persistencia' in stats:
            lineas.append(f"\nArchivo de persistencia: {stats['archivo_persistencia']}")
            existe = "✅ Sí" if stats.get('archivo_existe', False) else "❌ No"
            lineas.append(f"Archivo existe: {existe}")
        
        return "\n".join(lineas)
    
    @staticmethod
    def formatear_menu(titulo: str, opciones: list, info_adicional: str = None) -> str:
        """
        Formatea un menú de opciones.
        
        Args:
            titulo: Título del menú
            opciones: Lista de opciones
            info_adicional: Información adicional a mostrar
            
        Returns:
            str: Menú formateado
        """
        lineas = []
        separador = "=" * len(titulo)
        
        lineas.append(separador)
        lineas.append(titulo)
        lineas.append(separador)
        
        for i, opcion in enumerate(opciones, 1):
            lineas.append(f"{i}. {opcion}")
        
        lineas.append("-" * len(titulo))
        
        if info_adicional:
            lineas.append(info_adicional)
            lineas.append("-" * len(titulo))
        
        return "\n".join(lineas)
    
    @staticmethod
    def formatear_mensaje_exito(mensaje: str) -> str:
        """Formatea un mensaje de éxito."""
        return f"✅ {mensaje}"
    
    @staticmethod
    def formatear_mensaje_error(mensaje: str) -> str:
        """Formatea un mensaje de error."""
        return f"❌ {mensaje}"
    
    @staticmethod
    def formatear_mensaje_advertencia(mensaje: str) -> str:
        """Formatea un mensaje de advertencia."""
        return f"⚠️ {mensaje}"
    
    @staticmethod
    def formatear_mensaje_info(mensaje: str) -> str:
        """Formatea un mensaje informativo."""
        return f"ℹ️ {mensaje}"
    
    @staticmethod
    def formatear_info_figura(figura, unidad_actual, adapter):
        """
        Formatea la información completa de una figura.
        
        Args:
            figura: Objeto figura
            unidad_actual: Unidad de medida actual
            adapter: Adaptador de unidades
            
        Returns:
            str: Información formateada de la figura
        """
        try:
            from unidad_adapter import UnidadMedida
            
            # Información básica
            info_lines = [
                f"🆔 ID: {figura.get_id()}",
                f"📐 Tipo: {figura.get_nombre()}",
                f"📏 Unidad: {UnidadMedida.get_nombres_completos()[unidad_actual]}"
            ]
            
            # Dimensiones específicas según el tipo
            if hasattr(figura, 'radio'):
                radio_convertido = adapter.convertir(figura.radio, UnidadMedida.METROS, unidad_actual)
                info_lines.append(f"🔵 Radio: {radio_convertido:.4f} {unidad_actual}")
            
            if hasattr(figura, 'lado'):
                lado_convertido = adapter.convertir(figura.lado, UnidadMedida.METROS, unidad_actual)
                info_lines.append(f"📏 Lado: {lado_convertido:.4f} {unidad_actual}")
            
            # Cálculos según dimensión
            if hasattr(figura, 'calcular_area') and hasattr(figura, 'calcular_perimetro'):
                # Figura 2D
                area_original = figura.calcular_area()
                perimetro_original = figura.calcular_perimetro()
                
                area_convertida = adapter.convertir_area(area_original, UnidadMedida.METROS, unidad_actual)
                perimetro_convertido = adapter.convertir(perimetro_original, UnidadMedida.METROS, unidad_actual)
                
                info_lines.append(f"🔺 Área: {area_convertida:.4f} {unidad_actual}²")
                info_lines.append(f"📐 Perímetro: {perimetro_convertido:.4f} {unidad_actual}")
            
            elif hasattr(figura, 'calcular_volumen') and hasattr(figura, 'calcular_superficie'):
                # Figura 3D
                volumen_original = figura.calcular_volumen()
                superficie_original = figura.calcular_superficie()
                
                volumen_convertido = adapter.convertir_volumen(volumen_original, UnidadMedida.METROS, unidad_actual)
                superficie_convertida = adapter.convertir_area(superficie_original, UnidadMedida.METROS, unidad_actual)
                
                info_lines.append(f"📦 Volumen: {volumen_convertido:.4f} {unidad_actual}³")
                info_lines.append(f"🔲 Superficie: {superficie_convertida:.4f} {unidad_actual}²")
            
            return "\n".join(info_lines)
            
        except Exception as e:
            return f"❌ Error al formatear figura: {e}"
