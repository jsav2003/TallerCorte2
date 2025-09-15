package org.example;

/**
 * Generador de IDs únicos para figuras.
 * Implementa el patrón Singleton.
 */
public class GeneradorID {
    
    private static GeneradorID instance;
    private int contadorId;

    /**
     * Constructor privado para el patrón Singleton.
     */
    private GeneradorID() {
        this.contadorId = 0;
    }

    /**
     * Obtiene la instancia única del generador.
     * @return la instancia del GeneradorID
     */
    public static synchronized GeneradorID getInstance() {
        if (instance == null) {
            instance = new GeneradorID();
        }
        return instance;
    }

    /**
     * Obtiene el siguiente ID disponible.
     * @return el siguiente ID único
     */
    public synchronized int obtenerSiguienteId() {
        return ++contadorId;
    }

    /**
     * Actualiza el contador si el ID proporcionado es mayor al actual.
     * @param id el ID a comparar
     */
    public synchronized void actualizarSiMayor(int id) {
        if (id > contadorId) {
            contadorId = id;
        }
    }

    /**
     * Resetea el contador de IDs.
     */
    public synchronized void resetear() {
        contadorId = 0;
    }
}
