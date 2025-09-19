package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class EsferaTest {

    @Test
    void calcularVolumenYAreaSuperficie_correctos() {
        Esfera e = new Esfera(1, 1);
        assertEquals(4.0/3.0 * Math.PI, e.calcularVolumen(), 1e-6);
        assertEquals(4 * Math.PI, e.calcularAreaSuperficie(), 1e-6);
    }
}
