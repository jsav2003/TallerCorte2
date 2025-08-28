package org.example;

/**
 * Clase para figuras geométricas 3D.
 * Hereda de la clase Figura.
 */
public abstract class Figura3d extends Figura {

    /**
     * Constructor de la clase Figura3d.
     * @param nombre el nombre de la figura 3D
     */
    public Figura3d(String nombre) {
        super(nombre, "3D");
    }

    /**
     * Método abstracto para calcular el volumen de la figura 3D.
     * Debe ser implementado por las clases hijas específicas.
     * @return el volumen de la figura
     */
    public abstract double calcularVolumen();
}