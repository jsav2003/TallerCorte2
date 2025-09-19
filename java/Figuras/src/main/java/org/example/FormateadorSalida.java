package org.example;

import java.util.List;
import java.util.Map;

/**
 * Clase para formatear la salida hacia el usuario
 */
public class FormateadorSalida {
    
    /**
     * Formatea un menú para mostrar al usuario
     * @param titulo Título del menú
     * @param opciones Lista de opciones del menú
     * @param info Información adicional (opcional)
     * @return Menú formateado
     */
    public static String formatearMenu(String titulo, List<String> opciones, String info) {
        StringBuilder resultado = new StringBuilder();
        String lineaSeparadora = "=".repeat(50);
        
        resultado.append(lineaSeparadora).append("\n");
        resultado.append(String.format(" %s \n", centrarTexto(titulo, 48)));
        resultado.append(lineaSeparadora).append("\n");
        
        if (info != null && !info.isEmpty()) {
            resultado.append(info).append("\n");
            resultado.append("\n");
        }
        
        for (int i = 0; i < opciones.size(); i++) {
            resultado.append(String.format("%2d. %s\n", i + 1, opciones.get(i)));
        }
        
        resultado.append(lineaSeparadora);
        return resultado.toString();
    }
    
    /**
     * Formatea la información de una figura
     * @param figura Figura a formatear
     * @param unidad Unidad de medida a usar
     * @return Información formateada de la figura
     */
    public static String formatearFigura(Figura figura, UnidadMedida unidad) {
        StringBuilder resultado = new StringBuilder();
        
        resultado.append("📐 Figura ID: ").append(figura.getId()).append("\n");
        resultado.append("   Tipo: ").append(figura.getNombre()).append("\n");
        resultado.append("   Categoría: ").append(figura.getTipo()).append("\n");
        
        // Mostrar dimensiones específicas
        if (figura instanceof Circulo) {
            Circulo circulo = (Circulo) figura;
            double radioConvertido = UnidadAdapter.convertir(circulo.getRadio(), UnidadMedida.METROS, unidad);
            resultado.append("   Radio: ").append(UnidadAdapter.formatearConUnidad(radioConvertido, unidad)).append("\n");
        } else if (figura instanceof Cuadrado) {
            Cuadrado cuadrado = (Cuadrado) figura;
            double ladoConvertido = UnidadAdapter.convertir(cuadrado.getLado(), UnidadMedida.METROS, unidad);
            resultado.append("   Lado: ").append(UnidadAdapter.formatearConUnidad(ladoConvertido, unidad)).append("\n");
        } else if (figura instanceof Cubo) {
            Cubo cubo = (Cubo) figura;
            double ladoConvertido = UnidadAdapter.convertir(cubo.getLado(), UnidadMedida.METROS, unidad);
            resultado.append("   Lado: ").append(UnidadAdapter.formatearConUnidad(ladoConvertido, unidad)).append("\n");
        } else if (figura instanceof Esfera) {
            Esfera esfera = (Esfera) figura;
            double radioConvertido = UnidadAdapter.convertir(esfera.getRadio(), UnidadMedida.METROS, unidad);
            resultado.append("   Radio: ").append(UnidadAdapter.formatearConUnidad(radioConvertido, unidad)).append("\n");
        }
        
        // Mostrar cálculos
        if (figura instanceof Figura2d) {
            Figura2d figura2d = (Figura2d) figura;
            double area = figura2d.calcularArea();
            double perimetro = figura2d.calcularPerimetro();
            
            // Convertir área (unidad²) y perímetro
            double factor = unidad.getFactorConversion();
            double areaConvertida = area / (factor * factor);
            double perimetroConvertido = UnidadAdapter.convertir(perimetro, UnidadMedida.METROS, unidad);
            
            resultado.append(String.format("   Área: %.2f %s²\n", areaConvertida, unidad.getSimbolo()));
            resultado.append("   Perímetro: ").append(UnidadAdapter.formatearConUnidad(perimetroConvertido, unidad)).append("\n");
            
        } else if (figura instanceof Figura3d) {
            Figura3d figura3d = (Figura3d) figura;
            double volumen = figura3d.calcularVolumen();
            
            // Convertir volumen (unidad³)
            double factor = unidad.getFactorConversion();
            double volumenConvertido = volumen / (factor * factor * factor);
            
            resultado.append(String.format("   Volumen: %.2f %s³\n", volumenConvertido, unidad.getSimbolo()));
            
            if (figura instanceof Cubo) {
                Cubo cubo = (Cubo) figura;
                double areaSuperficie = cubo.calcularAreaSuperficie();
                double areaConvertida = areaSuperficie / (factor * factor);
                resultado.append(String.format("   Área superficie: %.2f %s²\n", areaConvertida, unidad.getSimbolo()));
            } else if (figura instanceof Esfera) {
                Esfera esfera = (Esfera) figura;
                double areaSuperficie = esfera.calcularAreaSuperficie();
                double areaConvertida = areaSuperficie / (factor * factor);
                resultado.append(String.format("   Área superficie: %.2f %s²\n", areaConvertida, unidad.getSimbolo()));
            }
        }
        
        return resultado.toString();
    }
    
