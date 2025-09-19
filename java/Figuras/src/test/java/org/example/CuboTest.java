package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CuboTest {

    @Test
    void calcularVolumenYAreaSuperficie_correctos() {
        Cubo cubo = new Cubo(2, 1);
        assertEquals(8, cubo.calcularVolumen());
        assertEquals(24, cubo.calcularAreaSuperficie());
    }
}
