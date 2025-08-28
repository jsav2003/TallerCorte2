package org.example;

/**
 * Clase para representar un círculo.
 * Hereda de la clase Figura2D.
 */
public class Circulo extends Figura2d {

    private final double radio;

    /**
     * Constructor de la clase Círculo.
     * @param radio el radio del círculo
     */
    public Circulo(double radio) {
        super("Circulo");
        this.radio = radio;
    }

    /**
     * Calcula el área del círculo.
     * @return el área del círculo
     */
    @Override
    public double calcularArea() {
        return Math.PI * radio * radio;
    }

    /**
     * Calcula el perímetro del círculo.
     * @return el perímetro del círculo
     */
    @Override
    public double calcularPerimetro() {
        return 2 * Math.PI * radio;
    }
}