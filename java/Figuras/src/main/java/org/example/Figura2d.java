package org.example;

/**
 * Clase abstracta para figuras bidimensionales
 */
public abstract class Figura2d extends Figura {
    
    /**
     * Constructor de la clase Figura2d
     * @param nombre Nombre de la figura
     * @param idFigura Identificador único de la figura
     */
    public Figura2d(String nombre, int idFigura) {
        super(nombre, "2D", idFigura);
    }
    
    /**
     * Calcula el área de la figura 2D
     * @return El área de la figura
     */
    public abstract double calcularArea();
    
    /**
     * Calcula el perímetro de la figura 2D
     * @return El perímetro de la figura
     */
    public abstract double calcularPerimetro();
}