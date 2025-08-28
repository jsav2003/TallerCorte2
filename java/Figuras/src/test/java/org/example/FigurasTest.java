package org.example;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Pruebas integradas: Circulo, Cuadrado, Cubo, Esfera")
class FigurasTest {

    private static final double EPS = 1e-9;

    // =======================
    // Circulo
    // =======================
    @Nested
    @DisplayName("Circulo")
    class CirculoTests {

        @ParameterizedTest(name = "r={0} → área={1}")
        @CsvSource({
                "1.0, 3.141592653589793",
                "5.0, 78.53981633974483",
                "0.5, 0.7853981633974483",
                "0.0, 0.0"
        })
        void area(double r, double esperado) {
            Circulo c = new Circulo(r);
            assertEquals("Circulo", c.getNombre());
            assertEquals("2D", c.getTipo());
            assertEquals(esperado, c.calcularArea(), EPS);
        }

        @ParameterizedTest(name = "r={0} → perímetro={1}")
        @CsvSource({
                "1.0, 6.283185307179586",
                "3.0, 18.84955592153876",
                "0.0, 0.0"
        })
        void perimetro(double r, double esperado) {
            Circulo c = new Circulo(r);
            assertEquals(esperado, c.calcularPerimetro(), EPS);
        }

        @Test
        void negativosSeCuadranEnArea() {
            Circulo c = new Circulo(-1.0);
            assertEquals(Math.PI /* (-1)^2 */, c.calcularArea(), EPS);
        }
    }

    // =======================
    // Cuadrado
    // =======================
    @Nested
    @DisplayName("Cuadrado")
    class CuadradoTests {

        @Test
        void areaYPerimetro() {
            Cuadrado q = new Cuadrado(4.0);
            assertEquals("Cuadrado", q.getNombre());
            assertEquals("2D", q.getTipo());
            assertEquals(16.0, q.calcularArea(), EPS);
            assertEquals(16.0, q.calcularPerimetro(), EPS);
        }

        @Test
        void casosBorde() {
            assertEquals(0.0, new Cuadrado(0.0).calcularArea(), EPS);
            assertEquals(0.0, new Cuadrado(0.0).calcularPerimetro(), EPS);

            // lado negativo: área positiva, perímetro negativo no tiene sentido físico,
            // pero validamos la implementación actual (4*lado).
            Cuadrado neg = new Cuadrado(-2.0);
            assertEquals(4.0, neg.calcularArea(), EPS);
            assertEquals(-8.0, neg.calcularPerimetro(), EPS);
        }
    }

    // =======================
    // Cubo
    // =======================
    @Nested
    @DisplayName("Cubo")
    class CuboTests {

        @Test
        void volumen() {
            Cubo c = new Cubo(3.0);
            assertEquals("Cubo", c.getNombre());
            assertEquals("3D", c.getTipo());
            assertEquals(27.0, c.calcularVolumen(), EPS);
        }

        @Test
        void volumenCerosNegativosDecimales() {
            assertEquals(0.0, new Cubo(0.0).calcularVolumen(), EPS);
            assertEquals(-27.0, new Cubo(-3.0).calcularVolumen(), EPS); // (-3)^3
            assertEquals(15.625, new Cubo(2.5).calcularVolumen(), EPS);
            assertEquals(1.0, new Cubo(1.0).calcularVolumen(), EPS);
        }
    }

    // =======================
    // Esfera
    // =======================
    @Nested
    @DisplayName("Esfera")
    class EsferaTests {

        @ParameterizedTest(name = "r={0}")
        @CsvSource({"1.0", "3.0", "2.0"})
        void volumenComparadoConFormula(double r) {
            Esfera e = new Esfera(r);
            assertEquals("Esfera", e.getNombre());
            assertEquals("3D", e.getTipo());
            double esperado = (4.0 / 3.0) * Math.PI * r * r * r;
            assertEquals(esperado, e.calcularVolumen(), 1e-9);
        }

        @Test
        void volumenCero() {
            assertEquals(0.0, new Esfera(0.0).calcularVolumen(), EPS);
        }
    }

    // =======================
    // Comparaciones entre figuras
    // =======================
    @Nested
    @DisplayName("Comparaciones")
    class Comparaciones {

        @Test
        void areaCirculoVsCuadrado() {
            Circulo c = new Circulo(1.0);
            Cuadrado q = new Cuadrado(1.0);
            assertTrue(c.calcularArea() > q.calcularArea());
        }

        @Test
        void volumenCuboVsEsfera() {
            Cubo cubo = new Cubo(2.0);
            Esfera esfera = new Esfera(2.0);

            assertEquals(8.0, cubo.calcularVolumen(), EPS);
            assertTrue(esfera.calcularVolumen() > 30.0); // ~33.51
        }
    }
}
