package org.example;

/**
 * Clase Esfera - Figura tridimensional
 */
public class Esfera extends Figura3d {
    
    private double radio;
    
    /**
     * Constructor de la clase Esfera
     * @param radio Radio de la esfera
     * @param idFigura Identificador único de la figura
     */
    public Esfera(double radio, int idFigura) {
        super("Esfera", idFigura);
        this.radio = radio;
    }
    
    /**
     * Calcula el volumen de la esfera
     * @return El volumen de la esfera
     */
    @Override
    public double calcularVolumen() {
        return (4.0/3.0) * Math.PI * (this.radio * this.radio * this.radio);
    }
    
    /**
     * Calcula el área de superficie de la esfera
     * @return El área de superficie de la esfera
     */
    public double calcularAreaSuperficie() {
        return 4 * Math.PI * (this.radio * this.radio);
    }
    
    /**
     * Obtiene el radio de la esfera
     * @return El radio de la esfera
     */
    public double getRadio() {
        return this.radio;
    }
    
    /**
     * Establece el radio de la esfera
     * @param radio El nuevo radio
     * @throws IllegalArgumentException Si el radio es menor o igual a cero
     */
    public void setRadio(double radio) {
        if (radio <= 0) {
            throw new IllegalArgumentException("El radio debe ser mayor que cero");
        }
        this.radio = radio;
    }
    
    /**
     * Representación en cadena de la esfera
     * @return Representación de la esfera
     */
    @Override
    public String toString() {
        return String.format("Esfera(id=%d, radio=%.2f)", getId(), radio);
    }
}