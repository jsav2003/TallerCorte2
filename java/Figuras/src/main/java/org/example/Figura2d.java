package org.example;

/**
 * Clase para figuras geométricas 2D.
 * Hereda de la clase Figura.
 */
public abstract class Figura2d extends Figura {

    /**
     * Constructor de la clase Figura2d.
     * @param nombre el nombre de la figura 2D
     */
    public Figura2d(String nombre) {
        super(nombre, "2D");
    }

    /**
     * Método abstracto para calcular el área de la figura 2D.
     * Debe ser implementado por las clases hijas específicas.
     * @return el área de la figura
     */
    public abstract double calcularArea();

    /**
     * Método abstracto para calcular el perímetro de la figura 2D.
     * Debe ser implementado por las clases hijas específicas.
     * @return el perímetro de la figura
     */
    public abstract double calcularPerimetro();
}