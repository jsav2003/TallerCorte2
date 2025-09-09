"""
Pruebas unitarias para el sistema de figuras geomÃ©tricas.
Implementa los criterios BDD definidos en las historias de usuario.
"""
import pytest
import os
import tempfile
import json
from figura import Figura
from figura_factory import FiguraFactory
from repositorio_figuras import RepositorioFiguras
from unidad_adapter import UnidadAdapter, UnidadMedida
from generador_id import GeneradorID
from circulo import Circulo
from cuadrado import Cuadrado
from cubo import Cubo
from esfera import Esfera

class TestCreacionFigurasConID:
    """Pruebas para la creaciÃ³n de figuras con identificadores Ãºnicos."""

    def setup_method(self):
        """ConfiguraciÃ³n inicial para cada prueba."""
        # Reiniciar el generador de IDs
        generador = GeneradorID()
        generador.reiniciar_contador()

    def test_figura_tiene_id_unico(self):
        """
        BDD: Dado que el usuario crea una figura,
        Cuando ingresa dimensiones vÃ¡lidas,
        Entonces el sistema asigna un ID Ãºnico.
        """
        # Given: El sistema estÃ¡ inicializado
        circulo = FiguraFactory.crear_figura('circulo', radio=5)

        # When/Then: La figura debe tener un ID Ãºnico mayor que 0
        assert circulo.get_id() > 0
        assert isinstance(circulo.get_id(), int)

    def test_multiples_figuras_ids_diferentes(self):
        """
        BDD: Dado que se crean mÃºltiples figuras,
        Cuando el sistema asigna IDs,
        Entonces cada figura tiene un identificador diferente.
        """
        # Given/When: Se crean mÃºltiples figuras
        circulo1 = FiguraFactory.crear_figura('circulo', radio=3)
        cuadrado1 = FiguraFactory.crear_figura('cuadrado', lado=4)
        esfera1 = FiguraFactory.crear_figura('esfera', radio=2)

        # Then: Todos los IDs deben ser diferentes
        ids = [circulo1.get_id(), cuadrado1.get_id(), esfera1.get_id()]
        assert len(ids) == len(set(ids)), "Los IDs deben ser Ãºnicos"

        # Y deben ser consecutivos
        assert circulo1.get_id() == 1
        assert cuadrado1.get_id() == 2
        assert esfera1.get_id() == 3

class TestFactory:
    """Pruebas para el patrÃ³n Factory Method."""

    def setup_method(self):
        """ConfiguraciÃ³n inicial para cada prueba."""
        # Reiniciar el generador de IDs
        generador = GeneradorID()
        generador.reiniciar_contador()

    def test_factory_crea_circulo(self):
        """Prueba que el factory crea cÃ­rculos correctamente."""
        circulo = FiguraFactory.crear_figura('circulo', radio=5)

        assert isinstance(circulo, Circulo)
        assert circulo.get_radio() == 5
        assert circulo.get_nombre() == "Circulo"

    def test_factory_crea_cuadrado(self):
        """Prueba que el factory crea cuadrados correctamente."""
        cuadrado = FiguraFactory.crear_figura('cuadrado', lado=4)

        assert isinstance(cuadrado, Cuadrado)
        assert cuadrado.get_lado() == 4
        assert cuadrado.get_nombre() == "Cuadrado"

    def test_factory_valida_tipo_invalido(self):
        """
        BDD: Dado que se proporciona un tipo invÃ¡lido,
        Cuando se intenta crear la figura,
        Entonces se debe lanzar una excepciÃ³n.
        """
        with pytest.raises(ValueError, match="Tipo de figura no vÃ¡lido"):
            FiguraFactory.crear_figura('triangulo', lado=3)

    def test_factory_valida_parametros_negativos(self):
        """
        BDD: Dado que se proporcionan parÃ¡metros invÃ¡lidos,
        Cuando se intenta crear la figura,
        Entonces se debe lanzar una excepciÃ³n de validaciÃ³n.
        """
        with pytest.raises(ValueError, match="debe ser mayor que 0"):
            FiguraFactory.crear_figura('circulo', radio=-5)

        with pytest.raises(ValueError, match="debe ser mayor que 0"):
            FiguraFactory.crear_figura('cuadrado', lado=0)

