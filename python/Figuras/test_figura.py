"""
Test module for geometric figures classes.

This module contains unit tests for Circulo, Cuadrado, Cubo, and Esfera classes.
Tests cover basic functionality, edge cases, and mathematical accuracy.
"""
import pytest
from circulo import Circulo
from cuadrado import Cuadrado
from cubo import Cubo
from esfera import Esfera


class TestCirculo:
    """Tests para la clase Circulo."""

    def test_crear_circulo(self):
        """Test para verificar la creaciÃ³n de un cÃ­rculo."""
        circulo = Circulo(5)
        assert circulo.radio == 5
        assert circulo.get_nombre() == "Circulo"

    def test_calcular_area_circulo(self):
        """Test para verificar el cÃ¡lculo del Ã¡rea del cÃ­rculo."""
        circulo = Circulo(1)
        expected_area = 3.14159 * 1 ** 2
        assert circulo.calcular_area() == expected_area

        circulo2 = Circulo(5)
        expected_area2 = 3.14159 * 5 ** 2
        assert circulo2.calcular_area() == expected_area2

        circulo3 = Circulo(0.5)
        expected_area3 = 3.14159 * 0.5 ** 2
        assert pytest.approx(circulo3.calcular_area(), rel=1e-5) == expected_area3

    def test_calcular_perimetro_circulo(self):
        """Test para verificar el cÃ¡lculo del perÃ­metro del cÃ­rculo."""
        circulo = Circulo(1)
        expected_perimetro = 2 * 3.14159 * 1
        assert circulo.calcular_perimetro() == expected_perimetro

        circulo2 = Circulo(3)
        expected_perimetro2 = 2 * 3.14159 * 3
        assert circulo2.calcular_perimetro() == expected_perimetro2

    def test_circulo_radio_cero(self):
        """Test para verificar comportamiento con radio cero."""
        circulo = Circulo(0)
        assert circulo.calcular_area() == 0
        assert circulo.calcular_perimetro() == 0


class TestCuadrado:
    """Tests para la clase Cuadrado."""

    def test_crear_cuadrado(self):
        """Test para verificar la creaciÃ³n de un cuadrado."""
        cuadrado = Cuadrado(4)
        assert cuadrado.lado == 4
        assert cuadrado.get_nombre() == "Cuadrado"

    def test_calcular_area_cuadrado(self):
        """Test para verificar el cÃ¡lculo del Ã¡rea del cuadrado."""
        cuadrado = Cuadrado(4)
        assert cuadrado.calcular_area() == 16

        cuadrado2 = Cuadrado(0)
        assert cuadrado2.calcular_area() == 0

        cuadrado3 = Cuadrado(2.5)
        assert cuadrado3.calcular_area() == 6.25

    def test_calcular_perimetro_cuadrado(self):
        """Test para verificar el cÃ¡lculo del perÃ­metro del cuadrado."""
        cuadrado = Cuadrado(4)
        assert cuadrado.calcular_perimetro() == 16

        cuadrado2 = Cuadrado(3)
        assert cuadrado2.calcular_perimetro() == 12

        cuadrado3 = Cuadrado(0)
        assert cuadrado3.calcular_perimetro() == 0


class TestCubo:
    """Tests para la clase Cubo."""

    def test_crear_cubo(self):
        """Test para verificar la creaciÃ³n de un cubo."""
        cubo = Cubo(3)
        assert cubo.lado == 3
        assert cubo.get_nombre() == "Cubo"

    def test_calcular_volumen_cubo(self):
        """Test para verificar el cÃ¡lculo del volumen del cubo."""
        cubo = Cubo(3)
        assert cubo.calcular_volumen() == 27

        cubo2 = Cubo(0)
        assert cubo2.calcular_volumen() == 0

        cubo3 = Cubo(2.5)
        assert cubo3.calcular_volumen() == 15.625

        cubo4 = Cubo(1)
        assert cubo4.calcular_volumen() == 1


class TestEsfera:
    """Tests para la clase Esfera."""

    def test_crear_esfera(self):
        """Test para verificar la creaciÃ³n de una esfera."""
        esfera = Esfera(5)
        assert esfera.radio == 5
        assert esfera.get_nombre() == "Esfera"

    def test_calcular_volumen_esfera(self):
        """Test para verificar el cÃ¡lculo del volumen de la esfera."""
        esfera = Esfera(1)
        expected_volume = (4/3) * 3.14159 * 1 ** 3
        assert pytest.approx(esfera.calcular_volumen(), rel=1e-5) == expected_volume

        esfera2 = Esfera(3)
        expected_volume2 = (4/3) * 3.14159 * 3 ** 3
        assert pytest.approx(esfera2.calcular_volumen(), rel=1e-5) == expected_volume2

        esfera3 = Esfera(0)
        assert esfera3.calcular_volumen() == 0

    def test_volumen_esfera_precision(self):
        """Test para verificar la precisiÃ³n del cÃ¡lculo del volumen."""
        esfera = Esfera(2)
        # Volumen = (4/3) * Ï€ * rÂ³ = (4/3) * 3.14159 * 8
        expected_volume = (4/3) * 3.14159 * 8
        calculated_volume = esfera.calcular_volumen()
        assert pytest.approx(calculated_volume, rel=1e-3) == expected_volume


class TestCasosEspeciales:
    """Tests para casos especiales y validaciones."""

    def test_valores_negativos(self):
        """Test para verificar comportamiento con valores negativos."""
        # Aunque matemÃ¡ticamente no tiene sentido, verificamos que las clases
        # manejen valores negativos
        circulo = Circulo(-1)
        assert circulo.calcular_area() == 3.14159  # (-1)Â² = 1

        cuadrado = Cuadrado(-2)
        assert cuadrado.calcular_area() == 4  # (-2)Â² = 4

        cubo = Cubo(-3)
        assert cubo.calcular_volumen() == -27  # (-3)Â³ = -27

    def test_valores_decimales(self):
        """Test para verificar comportamiento con valores decimales."""
        circulo = Circulo(1.5)
        expected_area = 3.14159 * 1.5 ** 2
        assert pytest.approx(circulo.calcular_area(), rel=1e-5) == expected_area

        cuadrado = Cuadrado(2.7)
        assert pytest.approx(cuadrado.calcular_area(), rel=1e-5) == 7.29

        cubo = Cubo(1.2)
        assert pytest.approx(cubo.calcular_volumen(), rel=1e-5) == 1.728


class TestComparaciones:
    """Tests para comparar resultados entre diferentes figuras."""

    def test_comparar_areas_2d(self):
        """Test para comparar Ã¡reas entre figuras 2D."""
        circulo = Circulo(1)
        cuadrado = Cuadrado(1)

        # El Ã¡rea del cÃ­rculo con radio 1 debe ser mayor que el Ã¡rea del cuadrado con lado 1
        assert circulo.calcular_area() > cuadrado.calcular_area()

    def test_comparar_volumenes_3d(self):
        """Test para comparar volÃºmenes entre figuras 3D."""
        cubo = Cubo(2)
        esfera = Esfera(2)

        # Para valores similares, verificar relaciones esperadas
        cubo_volumen = cubo.calcular_volumen()
        esfera_volumen = esfera.calcular_volumen()

        assert cubo_volumen == 8
        assert esfera_volumen > 30  # Aproximadamente 33.51
