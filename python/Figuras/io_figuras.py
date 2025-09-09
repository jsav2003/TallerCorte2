﻿"""
MÃ³dulo para manejo de entrada y salida de datos.
Se encarga exclusivamente de validar entradas y formatear salidas.
"""
from typing import Dict, Any, Union
from figura import Figura

class ValidadorEntrada:
    """Clase responsable de validar entradas de datos para figuras."""

    @staticmethod
    def validar_numero_positivo(valor: Union[int, float], nombre_parametro: str) -> float:
        """
        Valida que un valor sea un nÃºmero positivo.

        Args:
            valor: Valor a validar
            nombre_parametro: Nombre del parÃ¡metro para mensajes de error

        Returns:
            float: Valor validado

        Raises:
            ValueError: Si el valor no es vÃ¡lido
        """
        if not isinstance(valor, (int, float)):
            raise ValueError(f"El {nombre_parametro} debe ser un nÃºmero")

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
            nombre_parametro: Nombre del parÃ¡metro para mensajes de error

        Returns:
            int: Valor validado

        Raises:
            ValueError: Si el valor no es vÃ¡lido
        """
        try:
            valor_int = int(valor)
        except (ValueError, TypeError):
            raise ValueError(f"El {nombre_parametro} debe ser un nÃºmero entero")

        if valor_int <= 0:
            raise ValueError(f"El {nombre_parametro} debe ser mayor que 0")

        return valor_int

    @staticmethod
    def validar_opcion_menu(opcion: str, min_opcion: int, max_opcion: int) -> int:
        """
        Valida una opciÃ³n de menÃº.

        Args:
            opcion: OpciÃ³n a validar
            min_opcion: OpciÃ³n mÃ­nima vÃ¡lida
            max_opcion: OpciÃ³n mÃ¡xima vÃ¡lida

        Returns:
            int: OpciÃ³n validada

        Raises:
            ValueError: Si la opciÃ³n no es vÃ¡lida
        """
        try:
            opcion_int = int(opcion.strip())
        except (ValueError, AttributeError):
            raise ValueError(f"Ingrese un nÃºmero vÃ¡lido entre {min_opcion} y {max_opcion}")

        if not (min_opcion <= opcion_int <= max_opcion):
            raise ValueError(f"La opciÃ³n debe estar entre {min_opcion} y {max_opcion}")

        return opcion_int

class LectorEntrada:
    """Clase para leer y procesar entradas del usuario."""

    @staticmethod
    def leer_numero_positivo(mensaje: str, permite_decimales: bool = True) -> float:
        """
        Lee un nÃºmero positivo del usuario con validaciÃ³n.

        Args:
            mensaje: Mensaje a mostrar al usuario
            permite_decimales: Si acepta nÃºmeros decimales

        Returns:
            float: NÃºmero ingresado y validado
        """
        while True:
            try:
                entrada = input(mensaje).strip()
                if entrada == "":
                    print("âŒ No puede estar vacÃ­o. Intente de nuevo.")
                    continue

                valor = float(entrada) if permite_decimales else int(entrada)
                return ValidadorEntrada.validar_numero_positivo(valor, "valor")

            except ValueError as e:
                print(f"âŒ Error: {e}")
            except KeyboardInterrupt:
                print("\nâš ï¸ OperaciÃ³n cancelada por el usuario.")
                raise

    @staticmethod
    def leer_opcion_menu(mensaje: str, min_opcion: int, max_opcion: int) -> int:
        """
        Lee una opciÃ³n de menÃº del usuario.

        Args:
            mensaje: Mensaje a mostrar
            min_opcion: OpciÃ³n mÃ­nima vÃ¡lida
            max_opcion: OpciÃ³n mÃ¡xima vÃ¡lida

        Returns:
            int: OpciÃ³n seleccionada
        """
        while True:
            try:
                entrada = input(mensaje).strip()
                if entrada == "":
                    print(f"âŒ Seleccione una opciÃ³n entre {min_opcion} y {max_opcion}.")
                    continue

                return ValidadorEntrada.validar_opcion_menu(entrada, min_opcion, max_opcion)

            except ValueError as e:
                print(f"âŒ Error: {e}")
            except KeyboardInterrupt:
                print("\nâš ï¸ OperaciÃ³n cancelada por el usuario.")
                raise

    @staticmethod
    def leer_confirmacion(mensaje: str, opciones_si: list = None) -> bool:
        """
        Lee una confirmaciÃ³n del usuario.

        Args:
            mensaje: Mensaje de confirmaciÃ³n
            opciones_si: Lista de opciones que se consideran afirmativas

        Returns:
            bool: True si el usuario confirma
        """
        if opciones_si is None:
            opciones_si = ['s', 'si', 'sÃ­', 'yes', 'y']

        try:
            respuesta = input(mensaje).strip().lower()
            return respuesta in opciones_si
        except KeyboardInterrupt:
            print("\nâš ï¸ OperaciÃ³n cancelada por el usuario.")
            return False

    @staticmethod
    def leer_texto(mensaje: str, permitir_vacio: bool = False) -> str:
        """
        Lee un texto del usuario.

        Args:
            mensaje: Mensaje a mostrar
            permitir_vacio: Si permite texto vacÃ­o

        Returns:
            str: Texto ingresado
        """
        while True:
            try:
                texto = input(mensaje).strip()
                if not permitir_vacio and texto == "":
                    print("âŒ No puede estar vacÃ­o. Intente de nuevo.")
                    continue
                return texto
            except KeyboardInterrupt:
                print("\nâš ï¸ OperaciÃ³n cancelada por el usuario.")
                raise

class FormateadorSalida:
    """Clase responsable de formatear la salida de informaciÃ³n de figuras."""

    @staticmethod
    def formatear_figura_basica(figura: Figura) -> str:
        """
        Formatea informaciÃ³n bÃ¡sica de una figura.

        Args:
            figura: Instancia de figura

        Returns:
            str: InformaciÃ³n formateada
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
        Formatea informaciÃ³n completa de una figura.

        Args:
            figura: Instancia de figura

        Returns:
            str: InformaciÃ³n detallada formateada
        """
        lineas = []
        lineas.append(f"ðŸ†” ID: {figura.get_id()}")
        lineas.append(f"ðŸ“ Tipo: {figura.get_nombre()} ({figura.get_tipo()})")

        # Dimensiones
        if hasattr(figura, 'radio'):
            lineas.append(f"ðŸ“ Radio: {figura.radio:.2f}")
        if hasattr(figura, 'lado'):
            lineas.append(f"ðŸ“ Lado: {figura.lado:.2f}")

        # Medidas calculadas
        if hasattr(figura, 'calcular_area'):
            lineas.append(f"ðŸ“¦ Ãrea: {figura.calcular_area():.2f}")
        if hasattr(figura, 'calcular_perimetro'):
            lineas.append(f"ðŸ“ PerÃ­metro: {figura.calcular_perimetro():.2f}")
        if hasattr(figura, 'calcular_volumen'):
            lineas.append(f"ðŸ§Š Volumen: {figura.calcular_volumen():.2f}")

        return "\n".join(lineas)

    @staticmethod
    def formatear_lista_figuras(figuras: list, mostrar_detalle: bool = False) -> str:
        """
        Formatea una lista de figuras.

        Args:
            figuras: Lista de figuras
            mostrar_detalle: Si mostrar informaciÃ³n detallada

        Returns:
            str: Lista formateada
        """
        if not figuras:
            return "ðŸ“‹ No hay figuras para mostrar."

        lineas = [f"ðŸ“‹ FIGURAS ({len(figuras)} total)"]
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
        Formatea estadÃ­sticas del sistema.

        Args:
            stats: Diccionario con estadÃ­sticas

        Returns:
            str: EstadÃ­sticas formateadas
        """
        lineas = []
        lineas.append("ðŸ“Š ESTADÃSTICAS DEL SISTEMA")
        lineas.append("=" * 40)
        lineas.append(f"Total de figuras: {stats.get('total_figuras', 0)}")

        if 'tipos_figuras' in stats and stats['tipos_figuras']:
            lineas.append("\nDistribuciÃ³n por tipo:")
            for tipo, cantidad in stats['tipos_figuras'].items():
                lineas.append(f"  â€¢ {tipo}: {cantidad}")

        if 'ids_disponibles' in stats and stats['ids_disponibles']:
            ids = sorted(stats['ids_disponibles'])
            lineas.append(f"\nIDs en uso: {ids}")

        if 'archivo_persistencia' in stats:
            lineas.append(f"\nArchivo de persistencia: {stats['archivo_persistencia']}")
            existe = "âœ… SÃ­" if stats.get('archivo_existe', False) else "âŒ No"
            lineas.append(f"Archivo existe: {existe}")

        return "\n".join(lineas)

    @staticmethod
    def formatear_menu(titulo: str, opciones: list, info_adicional: str = None) -> str:
        """
        Formatea un menÃº de opciones.

        Args:
            titulo: TÃ­tulo del menÃº
            opciones: Lista de opciones
            info_adicional: InformaciÃ³n adicional a mostrar

        Returns:
            str: MenÃº formateado
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
        """Formatea un mensaje de Ã©xito."""
        return f"âœ… {mensaje}"

    @staticmethod
    def formatear_mensaje_error(mensaje: str) -> str:
        """Formatea un mensaje de error."""
        return f"âŒ {mensaje}"

    @staticmethod
    def formatear_mensaje_advertencia(mensaje: str) -> str:
        """Formatea un mensaje de advertencia."""
        return f"âš ï¸ {mensaje}"

    @staticmethod
    def formatear_mensaje_info(mensaje: str) -> str:
        """Formatea un mensaje informativo."""
        return f"â„¹ï¸ {mensaje}"

    @staticmethod
    def formatear_info_figura(figura, unidad_actual, adapter):
        """
        Formatea la informaciÃ³n completa de una figura.

        Args:
            figura: Objeto figura
            unidad_actual: Unidad de medida actual
            adapter: Adaptador de unidades

        Returns:
            str: InformaciÃ³n formateada de la figura
        """
        try:
            from unidad_adapter import UnidadMedida

            # InformaciÃ³n bÃ¡sica
            info_lines = [
                f"ðŸ†” ID: {figura.get_id()}",
                f"ðŸ“ Tipo: {figura.get_nombre()}",
                f"ðŸ“ Unidad: {UnidadMedida.get_nombres_completos()[unidad_actual]}"
            ]

            # Dimensiones especÃ­ficas segÃºn el tipo
            if hasattr(figura, 'radio'):
                radio_convertido = adapter.convertir(figura.radio, UnidadMedida.METROS, unidad_actual)
                info_lines.append(f"ðŸ”µ Radio: {radio_convertido:.4f} {unidad_actual}")

            if hasattr(figura, 'lado'):
                lado_convertido = adapter.convertir(figura.lado, UnidadMedida.METROS, unidad_actual)
                info_lines.append(f"ðŸ“ Lado: {lado_convertido:.4f} {unidad_actual}")

            # CÃ¡lculos segÃºn dimensiÃ³n
            if hasattr(figura, 'calcular_area') and hasattr(figura, 'calcular_perimetro'):
                # Figura 2D
                area_original = figura.calcular_area()
                perimetro_original = figura.calcular_perimetro()

                area_convertida = adapter.convertir_area(area_original, UnidadMedida.METROS, unidad_actual)
                perimetro_convertido = adapter.convertir(perimetro_original, UnidadMedida.METROS, unidad_actual)

                info_lines.append(f"ðŸ”º Ãrea: {area_convertida:.4f} {unidad_actual}Â²")
                info_lines.append(f"ðŸ“ PerÃ­metro: {perimetro_convertido:.4f} {unidad_actual}")

            elif hasattr(figura, 'calcular_volumen') and hasattr(figura, 'calcular_superficie'):
                # Figura 3D
                volumen_original = figura.calcular_volumen()
                superficie_original = figura.calcular_superficie()

                volumen_convertido = adapter.convertir_volumen(volumen_original, UnidadMedida.METROS, unidad_actual)
                superficie_convertida = adapter.convertir_area(superficie_original, UnidadMedida.METROS, unidad_actual)

                info_lines.append(f"ðŸ“¦ Volumen: {volumen_convertido:.4f} {unidad_actual}Â³")
                info_lines.append(f"ðŸ”² Superficie: {superficie_convertida:.4f} {unidad_actual}Â²")

            return "\n".join(info_lines)

        except Exception as e:
            return f"âŒ Error al formatear figura: {e}"
