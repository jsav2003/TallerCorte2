package org.example;

import java.util.Arrays;
import java.util.List;

/**
 * Factory para crear figuras geométricas
 */
public class FiguraFactory {
    
    /**
     * Crea una figura según el tipo especificado
     * @param tipo Tipo de figura ('circulo', 'cuadrado', 'cubo', 'esfera')
     * @param dimensiones Dimensiones de la figura (puede ser un solo valor o array)
     * @return Instancia de la figura creada
     * @throws IllegalArgumentException Si el tipo de figura no es válido
     */
    public static Figura crearFigura(String tipo, double... dimensiones) {
        if (dimensiones.length == 0) {
            throw new IllegalArgumentException("Se requiere al menos una dimensión");
        }
        
        String tipoLower = tipo.toLowerCase();
        int idFigura = GeneradorID.obtenerSiguienteId();
        double dimension = dimensiones[0];
        
        switch (tipoLower) {
            case "circulo":
                return new Circulo(dimension, idFigura);
            case "cuadrado":
                return new Cuadrado(dimension, idFigura);
            case "cubo":
                return new Cubo(dimension, idFigura);
            case "esfera":
                return new Esfera(dimension, idFigura);
            default:
                throw new IllegalArgumentException("Tipo de figura no válido: " + tipo);
        }
    }
    
    /**
     * Sobrecarga para crear figura con lista de dimensiones
     * @param tipo Tipo de figura
     * @param dimensiones Lista de dimensiones
     * @return Figura creada
     */
    public static Figura crearFigura(String tipo, List<Double> dimensiones) {
        if (dimensiones.isEmpty()) {
            throw new IllegalArgumentException("Se requiere al menos una dimensión");
        }
        return crearFigura(tipo, dimensiones.get(0));
    }
    
    /**
     * Retorna una lista de los tipos de figuras disponibles
     * @return Lista de tipos de figuras disponibles
     */
    public static List<String> tiposDisponibles() {
        return Arrays.asList("circulo", "cuadrado", "cubo", "esfera");
    }
}