
"""
MÃ³dulo para gestionar la interacciÃ³n con el usuario y las figuras geomÃ©tricas.
VersiÃ³n mejorada con soporte para IDs Ãºnicos, unidades de medida, persistencia y mÃ¡s.
"""
from figura_factory import FiguraFactory
from repositorio_figuras import RepositorioFiguras
from unidad_adapter import UnidadAdapter, UnidadMedida
from io_figuras import LectorEntrada, FormateadorSalida
import sys

class Gestionar:
    """
    Clase para gestionar el menÃº y la interacciÃ³n con figuras geomÃ©tricas.
    Incluye todas las nuevas funcionalidades requeridas.
    """

    def __init__(self):
        """Inicializa el gestor con repositorio y adapter."""
        self.repositorio = RepositorioFiguras()
        self.adapter = UnidadAdapter()
        self.unidad_actual = UnidadMedida.METROS  # Unidad por defecto
        self.lector = LectorEntrada()
        self.formateador = FormateadorSalida()

    def mostrar_menu_principal(self):
        """Muestra el menÃº principal del sistema."""
        opciones = [
            "Crear nueva figura",
            "Consultar todas las figuras",
            "Consultar figura por ID",
            "Eliminar figura por ID",
            "Cambiar unidad de medida",
            "Buscar figuras por tipo",
            "Ver estadÃ­sticas",
            "Guardar figuras",
            "Cargar figuras",
            "Limpiar repositorio",
            "Salir"
        ]

        unidad_nombre = UnidadMedida.get_nombres_completos()[self.unidad_actual]
        info_adicional = (f"ï¿½ Unidad actual: {unidad_nombre}\n"
                         f"ï¿½ðŸ“Š Figuras en memoria: {self.repositorio.contar_figuras()}")

        menu = self.formateador.formatear_menu(
            "    GESTOR DE FIGURAS GEOMÃ‰TRICAS V2.0",
            opciones,
            info_adicional
        )

        print("\n" + menu)

    def mostrar_menu_crear_figura(self):
        """Muestra el menÃº de creaciÃ³n de figuras."""
        opciones = ["Circulo", "Cuadrado", "Cubo", "Esfera", "Volver al menÃº principal"]
        menu = self.formateador.formatear_menu("    CREAR NUEVA FIGURA", opciones)
        print("\n" + menu)

    def mostrar_menu_unidades(self):
        """Muestra el menÃº de selecciÃ³n de unidades."""
        unidades = UnidadMedida.get_unidades_disponibles()
        nombres = UnidadMedida.get_nombres_completos()

        opciones_formateadas = []
        for unidad in unidades:
            marca = "âœ“" if unidad == self.unidad_actual else " "
            opciones_formateadas.append(f"{marca} {nombres[unidad]} ({unidad})")

        opciones_formateadas.append("Volver al menÃº principal")

        menu = self.formateador.formatear_menu("    SELECCIONAR UNIDAD DE MEDIDA", opciones_formateadas)
        print("\n" + menu)

    def crear_figura(self):
        """Maneja el proceso de creaciÃ³n de figuras."""
        while True:
            try:
                self.mostrar_menu_crear_figura()
                opcion = self.lector.leer_opcion_menu(
                    f"Seleccione una opciÃ³n (1-5): ", 1, 5
                )

                if opcion == 5:
                    return

                figura = None

                if opcion == 1:  # Circulo
                    radio = self.lector.leer_numero_positivo("Ingrese el radio del circulo: ")
                    figura = FiguraFactory.crear_figura('circulo', radio=radio)

                elif opcion == 2:  # Cuadrado
                    lado = self.lector.leer_numero_positivo("Ingrese el lado del cuadrado: ")
                    figura = FiguraFactory.crear_figura('cuadrado', lado=lado)

                elif opcion == 3:  # Cubo
                    lado = self.lector.leer_numero_positivo("Ingrese el lado del cubo: ")
                    figura = FiguraFactory.crear_figura('cubo', lado=lado)
                elif opcion == 4:  # Esfera
                    radio = self.lector.leer_numero_positivo("Ingrese el radio de la esfera: ")
                    figura = FiguraFactory.crear_figura('esfera', radio=radio)

                if figura:
                    id_asignado = self.repositorio.almacenar_figura(figura)
                    print(f"\n{self.formateador.formatear_mensaje_exito(f'{figura.get_nombre()} creado exitosamente!')}")
                    print(f"ðŸ†” ID asignado: {id_asignado}")
                    self.mostrar_figura_detallada(figura)
                    return

            except ValueError as e:
                print(self.formateador.formatear_mensaje_error(str(e)))
            except KeyboardInterrupt:
                print(self.formateador.formatear_mensaje_advertencia("OperaciÃ³n cancelada"))
                return
            except Exception as e:
                print(self.formateador.formatear_mensaje_error(f"Error inesperado: {e}"))

            self.pausar()

    def consultar_todas_figuras(self):
        """Consulta y muestra todas las figuras almacenadas."""
        figuras = self.repositorio.obtener_todas_figuras()

        if not figuras:
            print(f"\n{self.formateador.formatear_mensaje_info('No hay figuras almacenadas.')}")
            return

        print(f"\nðŸ“‹ FIGURAS ALMACENADAS ({len(figuras)} total)")
        print("="*60)

        for figura in sorted(figuras, key=lambda f: f.get_id()):
            self.mostrar_figura_detallada(figura)
            print("-"*60)

    def consultar_figura_por_id(self):
        """Consulta una figura especÃ­fica por su ID."""
        try:
            figura_id = int(self.lector.leer_numero_positivo("Ingrese el ID de la figura: ", False))
            figura = self.repositorio.obtener_figura(figura_id)

            if figura is None:
                print(self.formateador.formatear_mensaje_error(f"No se encontrÃ³ ninguna figura con ID {figura_id}"))
            else:
                print(f"\nðŸ” FIGURA ENCONTRADA:")
                print("="*40)
                self.mostrar_figura_detallada(figura)

        except KeyboardInterrupt:
            print(self.formateador.formatear_mensaje_advertencia("OperaciÃ³n cancelada"))
        except Exception as e:
            print(self.formateador.formatear_mensaje_error(f"Error: {e}"))

    def eliminar_figura(self):
        """Elimina una figura por su ID."""
        try:
            figura_id = int(self.lector.leer_numero_positivo("Ingrese el ID de la figura a eliminar: ", False))
            figura = self.repositorio.obtener_figura(figura_id)

            if figura is None:
                print(self.formateador.formatear_mensaje_error(f"No se encontrÃ³ ninguna figura con ID {figura_id}"))
                return

            print(f"\nâš ï¸  Va a eliminar la siguiente figura:")
            self.mostrar_figura_detallada(figura)

            if self.lector.leer_confirmacion("\nÂ¿EstÃ¡ seguro? (s/N): "):
                if self.repositorio.eliminar_figura(figura_id):
                    print(self.formateador.formatear_mensaje_exito(f"Figura con ID {figura_id} eliminada exitosamente."))
                else:
                    print(self.formateador.formatear_mensaje_error("Error al eliminar la figura."))
            else:
                print(self.formateador.formatear_mensaje_info("EliminaciÃ³n cancelada."))

        except KeyboardInterrupt:
            print(self.formateador.formatear_mensaje_advertencia("OperaciÃ³n cancelada"))
        except Exception as e:
            print(self.formateador.formatear_mensaje_error(f"Error: {e}"))

    def cambiar_unidad_medida(self):
        """Permite cambiar la unidad de medida del sistema."""
        while True:
            try:
                self.mostrar_menu_unidades()
                opcion = self.lector.leer_opcion_menu(f"Seleccione una opciÃ³n (1-5): ", 1, 5)

                if opcion == 5:
                    return

                unidades = UnidadMedida.get_unidades_disponibles()
                if 1 <= opcion <= len(unidades):
                    nueva_unidad = unidades[opcion - 1]
                    self.unidad_actual = nueva_unidad
                    nombre_unidad = UnidadMedida.get_nombres_completos()[nueva_unidad]
                    print(self.formateador.formatear_mensaje_exito(f"Unidad cambiada a: {nombre_unidad} ({nueva_unidad})"))
                    return

            except KeyboardInterrupt:
                print(self.formateador.formatear_mensaje_advertencia("OperaciÃ³n cancelada"))
                return
            except Exception as e:
                print(self.formateador.formatear_mensaje_error(f"Error: {e}"))

    def buscar_figuras_por_tipo(self):
        """Busca y muestra figuras por tipo especÃ­fico."""
        try:
            tipos_disponibles = ["Circulo", "Cuadrado", "Cubo", "Esfera"]
            opciones = tipos_disponibles + ["Volver al menÃº principal"]

            menu = self.formateador.formatear_menu("    BUSCAR POR TIPO DE FIGURA", opciones)
            print("\n" + menu)

            opcion = self.lector.leer_opcion_menu(f"Seleccione el tipo (1-{len(opciones)}): ", 1, len(opciones))

            if opcion == len(opciones):  # Ãšltima opciÃ³n: volver
                return

            tipo_buscar = tipos_disponibles[opcion - 1].lower()
            figuras_encontradas = self.repositorio.buscar_por_tipo(tipo_buscar)

            if not figuras_encontradas:
                print(self.formateador.formatear_mensaje_info(f"No se encontraron figuras de tipo '{tipos_disponibles[opcion - 1]}'"))
            else:
                print(f"\nï¿½ FIGURAS DE TIPO '{tipos_disponibles[opcion - 1].upper()}' ({len(figuras_encontradas)} encontradas)")
                print("="*60)
                for figura in figuras_encontradas:
                    self.mostrar_figura_detallada(figura)
                    print("-"*60)

        except KeyboardInterrupt:
            print(self.formateador.formatear_mensaje_advertencia("OperaciÃ³n cancelada"))
        except Exception as e:
            print(self.formateador.formatear_mensaje_error(f"Error: {e}"))

    def mostrar_estadisticas(self):
        """Muestra estadÃ­sticas del repositorio."""
        stats = self.repositorio.obtener_estadisticas()

        print(f"\nðŸ“Š ESTADÃSTICAS DEL REPOSITORIO")
        print("="*50)
        print(f"ðŸ“ˆ Total de figuras: {stats['total_figuras']}")
        print(f"ðŸ·ï¸  Tipos Ãºnicos: {stats['tipos_unicos']}")
        print("\nðŸ”¢ Figuras por tipo:")

        for tipo, cantidad in stats['figuras_por_tipo'].items():
            print(f"   â€¢ {tipo.title()}: {cantidad}")

        if stats['total_figuras'] > 0:
            unidad_nombre = UnidadMedida.get_nombres_completos()[self.unidad_actual]
            print(f"\nðŸ“ MÃ©tricas en {unidad_nombre}:")

            print(f"   ðŸ”º Ãrea total 2D: {stats['area_total_2d']:.4f}")
            print(f"   ðŸ“¦ Volumen total 3D: {stats['volumen_total_3d']:.4f}")
            print(f"   ðŸ“ PerÃ­metro total 2D: {stats['perimetro_total_2d']:.4f}")

            print(f"\nâ­ Promedios:")
            if stats['area_promedio_2d'] > 0:
                print(f"   ðŸ”º Ãrea promedio 2D: {stats['area_promedio_2d']:.4f}")
            if stats['volumen_promedio_3d'] > 0:
                print(f"   ðŸ“¦ Volumen promedio 3D: {stats['volumen_promedio_3d']:.4f}")
            if stats['perimetro_promedio_2d'] > 0:
                print(f"   ðŸ“ PerÃ­metro promedio 2D: {stats['perimetro_promedio_2d']:.4f}")

    def guardar_figuras(self):
        """Guarda las figuras en un archivo."""
        try:
            if self.repositorio.contar_figuras() == 0:
                print(self.formateador.formatear_mensaje_info("No hay figuras para guardar."))
                return

            archivo = self.lector.leer_texto("Ingrese el nombre del archivo (o presione Enter para 'figuras.json'): ")
            if not archivo:
                archivo = "figuras.json"

            if not archivo.endswith('.json'):
                archivo += '.json'

            if self.repositorio.guardar_en_archivo(archivo):
                print(self.formateador.formatear_mensaje_exito(f"Figuras guardadas en '{archivo}' exitosamente."))
            else:
                print(self.formateador.formatear_mensaje_error(f"Error al guardar en '{archivo}'."))

        except KeyboardInterrupt:
            print(self.formateador.formatear_mensaje_advertencia("OperaciÃ³n cancelada"))
        except Exception as e:
            print(self.formateador.formatear_mensaje_error(f"Error: {e}"))

    def cargar_figuras(self):
        """Carga figuras desde un archivo."""
        try:
            archivo = self.lector.leer_texto("Ingrese el nombre del archivo (o presione Enter para 'figuras.json'): ")
            if not archivo:
                archivo = "figuras.json"

            if not archivo.endswith('.json'):
                archivo += '.json'

            if self.lector.leer_confirmacion(f"Â¿Desea reemplazar las figuras actuales? (s/N): "):
                self.repositorio.limpiar()
                mensaje_adicional = " (reemplazando las anteriores)"
            else:
                mensaje_adicional = " (agregando a las existentes)"

            figuras_cargadas = self.repositorio.cargar_desde_archivo(archivo)
            if figuras_cargadas > 0:
                print(self.formateador.formatear_mensaje_exito(
                    f"{figuras_cargadas} figuras cargadas desde '{archivo}'{mensaje_adicional}."
                ))
            else:
                print(self.formateador.formatear_mensaje_error(f"No se pudieron cargar figuras desde '{archivo}'."))

        except KeyboardInterrupt:
            print(self.formateador.formatear_mensaje_advertencia("OperaciÃ³n cancelada"))
        except Exception as e:
            print(self.formateador.formatear_mensaje_error(f"Error: {e}"))

    def limpiar_repositorio(self):
        """Limpia el repositorio despuÃ©s de confirmaciÃ³n."""
        try:
            total_figuras = self.repositorio.contar_figuras()
            if total_figuras == 0:
                print(self.formateador.formatear_mensaje_info("El repositorio ya estÃ¡ vacÃ­o."))
                return

            print(f"âš ï¸  Va a eliminar todas las figuras ({total_figuras} total)")

            if self.lector.leer_confirmacion("Â¿EstÃ¡ seguro? (s/N): "):
                self.repositorio.limpiar()
                print(self.formateador.formatear_mensaje_exito("Repositorio limpiado exitosamente."))
            else:
                print(self.formateador.formatear_mensaje_info("Limpieza cancelada."))

        except KeyboardInterrupt:
            print(self.formateador.formatear_mensaje_advertencia("OperaciÃ³n cancelada"))
        except Exception as e:
            print(self.formateador.formatear_mensaje_error(f"Error: {e}"))

    def mostrar_figura_detallada(self, figura):
        """
        Muestra informaciÃ³n detallada de una figura con formato mejorado.

        Args:
            figura: Objeto figura a mostrar
        """
        info_figura = self.formateador.formatear_info_figura(
            figura, self.unidad_actual, self.adapter
        )
        print(info_figura)

    def pausar(self):
        """Pausa la ejecuciÃ³n esperando entrada del usuario."""
        try:
            input("\nï¿½ Presione Enter para continuar...")
        except KeyboardInterrupt:
            pass

    def ejecutar(self):
        """Ejecuta el bucle principal del programa."""
        print(self.formateador.formatear_mensaje_exito("Â¡Bienvenido al Gestor de Figuras GeomÃ©tricas V2.0!"))
        print(self.formateador.formatear_mensaje_info("Sistema con soporte para IDs Ãºnicos, unidades y persistencia"))

        # Cargar figuras automÃ¡ticamente al iniciar si existe el archivo
        try:
            figuras_cargadas = self.repositorio.cargar_desde_archivo("figuras.json")
            if figuras_cargadas > 0:
                print(self.formateador.formatear_mensaje_info(f"Se cargaron {figuras_cargadas} figuras de la sesiÃ³n anterior."))
        except Exception:
            pass  # No mostrar error si no existe el archivo

        while True:
            try:
                self.mostrar_menu_principal()
                opcion = self.lector.leer_opcion_menu(f"Seleccione una opciÃ³n (1-11): ", 1, 11)

                if opcion == 1:
                    self.crear_figura()
                elif opcion == 2:
                    self.consultar_todas_figuras()
                elif opcion == 3:
                    self.consultar_figura_por_id()
                elif opcion == 4:
                    self.eliminar_figura()
                elif opcion == 5:
                    self.cambiar_unidad_medida()
                elif opcion == 6:
                    self.buscar_figuras_por_tipo()
                elif opcion == 7:
                    self.mostrar_estadisticas()
                elif opcion == 8:
                    self.guardar_figuras()
                elif opcion == 9:
                    self.cargar_figuras()
                elif opcion == 10:
                    self.limpiar_repositorio()
                elif opcion == 11:
                    # Guardar automÃ¡ticamente antes de salir si hay figuras
                    if self.repositorio.contar_figuras() > 0:
                        try:
                            self.repositorio.guardar_en_archivo("figuras.json")
                            print(self.formateador.formatear_mensaje_info("Figuras guardadas automÃ¡ticamente."))
                        except Exception:
                            pass
                    print(self.formateador.formatear_mensaje_info("Â¡Gracias por usar el Gestor de Figuras GeomÃ©tricas!"))
                    break

                if opcion != 11:
                    self.pausar()

            except KeyboardInterrupt:
                print(f"\n{self.formateador.formatear_mensaje_advertencia('Programa interrumpido por el usuario')}")
                # Guardar automÃ¡ticamente antes de salir por interrupciÃ³n
                if self.repositorio.contar_figuras() > 0:
                    try:
                        self.repositorio.guardar_en_archivo("figuras.json")
                        print(self.formateador.formatear_mensaje_info("Figuras guardadas automÃ¡ticamente."))
                    except Exception:
                        pass
                break
            except EOFError:
                print(f"\n{self.formateador.formatear_mensaje_info('Programa terminado')}")
                break
            except Exception as e:
                print(self.formateador.formatear_mensaje_error(f"Error inesperado: {e}"))
                self.pausar()
