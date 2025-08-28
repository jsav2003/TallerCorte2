package org.example;

/**
 * Clase para representar una esfera.
 * Hereda de la clase Figura3D.
 */
public class Esfera extends Figura3d {

    private final double radio;

    /**
     * Constructor de la clase Esfera.
     * @param radio el radio de la esfera
     */
    public Esfera(double radio) {
        super("Esfera");
        this.radio = radio;
    }

    /**
     * Calcula el volumen de la esfera.
     * @return el volumen de la esfera
     */
    @Override
    public double calcularVolumen() {
        return (4.0 / 3.0) * Math.PI * radio * radio * radio;
    }
}