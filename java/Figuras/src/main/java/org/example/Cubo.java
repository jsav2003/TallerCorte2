package org.example;

/**
 * Clase Cubo - Figura tridimensional
 */
public class Cubo extends Figura3d {
    
    private double lado;
    
    /**
     * Constructor de la clase Cubo
     * @param lado Longitud del lado del cubo
     * @param idFigura Identificador único de la figura
     */
    public Cubo(double lado, int idFigura) {
        super("Cubo", idFigura);
        this.lado = lado;
    }
    
    /**
     * Calcula el volumen del cubo
     * @return El volumen del cubo
     */
    @Override
    public double calcularVolumen() {
        return this.lado * this.lado * this.lado;
    }
    
    /**
     * Calcula el área de superficie del cubo
     * @return El área de superficie del cubo
     */
    public double calcularAreaSuperficie() {
        return 6 * (this.lado * this.lado);
    }
    
    /**
     * Obtiene la longitud del lado del cubo
     * @return La longitud del lado
     */
    public double getLado() {
        return this.lado;
    }
    
    /**
     * Establece la longitud del lado del cubo
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
     * Representación en cadena del cubo
     * @return Representación del cubo
     */
    @Override
    public String toString() {
        return String.format("Cubo(id=%d, lado=%.2f)", getId(), lado);
    }
}