    /**
     * Formatea una lista de figuras
     * @param figuras Lista de figuras
     * @param unidad Unidad de medida a usar
     * @return Lista formateada de figuras
     */
    public static String formatearListaFiguras(List<Figura> figuras, UnidadMedida unidad) {
        if (figuras.isEmpty()) {
            return "No hay figuras para mostrar.";
        }
        
        StringBuilder resultado = new StringBuilder();
        resultado.append("Total de figuras: ").append(figuras.size()).append("\n");
        resultado.append("=".repeat(50)).append("\n");
        
        for (int i = 0; i < figuras.size(); i++) {
            resultado.append("\n").append(i + 1).append(". ").append(formatearFigura(figuras.get(i), unidad));
        }
        
        return resultado.toString();
    }
    
    /**
     * Formatea las estadísticas del repositorio
     * @param estadisticas Mapa con estadísticas
     * @return Estadísticas formateadas
     */
    public static String formatearEstadisticas(Map<String, Integer> estadisticas) {
        StringBuilder resultado = new StringBuilder();
        resultado.append("ESTADÍSTICAS DEL REPOSITORIO\n");
        resultado.append("=".repeat(40)).append("\n");
        resultado.append("Total de figuras: ").append(estadisticas.getOrDefault("total", 0)).append("\n");
        resultado.append("\n");
        resultado.append("Distribución por tipo:\n");
        
        String[] tipos = {"círculo", "cuadrado", "cubo", "esfera"};
        int total = estadisticas.getOrDefault("total", 0);
        
        for (String tipo : tipos) {
            int cantidad = estadisticas.getOrDefault(tipo, 0);
            if (cantidad > 0) {
                double porcentaje = total > 0 ? (cantidad * 100.0 / total) : 0.0;
                resultado.append(String.format(" • %s: %d (%.1f%%)\n", 
                    tipo.substring(0, 1).toUpperCase() + tipo.substring(1), cantidad, porcentaje));
            }
        }
        
        return resultado.toString();
    }
    
    /**
     * Formatea un mensaje de error
     * @param mensaje Mensaje de error
     * @return Mensaje de error formateado
     */
    public static String mostrarError(String mensaje) {
        return "Error: " + mensaje;
    }
    
    /**
     * Formatea un mensaje de éxito
     * @param mensaje Mensaje de éxito
     * @return Mensaje de éxito formateado
     */
    public static String mostrarExito(String mensaje) {
        return mensaje;
    }
    
    /**
     * Formatea un mensaje informativo
     * @param mensaje Mensaje informativo
     * @return Mensaje informativo formateado
     */
    public static String mostrarInfo(String mensaje) {
        return mensaje;
    }
    
    /**
     * Centra un texto en un ancho específico
     * @param texto Texto a centrar
     * @param ancho Ancho total
     * @return Texto centrado
     */
    private static String centrarTexto(String texto, int ancho) {
        if (texto.length() >= ancho) {
            return texto;
        }
        
        int espacios = (ancho - texto.length()) / 2;
        return " ".repeat(espacios) + texto + " ".repeat(ancho - texto.length() - espacios);
    }
}