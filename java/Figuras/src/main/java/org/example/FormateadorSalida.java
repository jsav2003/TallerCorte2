package org.example;

import java.util.List;
import java.util.Map;

/**
 * Clase para formatear la salida de información.
 */
public class FormateadorSalida {

    /**
     * Formatea un menú con título, opciones e información adicional.
     * @param titulo el título del menú
     * @param opciones las opciones del menú
     * @param info información adicional a mostrar
     * @return cadena formateada del menú
     */
    public String formatearMenu(String titulo, String[] opciones, String info) {
        StringBuilder sb = new StringBuilder();
        
        sb.append("\n").append("=".repeat(50)).append("\n");
        sb.append("  ").append(titulo).append("\n");
        sb.append("=".repeat(50)).append("\n");
        
        if (info != null && !info.isEmpty()) {
            sb.append(info).append("\n");
            sb.append("-".repeat(30)).append("\n");
        }
        
        for (int i = 0; i < opciones.length; i++) {
            sb.append(String.format("%2d. %s%n", i + 1, opciones[i]));
        }
        
        sb.append("=".repeat(50)).append("\n");
        
        return sb.toString();
    }

    /**
     * Formatea la información de una figura con unidad especificada.
     * @param figura la figura a formatear
     * @param unidad la unidad para mostrar las medidas
     * @return cadena formateada de la figura
     */
    public String formatearFigura(Figura figura, UnidadMedida unidad) {
        if (figura == null) {
            return "Figura no encontrada";
        }

        UnidadAdapter adapter = new UnidadAdapter();
        StringBuilder sb = new StringBuilder();
        
        sb.append(String.format("ID: %d | Tipo: %s | Nombre: %s%n", 
                figura.getId(), figura.getTipo(), figura.getNombre()));
        
        if (figura instanceof Figura2d) {
            Figura2d fig2d = (Figura2d) figura;
            double area = fig2d.calcularArea();
            double perimetro = fig2d.calcularPerimetro();
            
            sb.append(String.format("  Área: %s²%n", 
                    adapter.formatearConUnidad(area, unidad)));
            sb.append(String.format("  Perímetro: %s%n", 
                    adapter.formatearConUnidad(perimetro, unidad)));
            
            if (figura instanceof Circulo) {
                Circulo circulo = (Circulo) figura;
                sb.append(String.format("  Radio: %s%n", 
                        adapter.formatearConUnidad(circulo.getRadio(), unidad)));
            } else if (figura instanceof Cuadrado) {
                Cuadrado cuadrado = (Cuadrado) figura;
                sb.append(String.format("  Lado: %s%n", 
                        adapter.formatearConUnidad(cuadrado.getLado(), unidad)));
            }
        }
        
        if (figura instanceof Figura3d) {
            Figura3d fig3d = (Figura3d) figura;
            double volumen = fig3d.calcularVolumen();
            
            sb.append(String.format("  Volumen: %s³%n", 
                    adapter.formatearConUnidad(volumen, unidad)));
            
            if (figura instanceof Cubo) {
                Cubo cubo = (Cubo) figura;
                double areaSuperficie = cubo.calcularAreaSuperficie();
                sb.append(String.format("  Lado: %s%n", 
                        adapter.formatearConUnidad(cubo.getLado(), unidad)));
                sb.append(String.format("  Área Superficie: %s²%n", 
                        adapter.formatearConUnidad(areaSuperficie, unidad)));
            } else if (figura instanceof Esfera) {
                Esfera esfera = (Esfera) figura;
                double areaSuperficie = esfera.calcularAreaSuperficie();
                sb.append(String.format("  Radio: %s%n", 
                        adapter.formatearConUnidad(esfera.getRadio(), unidad)));
                sb.append(String.format("  Área Superficie: %s²%n", 
                        adapter.formatearConUnidad(areaSuperficie, unidad)));
            }
        }
        
        return sb.toString();
    }

    /**
     * Formatea una lista de figuras.
     * @param figuras lista de figuras a formatear
     * @param unidad unidad para mostrar las medidas
     * @return cadena formateada de la lista
     */
    public String formatearListaFiguras(List<Figura> figuras, UnidadMedida unidad) {
        if (figuras == null || figuras.isEmpty()) {
            return "No hay figuras para mostrar.";
        }

        StringBuilder sb = new StringBuilder();
        sb.append(String.format("Total de figuras: %d%n", figuras.size()));
        sb.append("-".repeat(60)).append("\n");
        
        for (Figura figura : figuras) {
            sb.append(formatearFigura(figura, unidad));
            sb.append("-".repeat(60)).append("\n");
        }
        
        return sb.toString();
    }

    /**
     * Formatea estadísticas del sistema.
     * @param estadisticas mapa con las estadísticas
     * @return cadena formateada de las estadísticas
     */
    public String formatearEstadisticas(Map<String, Object> estadisticas) {
        StringBuilder sb = new StringBuilder();
        
        sb.append("\n").append("=".repeat(40)).append("\n");
        sb.append("  ESTADÍSTICAS DEL SISTEMA").append("\n");
        sb.append("=".repeat(40)).append("\n");
        
        estadisticas.forEach((key, value) -> 
            sb.append(String.format("%-20s: %s%n", key, value))
        );
        
        sb.append("=".repeat(40)).append("\n");
        
        return sb.toString();
    }
}
