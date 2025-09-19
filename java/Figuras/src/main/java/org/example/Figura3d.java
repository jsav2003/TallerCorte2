package org.example;

/**
 * Clase abstracta para figuras tridimensionales
 */
public abstract class Figura3d extends Figura {
    
    /**
     * Constructor de la clase Figura3d
     * @param nombre Nombre de la figura
     * @param idFigura Identificador único de la figura
     */
    public Figura3d(String nombre, int idFigura) {
        super(nombre, "3D", idFigura);
    }
    
    /**
     * Calcula el volumen de la figura 3D
     * @return El volumen de la figura
     */
    public abstract double calcularVolumen();
}