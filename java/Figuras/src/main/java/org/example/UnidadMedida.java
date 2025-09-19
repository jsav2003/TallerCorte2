package org.example;

import java.util.HashMap;
import java.util.Map;

/**
 * Enumeración para unidades de medida
 */
public enum UnidadMedida {
    METROS("m"),
    CENTIMETROS("cm"),
    MILIMETROS("mm"),
    PULGADAS("in"),
    PIES("ft");
    
    private final String simbolo;
    
    /**
     * Constructor privado del enum
     * @param simbolo Símbolo de la unidad
     */
    UnidadMedida(String simbolo) {
        this.simbolo = simbolo;
    }
    
    /**
     * Obtiene el factor de conversión a metros
     * @return Factor de conversión a metros
     */
    public double getFactorConversion() {
        switch (this) {
            case METROS:
                return 1.0;
            case CENTIMETROS:
                return 0.01;
            case MILIMETROS:
                return 0.001;
            case PULGADAS:
                return 0.0254;
            case PIES:
                return 0.3048;
            default:
                return 1.0;
        }
    }
    
    /**
     * Obtiene el símbolo de la unidad
     * @return Símbolo de la unidad
     */
    public String getSimbolo() {
        return this.simbolo;
    }
    
    /**
     * Obtiene un mapa con los nombres completos de las unidades
     * @return Mapa con nombres completos
     */
    public static Map<String, String> getNombresCompletos() {
        Map<String, String> nombres = new HashMap<>();
        nombres.put(METROS.getSimbolo(), "metros");
        nombres.put(CENTIMETROS.getSimbolo(), "centímetros");
        nombres.put(MILIMETROS.getSimbolo(), "milímetros");
        nombres.put(PULGADAS.getSimbolo(), "pulgadas");
        nombres.put(PIES.getSimbolo(), "pies");
        return nombres;
    }
}