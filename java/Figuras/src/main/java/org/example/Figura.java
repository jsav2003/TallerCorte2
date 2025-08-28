package org.example;

/**
 * Clase madre para figuras geométricas 2D y 3D.
 */
public class Figura {

    private String nombre;
    private String tipo;

    /**
     * Constructor de la clase Figura.
     * @param nombre el nombre de la figura
     * @param tipo el tipo de la figura
     */
    public Figura(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
    }

    /**
     * Retorna el nombre de la figura.
     * @return el nombre de la figura
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * Retorna el tipo de la figura.
     * @return el tipo de la figura
     */
    public String getTipo() {
        return tipo;
    }

    /**
     * Establece el nombre de la figura.
     * @param nombre el nuevo nombre de la figura
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    /**
     * Establece el tipo de la figura.
     * @param tipo el nuevo tipo de la figura
     */
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
}