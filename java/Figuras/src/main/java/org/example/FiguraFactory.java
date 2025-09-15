package org.example;

import java.util.Arrays;
import java.util.List;

/**
 * Factory para crear figuras geométricas.
 */
public class FiguraFactory {

    /**
     * Crea una figura según el tipo y dimensiones especificadas.
     * @param tipo el tipo de figura a crear
     * @param dimensiones las dimensiones necesarias para crear la figura
     * @return la figura creada
     * @throws IllegalArgumentException si el tipo no es reconocido o las dimensiones son inválidas
     */
    public static Figura crearFigura(String tipo, double[] dimensiones) {
        if (tipo == null || dimensiones == null) {
            throw new IllegalArgumentException("Tipo y dimensiones no pueden ser nulos");
        }

        GeneradorID generador = GeneradorID.getInstance();
        int id = generador.obtenerSiguienteId();

        switch (tipo.toLowerCase()) {
            case "circulo":
                if (dimensiones.length != 1) {
                    throw new IllegalArgumentException("Círculo requiere 1 dimensión (radio)");
                }
                return new Circulo(dimensiones[0], id);
            
            case "cuadrado":
                if (dimensiones.length != 1) {
                    throw new IllegalArgumentException("Cuadrado requiere 1 dimensión (lado)");
                }
                return new Cuadrado(dimensiones[0], id);
            
            case "cubo":
                if (dimensiones.length != 1) {
                    throw new IllegalArgumentException("Cubo requiere 1 dimensión (lado)");
                }
                return new Cubo(dimensiones[0], id);
            
            case "esfera":
                if (dimensiones.length != 1) {
                    throw new IllegalArgumentException("Esfera requiere 1 dimensión (radio)");
                }
                return new Esfera(dimensiones[0], id);
            
            default:
                throw new IllegalArgumentException("Tipo de figura no reconocido: " + tipo);
        }
    }

    /**
     * Retorna la lista de tipos de figuras disponibles.
     * @return lista con los tipos disponibles
     */
    public static List<String> tiposDisponibles() {
        return Arrays.asList("circulo", "cuadrado", "cubo", "esfera");
    }
}
