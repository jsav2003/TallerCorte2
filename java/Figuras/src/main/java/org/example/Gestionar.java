package org.example;

import java.io.File;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

/**
 * Clase principal para gestionar el sistema de figuras geométricas
 */
public class Gestionar {
    
    private final RepositorioFiguras repositorio;
    private UnidadMedida unidadActual;
    
    /**
     * Constructor de la clase Gestionar
     */
    public Gestionar() {
        // Construir la ruta al archivo figuras.json en el directorio actual
        String directorioActual = System.getProperty("user.dir");
        String archivoFiguras = directorioActual + File.separator + "figuras.json";
        
        this.repositorio = new RepositorioFiguras(archivoFiguras, true);
        this.unidadActual = UnidadMedida.METROS;
    }
    
    /**
     * Ejecuta el bucle principal de la aplicación
     */
    public void ejecutar() {
        System.out.println(FormateadorSalida.mostrarInfo("Bienvenido al Sistema de Figuras Geométricas"));
        System.out.println(FormateadorSalida.mostrarInfo("Unidad actual: " + unidadActual.getSimbolo()));
        
        while (true) {
            try {
                mostrarMenuPrincipal();
                int opcion = LectorEntrada.leerEntero("\nSeleccione una opción: ", 1, 8);
                procesarOpcion(opcion);
                
                if (opcion == 8) { // Salir
                    break;
                }
                
                System.out.println("\nPresione Enter para continuar...");
                System.in.read();
                
            } catch (Exception e) {
                if (e instanceof InterruptedException || e.getMessage().contains("interrupted")) {
                    System.out.println("\n" + FormateadorSalida.mostrarInfo("Saliendo del programa..."));
                    break;
                } else {
                    System.out.println(FormateadorSalida.mostrarError("Error inesperado: " + e.getMessage()));
                }
            }
        }
    }
    
    /**
     * Muestra el menú principal de opciones
     */
    private void mostrarMenuPrincipal() {
        List<String> opciones = Arrays.asList(
            "Crear nueva figura",
            "Consultar todas las figuras", 
            "Consultar figura por ID",
            "Eliminar figura",
            "Ver estadísticas",
            "Cambiar unidad de medida",
            "Limpiar repositorio",
            "Salir"
        );
        
        Map<String, Integer> estadisticas = repositorio.obtenerEstadisticas();
        String info = String.format("Figuras almacenadas: %d | Unidad: %s", 
                                   estadisticas.get("total"), unidadActual.getSimbolo());
        
        String menu = FormateadorSalida.formatearMenu("SISTEMA DE FIGURAS GEOMÉTRICAS", opciones, info);
        System.out.println(menu);
    }
    
    /**
     * Procesa la opción seleccionada por el usuario
     * @param opcion Número de opción seleccionada
     */
    private void procesarOpcion(int opcion) {
        switch (opcion) {
            case 1:
                crearFigura();
                break;
            case 2:
                consultarTodasFiguras();
                break;
            case 3:
                consultarFiguraPorId();
                break;
            case 4:
                eliminarFigura();
                break;
            case 5:
                mostrarEstadisticas();
                break;
            case 6:
                cambiarUnidadMedida();
                break;
            case 7:
                limpiarRepositorio();
                break;
            case 8:
                System.out.println(FormateadorSalida.mostrarInfo("¡Gracias por usar el sistema!"));
                break;
        }
    }
    
    /**
     * Crea una nueva figura geométrica
     */
    private void crearFigura() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println(" CREAR NUEVA FIGURA");
        System.out.println("=".repeat(50));
        
        List<String> tiposDisponibles = FiguraFactory.tiposDisponibles();
        List<String> tiposMostrar = tiposDisponibles.stream()
                .map(tipo -> tipo.substring(0, 1).toUpperCase() + tipo.substring(1))
                .collect(java.util.stream.Collectors.toList());
        
        System.out.println("\nTipos de figuras disponibles:");
        int indice = LectorEntrada.seleccionarOpcion("", tiposMostrar);
        String tipoSeleccionado = tiposDisponibles.get(indice);
        
