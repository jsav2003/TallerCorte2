package org.example;

/**
 * Clase para representar un cuadrado.
 * Hereda de la clase Figura2D.
 */
public class Cuadrado extends Figura2d {

    private final double longitudLado;

    /**
     * Constructor de la clase Cuadrado.
     * @param longitudLado la longitud del lado del cuadrado
     */
    public Cuadrado(double longitudLado) {
        super("Cuadrado");
        this.longitudLado = longitudLado;
    }

    /**
     * Calcula el área del cuadrado.
     * @return el área del cuadrado
     */
    @Override
    public double calcularArea() {
        return longitudLado * longitudLado;
    }

    /**
     * Calcula el perímetro del cuadrado.
     * @return el perímetro del cuadrado
     */
    @Override
    public double calcularPerimetro() {
        return 4 * longitudLado;
    }
}