#include <gtest/gtest.h>
#include "Cubo.h"
#include "Esfera.h"
#include "Cuadrado.h"
#include "Circulo.h"

// Pruebas para Esfera
TEST(EsferaTest, CalculoVolumenYAreaYGetter) {
    Esfera e(1.0);
    // usar el getter -> evita unusedFunction
    EXPECT_NEAR(e.radio(), 1.0, 1e-12);

    EXPECT_NEAR(e.volumen(), 4.0 / 3.0 * 3.141592653589793 * 1.0, 1e-6);
    EXPECT_NEAR(e.area(), 4.0 * 3.141592653589793 * 1.0, 1e-6);
}

// Pruebas para Cuadrado
TEST(CuadradoTest, CalculoAreaYGetter) {
    Cuadrado c(2.0);
    // usar el getter -> evita unusedFunction
    EXPECT_NEAR(c.lado(), 2.0, 1e-12);

    EXPECT_NEAR(c.area(), 4.0, 1e-6);
}

// Pruebas para Circulo
TEST(CirculoTest, CalculoAreaYGetter) {
    Circulo circ(1.0);
    // usar el getter -> evita unusedFunction
    EXPECT_NEAR(circ.radio(), 1.0, 1e-12);

    EXPECT_NEAR(circ.area(), 3.141592653589793, 1e-6);
}

// Pruebas para Cubo
TEST(CuboTest, CalculoVolumenYAreaYGetter) {
    Cubo cubo(3.0);
    // usar el getter -> evita unusedFunction
    EXPECT_NEAR(cubo.lado(), 3.0, 1e-12);

    EXPECT_NEAR(cubo.volumen(), 27.0, 1e-6);
    EXPECT_NEAR(cubo.area(), 54.0, 1e-6);
}
