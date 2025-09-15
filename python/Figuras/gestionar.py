"""
Clase principal para gestionar el sistema de figuras geométricas
"""
from .RepositorioFiguras import RepositorioFiguras
from .UnidadAdapter import UnidadAdapter
from .UnidadMedida import UnidadMedida
from .LectorEntrada import LectorEntrada
from .FormateadorSalida import FormateadorSalida
from .FiguraFactory import FiguraFactory


class Gestionar:
    """Clase principal para gestionar el sistema de figuras geométricas"""
    
    def __init__(self):
        """Constructor de la clase Gestionar"""
        import os
        # Construir la ruta al archivo figuras.json en el directorio del módulo
        directorio_actual = os.path.dirname(__file__)
        archivo_figuras = os.path.join(directorio_actual, "figuras.json")
        self._repositorio = RepositorioFiguras(archivo_figuras, True)
        self._adapter = UnidadAdapter()
        self._unidad_actual = UnidadMedida.METROS
        self._lector = LectorEntrada()
        self._formateador = FormateadorSalida()
    
    def ejecutar(self) -> None:
        """Ejecuta el bucle principal de la aplicación"""
        print(self._formateador.mostrar_info("Bienvenido al Sistema de Figuras Geométricas"))
        print(self._formateador.mostrar_info(f"Unidad actual: {self._unidad_actual.get_simbolo()}"))
        
        while True:
            try:
                self.mostrar_menu_principal()
                opcion = self._lector.leer_entero("\nSeleccione una opción: ", 1, 8)
                self.procesar_opcion(opcion)
                
                if opcion == 8:  # Salir
                    break
                    
                input("\nPresione Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n" + self._formateador.mostrar_info("Saliendo del programa..."))
                break
            except Exception as e:
                print(self._formateador.mostrar_error(f"Error inesperado: {e}"))
    
    def mostrar_menu_principal(self) -> None:
        """Muestra el menú principal de opciones"""
        opciones = [
            "Crear nueva figura",
            "Consultar todas las figuras",
            "Consultar figura por ID",
            "Eliminar figura",
            "Ver estadísticas",
            "Cambiar unidad de medida",
            "Limpiar repositorio",
            "Salir"
        ]
        
        estadisticas = self._repositorio.obtener_estadisticas()
        info = f"Figuras almacenadas: {estadisticas['total']} | Unidad: {self._unidad_actual.get_simbolo()}"
        
        menu = self._formateador.formatear_menu("SISTEMA DE FIGURAS GEOMÉTRICAS", opciones, info)
        print(menu)
    
    def procesar_opcion(self, opcion: int) -> None:
        """
        Procesa la opción seleccionada por el usuario
        
        Args:
            opcion (int): Número de opción seleccionada
        """
        if opcion == 1:
            self.crear_figura()
        elif opcion == 2:
            self.consultar_todas_figuras()
        elif opcion == 3:
            self.consultar_figura_por_id()
        elif opcion == 4:
            self.eliminar_figura()
        elif opcion == 5:
            self.mostrar_estadisticas()
        elif opcion == 6:
            self.cambiar_unidad_medida()
        elif opcion == 7:
            self.limpiar_repositorio()
        elif opcion == 8:
            print(self._formateador.mostrar_info("¡Gracias por usar el sistema!"))
    
    def crear_figura(self) -> None:
        """Crea una nueva figura geométrica"""
        print("\n" + "="*50)
        print(" CREAR NUEVA FIGURA")
        print("="*50)
        
        tipos_disponibles = FiguraFactory.tipos_disponibles()
        tipos_mostrar = [tipo.capitalize() for tipo in tipos_disponibles]
        
        print("\nTipos de figuras disponibles:")
        indice = self._lector.seleccionar_opcion("", tipos_mostrar)
        tipo_seleccionado = tipos_disponibles[indice]
        
        try:
            if tipo_seleccionado in ["circulo", "esfera"]:
                radio = self._lector.leer_flotante(f"\nIngrese el radio del {tipo_seleccionado} (en {self._unidad_actual.get_simbolo()}): ", 0.001)
                # Convertir a metros para almacenamiento interno
                radio_metros = UnidadAdapter.convertir(radio, self._unidad_actual, UnidadMedida.METROS)
                figura = FiguraFactory.crear_figura(tipo_seleccionado, radio_metros)
            
            elif tipo_seleccionado in ["cuadrado", "cubo"]:
                lado = self._lector.leer_flotante(f"\nIngrese el lado del {tipo_seleccionado} (en {self._unidad_actual.get_simbolo()}): ", 0.001)
                # Convertir a metros para almacenamiento interno
                lado_metros = UnidadAdapter.convertir(lado, self._unidad_actual, UnidadMedida.METROS)
                figura = FiguraFactory.crear_figura(tipo_seleccionado, lado_metros)
            
            else:
                raise ValueError(f"Tipo de figura no soportado: {tipo_seleccionado}")
            
            id_figura = self._repositorio.almacenar_figura(figura)
            print(self._formateador.mostrar_exito(f"Figura creada exitosamente con ID: {id_figura}"))
            
            # Mostrar información de la figura creada
            print("\n" + self._formateador.formatear_figura(figura, self._unidad_actual))
            
        except Exception as e:
            print(self._formateador.mostrar_error(f"Error al crear la figura: {e}"))
    
    def consultar_todas_figuras(self) -> None:
        """Consulta y muestra todas las figuras almacenadas"""
        print("\n" + "="*50)
        print(" TODAS LAS FIGURAS")
        print("="*50)
        
        figuras = self._repositorio.obtener_todas_figuras()
        resultado = self._formateador.formatear_lista_figuras(figuras, self._unidad_actual)
        print(resultado)
    
    def consultar_figura_por_id(self) -> None:
        """Consulta una figura específica por su ID"""
        print("\n" + "="*50)
        print(" CONSULTAR FIGURA POR ID")
        print("="*50)
        
        id_figura = self._lector.leer_entero("Ingrese el ID de la figura: ", 1)
        figura = self._repositorio.obtener_figura(id_figura)
        
        if figura:
            print("\n" + self._formateador.formatear_figura(figura, self._unidad_actual))
        else:
            print(self._formateador.mostrar_error(f"No se encontró una figura con ID: {id_figura}"))
    
    def eliminar_figura(self) -> None:
        """Elimina una figura del repositorio"""
        print("\n" + "="*50)
        print(" ELIMINAR FIGURA")
        print("="*50)
        
        # Mostrar figuras disponibles
        figuras = self._repositorio.obtener_todas_figuras()
        if not figuras:
            print(self._formateador.mostrar_info("No hay figuras para eliminar."))
            return
        
        print(self._formateador.formatear_lista_figuras(figuras, self._unidad_actual))
        
        id_figura = self._lector.leer_entero("\nIngrese el ID de la figura a eliminar: ", 1)
        figura = self._repositorio.obtener_figura(id_figura)
        
        if not figura:
            print(self._formateador.mostrar_error(f"No se encontró una figura con ID: {id_figura}"))
            return
        
        # Mostrar información de la figura a eliminar
        print("\nFigura a eliminar:")
        print(self._formateador.formatear_figura(figura, self._unidad_actual))
        
        # Confirmar eliminación
        if self._lector.confirmar_accion("¿Está seguro de que desea eliminar esta figura?"):
            if self._repositorio.eliminar_figura(id_figura):
                print(self._formateador.mostrar_exito("Figura eliminada exitosamente."))
            else:
                print(self._formateador.mostrar_error("Error al eliminar la figura."))
        else:
            print(self._formateador.mostrar_info("Eliminación cancelada."))
    
    def mostrar_estadisticas(self) -> None:
        """Muestra las estadísticas del repositorio"""
        print("\n" + "="*50)
        print(" ESTADÍSTICAS")
        print("="*50)
        
        estadisticas = self._repositorio.obtener_estadisticas()
        resultado = self._formateador.formatear_estadisticas(estadisticas)
        print(resultado)
    
    def cambiar_unidad_medida(self) -> None:
        """Permite cambiar la unidad de medida actual"""
        print("\n" + "="*50)
        print(" CAMBIAR UNIDAD DE MEDIDA")
        print("="*50)
        
        unidades_disponibles = self._adapter.obtener_unidades_disponibles()
        nombres_unidades = [f"{unidad.get_simbolo()} - {unidad.get_nombres_completos()[unidad.get_simbolo()]}" 
                           for unidad in unidades_disponibles]
        
        print(f"Unidad actual: {self._unidad_actual.get_simbolo()}")
        print("\nUnidades disponibles:")
        indice = self._lector.seleccionar_opcion("", nombres_unidades)
        
        nueva_unidad = unidades_disponibles[indice]
        if nueva_unidad != self._unidad_actual:
            self._unidad_actual = nueva_unidad
            print(self._formateador.mostrar_exito(f"Unidad cambiada a: {self._unidad_actual.get_simbolo()}"))
        else:
            print(self._formateador.mostrar_info("Ya está usando esa unidad."))
    
    def limpiar_repositorio(self) -> None:
        """Limpia todas las figuras del repositorio"""
        print("\n" + "="*50)
        print(" LIMPIAR REPOSITORIO")
        print("="*50)
        
        estadisticas = self._repositorio.obtener_estadisticas()
        if estadisticas['total'] == 0:
            print(self._formateador.mostrar_info("El repositorio ya está vacío."))
            return
        
        print(f"Se eliminarán {estadisticas['total']} figuras del repositorio.")
        
        if self._lector.confirmar_accion("¿Está seguro de que desea eliminar todas las figuras?"):
            self._repositorio.limpiar_repositorio()
            print(self._formateador.mostrar_exito("Repositorio limpiado exitosamente."))
        else:
            print(self._formateador.mostrar_info("Operación cancelada."))