        try {
            Figura figura;
            if (tipoSeleccionado.equals("circulo") || tipoSeleccionado.equals("esfera")) {
                double radio = LectorEntrada.leerFlotante(
                    String.format("\nIngrese el radio del %s (en %s): ", tipoSeleccionado, unidadActual.getSimbolo()), 
                    0.001);
                
                // Convertir a metros para almacenamiento interno
                double radioMetros = UnidadAdapter.convertir(radio, unidadActual, UnidadMedida.METROS);
                figura = FiguraFactory.crearFigura(tipoSeleccionado, radioMetros);
                
            } else if (tipoSeleccionado.equals("cuadrado") || tipoSeleccionado.equals("cubo")) {
                double lado = LectorEntrada.leerFlotante(
                    String.format("\nIngrese el lado del %s (en %s): ", tipoSeleccionado, unidadActual.getSimbolo()), 
                    0.001);
                
                // Convertir a metros para almacenamiento interno
                double ladoMetros = UnidadAdapter.convertir(lado, unidadActual, UnidadMedida.METROS);
                figura = FiguraFactory.crearFigura(tipoSeleccionado, ladoMetros);
                
            } else {
                throw new IllegalArgumentException("Tipo de figura no soportado: " + tipoSeleccionado);
            }
            
            int idFigura = repositorio.almacenarFigura(figura);
            System.out.println(FormateadorSalida.mostrarExito("Figura creada exitosamente con ID: " + idFigura));
            
            // Mostrar información de la figura creada
            System.out.println("\n" + FormateadorSalida.formatearFigura(figura, unidadActual));
            
        } catch (Exception e) {
            System.out.println(FormateadorSalida.mostrarError("Error al crear la figura: " + e.getMessage()));
        }
    }
    
    /**
     * Consulta y muestra todas las figuras almacenadas
     */
    private void consultarTodasFiguras() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println(" TODAS LAS FIGURAS");
        System.out.println("=".repeat(50));
        
        List<Figura> figuras = repositorio.obtenerTodasFiguras();
        String resultado = FormateadorSalida.formatearListaFiguras(figuras, unidadActual);
        System.out.println(resultado);
    }
    
    /**
     * Consulta una figura específica por su ID
     */
    private void consultarFiguraPorId() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println(" CONSULTAR FIGURA POR ID");
        System.out.println("=".repeat(50));
        
        int idFigura = LectorEntrada.leerEntero("Ingrese el ID de la figura: ", 1, null);
        Figura figura = repositorio.obtenerFigura(idFigura);
        
        if (figura != null) {
            System.out.println("\n" + FormateadorSalida.formatearFigura(figura, unidadActual));
        } else {
            System.out.println(FormateadorSalida.mostrarError("No se encontró una figura con ID: " + idFigura));
        }
    }
    
    /**
     * Elimina una figura del repositorio
     */
    private void eliminarFigura() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println(" ELIMINAR FIGURA");
        System.out.println("=".repeat(50));
        
        // Mostrar figuras disponibles
        List<Figura> figuras = repositorio.obtenerTodasFiguras();
        if (figuras.isEmpty()) {
            System.out.println(FormateadorSalida.mostrarInfo("No hay figuras para eliminar."));
            return;
        }
        
        System.out.println(FormateadorSalida.formatearListaFiguras(figuras, unidadActual));
        
        int idFigura = LectorEntrada.leerEntero("\nIngrese el ID de la figura a eliminar: ", 1, null);
        Figura figura = repositorio.obtenerFigura(idFigura);
        
        if (figura == null) {
            System.out.println(FormateadorSalida.mostrarError("No se encontró una figura con ID: " + idFigura));
            return;
        }
        
        // Mostrar información de la figura a eliminar
        System.out.println("\nFigura a eliminar:");
        System.out.println(FormateadorSalida.formatearFigura(figura, unidadActual));
        
        // Confirmar eliminación
        if (LectorEntrada.confirmarAccion("¿Está seguro de que desea eliminar esta figura?")) {
            if (repositorio.eliminarFigura(idFigura)) {
                System.out.println(FormateadorSalida.mostrarExito("Figura eliminada exitosamente."));
            } else {
                System.out.println(FormateadorSalida.mostrarError("Error al eliminar la figura."));
            }
        } else {
            System.out.println(FormateadorSalida.mostrarInfo("Eliminación cancelada."));
        }
    }
    
    /**
     * Muestra las estadísticas del repositorio
     */
    private void mostrarEstadisticas() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println(" ESTADÍSTICAS");
        System.out.println("=".repeat(50));
        
        Map<String, Integer> estadisticas = repositorio.obtenerEstadisticas();
        String resultado = FormateadorSalida.formatearEstadisticas(estadisticas);
        System.out.println(resultado);
    }
    
    /**
     * Permite cambiar la unidad de medida actual
     */
    private void cambiarUnidadMedida() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println(" CAMBIAR UNIDAD DE MEDIDA");
        System.out.println("=".repeat(50));
        
        List<UnidadMedida> unidadesDisponibles = UnidadAdapter.obtenerUnidadesDisponibles();
        Map<String, String> nombresCompletos = UnidadMedida.getNombresCompletos();
        
        List<String> nombresUnidades = unidadesDisponibles.stream()
                .map(unidad -> unidad.getSimbolo() + " - " + nombresCompletos.get(unidad.getSimbolo()))
                .collect(java.util.stream.Collectors.toList());
        
        System.out.println("Unidad actual: " + unidadActual.getSimbolo());
        System.out.println("\nUnidades disponibles:");
        
        int indice = LectorEntrada.seleccionarOpcion("", nombresUnidades);
        UnidadMedida nuevaUnidad = unidadesDisponibles.get(indice);
        
        if (nuevaUnidad != unidadActual) {
            unidadActual = nuevaUnidad;
            System.out.println(FormateadorSalida.mostrarExito("Unidad cambiada a: " + unidadActual.getSimbolo()));
        } else {
            System.out.println(FormateadorSalida.mostrarInfo("Ya está usando esa unidad."));
        }
    }
    
    /**
     * Limpia todas las figuras del repositorio
     */
    private void limpiarRepositorio() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println(" LIMPIAR REPOSITORIO");
        System.out.println("=".repeat(50));
        
        Map<String, Integer> estadisticas = repositorio.obtenerEstadisticas();
        int total = estadisticas.get("total");
        
        if (total == 0) {
            System.out.println(FormateadorSalida.mostrarInfo("El repositorio ya está vacío."));
            return;
        }
        
        System.out.println("Se eliminarán " + total + " figuras del repositorio.");
        
        if (LectorEntrada.confirmarAccion("¿Está seguro de que desea eliminar todas las figuras?")) {
            repositorio.limpiarRepositorio();
            System.out.println(FormateadorSalida.mostrarExito("Repositorio limpiado exitosamente."));
        } else {
            System.out.println(FormateadorSalida.mostrarInfo("Operación cancelada."));
        }
    }
}