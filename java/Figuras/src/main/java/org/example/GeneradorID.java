package org.example;

/**
 * Generador de IDs únicos para las figuras
 */
public class GeneradorID {
    
    private static int contadorId = 0;
    
    /**
     * Obtiene el siguiente ID disponible
     * @return Siguiente ID único
     */
    public static synchronized int obtenerSiguienteId() {
        return ++contadorId;
    }
    
    /**
     * Actualiza el contador si el ID proporcionado es mayor
     * @param idFigura ID a comparar con el contador actual
     */
    public static synchronized void actualizarSiMayor(int idFigura) {
        if (idFigura > contadorId) {
            contadorId = idFigura;
        }
    }
    
    /**
     * Resetea el contador de IDs a cero
     */
    public static synchronized void resetear() {
        contadorId = 0;
    }
    
    /**
     * Obtiene el valor actual del contador sin incrementarlo
     * @return Valor actual del contador
     */
    public static synchronized int obtenerContadorActual() {
        return contadorId;
    }
}