class TestUnidadAdapter:
    """Pruebas para el patrÃ³n Adapter de conversiÃ³n de unidades."""

    def setup_method(self):
        """ConfiguraciÃ³n inicial para cada prueba."""
        self.adapter = UnidadAdapter()
        # Reiniciar el generador de IDs
        generador = GeneradorID()
        generador.reiniciar_contador()

    def test_conversion_longitud_metros_a_centimetros(self):
        """
        BDD: Dado que tengo una medida en metros,
        Cuando solicito conversiÃ³n a centÃ­metros,
        Entonces el resultado debe ser correcto.
        """
        # Given: Un cÃ­rculo con radio 1 metro
        circulo = FiguraFactory.crear_figura('circulo', radio=1)

        # When: Convierto las medidas a centÃ­metros
        medidas = self.adapter.convertir_medidas_figura(
            circulo, UnidadMedida.METROS, UnidadMedida.CENTIMETROS
        )

        # Then: El radio debe ser 100 cm
        assert abs(medidas['radio'] - 100) < 0.001
        # Y el Ã¡rea debe convertirse correctamente (Ï€ * 1mÂ² = Ï€ * 10000cmÂ²)
        assert abs(medidas['area'] - (3.14159 * 10000)) < 100

    def test_conversion_misma_unidad(self):
        """Prueba que no hay cambios al convertir a la misma unidad."""
        circulo = FiguraFactory.crear_figura('circulo', radio=5)

        medidas = self.adapter.convertir_medidas_figura(
            circulo, UnidadMedida.METROS, UnidadMedida.METROS
        )

        assert medidas['radio'] == 5
        assert abs(medidas['area'] - circulo.calcular_area()) < 0.001

    def test_validacion_unidad_invalida(self):
        """
        BDD: Dado que se proporciona una unidad invÃ¡lida,
        Cuando se intenta convertir,
        Entonces se debe lanzar una excepciÃ³n.
        """
        circulo = FiguraFactory.crear_figura('circulo', radio=1)

        with pytest.raises(ValueError, match="Unidad de origen no vÃ¡lida"):
            self.adapter.convertir_medidas_figura(circulo, "km", UnidadMedida.METROS)

