package org.example;

/**
 * Clase Cuadrado - Figura bidimensional
 */
public class Cuadrado extends Figura2d {
    
    private double lado;
    
    /**
     * Constructor de la clase Cuadrado
     * @param lado Longitud del lado del cuadrado
     * @param idFigura Identificador único de la figura
     * @throws IllegalArgumentException Si el lado es menor o igual a cero
     */
    public Cuadrado(double lado, int idFigura) {
        super("Cuadrado", idFigura);
        if (lado <= 0) {
            throw new IllegalArgumentException("El lado debe ser mayor que cero");
        }
        this.lado = lado;
    }
    
    /**
     * Calcula el área del cuadrado
     * @return El área del cuadrado
     */
    @Override
    public double calcularArea() {
        return this.lado * this.lado;
    }
    
    /**
     * Calcula el perímetro del cuadrado
     * @return El perímetro del cuadrado
     */
    @Override
    public double calcularPerimetro() {
        return 4 * this.lado;
    }
    
    /**
     * Obtiene la longitud del lado del cuadrado
     * @return La longitud del lado
     */
    public double getLado() {
        return this.lado;
    }
    
    /**
     * Establece la longitud del lado del cuadrado
     * @param lado La nueva longitud del lado
     * @throws IllegalArgumentException Si el lado es menor o igual a cero
     */
    public void setLado(double lado) {
        if (lado <= 0) {
            throw new IllegalArgumentException("El lado debe ser mayor que cero");
        }
        this.lado = lado;
    }
    
    /**
     * Representación en cadena del cuadrado
     * @return Representación del cuadrado
     */
    @Override
    public String toString() {
        return String.format("Cuadrado(id=%d, lado=%.2f)", getId(), lado);
    }
}