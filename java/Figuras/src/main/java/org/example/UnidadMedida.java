package org.example;

import java.util.HashMap;
import java.util.Map;

/**
 * Enum para representar unidades de medida.
 */
public enum UnidadMedida {
    METROS(1.0, "m"),
    CENTIMETROS(0.01, "cm"),
    MILIMETROS(0.001, "mm"),
    KILOMETROS(1000.0, "km"),
    PULGADAS(0.0254, "in"),
    PIES(0.3048, "ft");

    private final double factorConversion;
    private final String simbolo;

    /**
     * Constructor de UnidadMedida.
     * @param factorConversion factor para convertir a metros
     * @param simbolo símbolo de la unidad
     */
    UnidadMedida(double factorConversion, String simbolo) {
        this.factorConversion = factorConversion;
        this.simbolo = simbolo;
    }

    /**
     * Obtiene el factor de conversión a metros.
     * @return el factor de conversión
     */
    public double getFactorConversion() {
        return factorConversion;
    }

    /**
     * Obtiene el símbolo de la unidad.
     * @return el símbolo
     */
    public String getSimbolo() {
        return simbolo;
    }

    /**
     * Obtiene los nombres completos de las unidades.
     * @return mapa con los nombres completos
     */
    public static Map<UnidadMedida, String> getNombresCompletos() {
        Map<UnidadMedida, String> nombres = new HashMap<>();
        nombres.put(METROS, "Metros");
        nombres.put(CENTIMETROS, "Centímetros");
        nombres.put(MILIMETROS, "Milímetros");
        nombres.put(KILOMETROS, "Kilómetros");
        nombres.put(PULGADAS, "Pulgadas");
        nombres.put(PIES, "Pies");
        return nombres;
    }
}
