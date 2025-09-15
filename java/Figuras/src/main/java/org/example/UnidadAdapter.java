package org.example;

/**
 * Adaptador para conversión entre unidades de medida.
 */
public class UnidadAdapter {

    /**
     * Convierte un valor de una unidad a otra.
     * @param valor el valor a convertir
     * @param desde la unidad de origen
     * @param hacia la unidad de destino
     * @return el valor convertido
     */
    public double convertir(double valor, UnidadMedida desde, UnidadMedida hacia) {
        if (desde == hacia) {
            return valor;
        }
        
        // Convertir a metros primero, luego a la unidad destino
        double valorEnMetros = valor * desde.getFactorConversion();
        return valorEnMetros / hacia.getFactorConversion();
    }

    /**
     * Formatea un valor con su unidad correspondiente.
     * @param valor el valor a formatear
     * @param unidad la unidad del valor
     * @return cadena formateada con valor y unidad
     */
    public String formatearConUnidad(double valor, UnidadMedida unidad) {
        return String.format("%.2f %s", valor, unidad.getSimbolo());
    }
}
