package org.example;

import java.util.Arrays;
import java.util.List;

/**
 * Adaptador para conversión entre unidades de medida
 */
public class UnidadAdapter {
    
    /**
     * Convierte un valor de una unidad a otra
     * @param valor Valor a convertir
     * @param desde Unidad de origen
     * @param hacia Unidad de destino
     * @return Valor convertido
     */
    public static double convertir(double valor, UnidadMedida desde, UnidadMedida hacia) {
        if (desde == hacia) {
            return valor;
        }
        
        // Convertir a metros primero
        double valorEnMetros = valor * desde.getFactorConversion();
        
        // Convertir de metros a la unidad destino
        double factorDestino = hacia.getFactorConversion();
        return valorEnMetros / factorDestino;
    }
    
    /**
     * Formatea un valor con su unidad
     * @param valor Valor a formatear
     * @param unidad Unidad del valor
     * @return Valor formateado con unidad
     */
    public static String formatearConUnidad(double valor, UnidadMedida unidad) {
        return String.format("%.2f %s", valor, unidad.getSimbolo());
    }
    
    /**
     * Obtiene una lista de todas las unidades disponibles
     * @return Lista de unidades disponibles
     */
    public static List<UnidadMedida> obtenerUnidadesDisponibles() {
        return Arrays.asList(UnidadMedida.values());
    }
}