class TestRepositorioFiguras:
    """Pruebas para el repositorio de figuras."""

    def setup_method(self):
        """ConfiguraciÃ³n inicial para cada prueba."""
        # Crear archivo temporal para pruebas
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.repositorio = RepositorioFiguras(self.temp_file.name)
        # Reiniciar el generador de IDs
        generador = GeneradorID()
        generador.reiniciar_contador()

    def teardown_method(self):
        """Limpieza despuÃ©s de cada prueba."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_almacenar_figura(self):
        """
        BDD: Dado que tengo una figura,
        Cuando la almaceno en el repositorio,
        Entonces debe quedar guardada y accesible.
        """
        # Given: Una figura
        circulo = FiguraFactory.crear_figura('circulo', radio=5)

        # When: La almaceno
        figura_id = self.repositorio.almacenar_figura(circulo)

        # Then: Debe estar accesible
        figura_recuperada = self.repositorio.obtener_figura(figura_id)
        assert figura_recuperada is not None
        assert figura_recuperada.get_id() == figura_id
        assert figura_recuperada.get_radio() == 5

    def test_multiples_figuras_coexisten(self):
        """
        BDD: Dado que creo mÃºltiples figuras,
        Cuando las almaceno,
        Entonces todas coexisten en memoria.
        """
        # Given/When: MÃºltiples figuras almacenadas
        circulo = FiguraFactory.crear_figura('circulo', radio=3)
        cuadrado = FiguraFactory.crear_figura('cuadrado', lado=4)

        self.repositorio.almacenar_figura(circulo)
        self.repositorio.almacenar_figura(cuadrado)

        # Then: Ambas deben coexistir
        todas_figuras = self.repositorio.obtener_todas_figuras()
        assert len(todas_figuras) == 2

        # Y deben ser los tipos correctos
        tipos = [f.get_nombre() for f in todas_figuras]
        assert "Circulo" in tipos
        assert "Cuadrado" in tipos

    def test_eliminar_figura(self):
        """
        BDD: Dado que tengo figuras almacenadas,
        Cuando elimino una por ID,
        Entonces ya no debe existir en el repositorio.
        """
        # Given: Figuras almacenadas
        circulo = FiguraFactory.crear_figura('circulo', radio=5)
        cuadrado = FiguraFactory.crear_figura('cuadrado', lado=4)

        id_circulo = self.repositorio.almacenar_figura(circulo)
        id_cuadrado = self.repositorio.almacenar_figura(cuadrado)

        # When: Elimino una figura
        resultado = self.repositorio.eliminar_figura(id_circulo)

        # Then: Debe haberse eliminado
        assert resultado is True
        assert self.repositorio.obtener_figura(id_circulo) is None
        assert self.repositorio.obtener_figura(id_cuadrado) is not None
        assert self.repositorio.contar_figuras() == 1

    def test_eliminar_figura_inexistente(self):
        """
        BDD: Dado que intento eliminar un ID inexistente,
        Cuando ejecuto la eliminaciÃ³n,
        Entonces debe retornar False.
        """
        resultado = self.repositorio.eliminar_figura(999)
        assert resultado is False

    def test_persistencia_guardar(self):
        """
        BDD: Dado que tengo figuras en memoria,
        Cuando solicito guardar,
        Entonces se debe crear el archivo de persistencia.
        """
        # Given: Figuras en memoria
        circulo = FiguraFactory.crear_figura('circulo', radio=5)
        self.repositorio.almacenar_figura(circulo)

        # When: Guardo
        resultado = self.repositorio.guardar_figuras()

        # Then: El archivo debe existir y contener datos
        assert resultado is True
        assert os.path.exists(self.temp_file.name)

        with open(self.temp_file.name, 'r') as f:
            datos = json.load(f)
            assert 'figuras' in datos
            assert len(datos['figuras']) == 1
            assert datos['figuras'][0]['nombre'] == 'Circulo'

    def test_persistencia_cargar(self):
        """
        BDD: Dado que existe un archivo con figuras,
        Cuando cargo las figuras,
        Entonces deben aparecer en memoria.
        """
        # Given: Archivo con figuras guardadas
        circulo = FiguraFactory.crear_figura('circulo', radio=7)
        self.repositorio.almacenar_figura(circulo)
        self.repositorio.guardar_figuras()

        # Simulo nuevo repositorio
        nuevo_repositorio = RepositorioFiguras(self.temp_file.name)

        # Then: Las figuras deben haberse cargado
        figuras = nuevo_repositorio.obtener_todas_figuras()
        assert len(figuras) == 1
        assert figuras[0].get_nombre() == "Circulo"
        assert figuras[0].get_radio() == 7

class TestValidacionEntradas:
    """Pruebas para validaciÃ³n de entradas invÃ¡lidas."""

    def setup_method(self):
        """ConfiguraciÃ³n inicial para cada prueba."""
        # Reiniciar el generador de IDs
        generador = GeneradorID()
        generador.reiniciar_contador()

    def test_radio_negativo_circulo(self):
        """
        BDD: Dado que intento crear un cÃ­rculo con radio negativo,
        Cuando ejecuto la creaciÃ³n,
        Entonces debe lanzarse una excepciÃ³n.
        """
        with pytest.raises(ValueError, match="debe ser mayor que 0"):
            FiguraFactory.crear_figura('circulo', radio=-5)

    def test_lado_cero_cuadrado(self):
        """
        BDD: Dado que intento crear un cuadrado con lado cero,
        Cuando ejecuto la creaciÃ³n,
        Entonces debe lanzarse una excepciÃ³n.
        """
        with pytest.raises(ValueError, match="debe ser mayor que 0"):
            FiguraFactory.crear_figura('cuadrado', lado=0)

    def test_tipo_dato_incorrecto(self):
        """
        BDD: Dado que proporciono un tipo de dato incorrecto,
        Cuando intento crear una figura,
        Entonces debe lanzarse una excepciÃ³n de tipo.
        """
        with pytest.raises(ValueError):
            FiguraFactory.crear_figura('circulo', radio="texto")

        with pytest.raises(ValueError):
            FiguraFactory.crear_figura('cuadrado', lado="abc")

if __name__ == "__main__":
    # Ejecutar pruebas con pytest
    pytest.main([__file__, "-v"])
