package org.example;

/**
 * Clase Circulo - Figura bidimensional
 */
public class Circulo extends Figura2d {
    
    private double radio;
    
    /**
     * Constructor de la clase Circulo
     * @param radio Radio del círculo
     * @param idFigura Identificador único de la figura
     * @throws IllegalArgumentException Si el radio es menor o igual a cero
     */
    public Circulo(double radio, int idFigura) {
        super("Círculo", idFigura);
        if (radio <= 0) {
            throw new IllegalArgumentException("El radio debe ser mayor que cero");
        }
        this.radio = radio;
    }
    
    /**
     * Calcula el área del círculo
     * @return El área del círculo
     */
    @Override
    public double calcularArea() {
        return Math.PI * this.radio * this.radio;
    }
    
    /**
     * Calcula el perímetro del círculo
     * @return El perímetro del círculo
     */
    @Override
    public double calcularPerimetro() {
        return 2 * Math.PI * this.radio;
    }
    
    /**
     * Obtiene el radio del círculo
     * @return El radio del círculo
     */
    public double getRadio() {
        return this.radio;
    }
    
    /**
     * Establece el radio del círculo
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
     * Representación en cadena del círculo
     * @return Representación del círculo
     */
    @Override
    public String toString() {
        return String.format("Círculo(id=%d, radio=%.2f)", getId(), radio);
    }
}