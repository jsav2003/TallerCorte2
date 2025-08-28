package org.example;

/**
 * Clase para representar un cubo.
 * Hereda de la clase Figura3d.
 */
public class Cubo extends Figura3d {

    private final double longitudLado;

    /**
     * Constructor de la clase Cubo.
     * @param longitudLado la longitud del lado del cubo
     */
    public Cubo(double longitudLado) {
        super("Cubo");
        this.longitudLado = longitudLado;
    }

    /**
     * Calcula el volumen del cubo.
     * @return el volumen del cubo
     */
    @Override
    public double calcularVolumen() {
        return longitudLado * longitudLado * longitudLado;
    }
}
