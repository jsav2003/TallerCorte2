package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CirculoTest {

    @Test
    void crearConRadioInvalido_deberiaLanzar() {
        assertThrows(IllegalArgumentException.class, () -> new Circulo(0, 1));
        assertThrows(IllegalArgumentException.class, () -> new Circulo(-5, 1));
    }

    @Test
    void calcularAreaYPerimetro_correctos() {
        Circulo c = new Circulo(2, 1);
        assertEquals(Math.PI * 4, c.calcularArea(), 1e-6);
        assertEquals(2 * Math.PI * 2, c.calcularPerimetro(), 1e-6);
    }

    @Test
    void setRadioInvalido_deberiaLanzar() {
        Circulo c = new Circulo(1, 1);
        assertThrows(IllegalArgumentException.class, () -> c.setRadio(0));
    }
}
