package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CuadradoTest {

    @Test
    void crearConLadoInvalido_deberiaLanzar() {
        assertThrows(IllegalArgumentException.class, () -> new Cuadrado(0, 1));
    }

    @Test
    void calcularAreaYPerimetro_correctos() {
        Cuadrado q = new Cuadrado(3, 1);
        assertEquals(9, q.calcularArea());
        assertEquals(12, q.calcularPerimetro());
    }
}
