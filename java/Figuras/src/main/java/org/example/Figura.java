package org.example;

/**
 * Clase base abstracta Figura
 */
public abstract class Figura {
    
    private String nombre;
    private String tipo;
    private int idFigura;
    
    /**
     * Constructor de la clase Figura
     * @param nombre Nombre de la figura
     * @param tipo Tipo de figura
     * @param idFigura Identificador único de la figura
     */
    public Figura(String nombre, String tipo, int idFigura) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.idFigura = idFigura;
    }
    
    /**
     * Obtiene el nombre de la figura
     * @return El nombre de la figura
     */
    public String getNombre() {
        return this.nombre;
    }
    
    /**
     * Obtiene el tipo de la figura
     * @return El tipo de la figura
     */
    public String getTipo() {
        return this.tipo;
    }
    
    /**
     * Obtiene el ID de la figura
     * @return El ID de la figura
     */
    public int getId() {
        return this.idFigura;
    }
    
    /**
     * Establece el nombre de la figura
     * @param nombre El nuevo nombre
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    /**
     * Establece el tipo de la figura
     * @param tipo El nuevo tipo
     */
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
}