# -*- coding: utf-8 -*-
"""
Archivo: features/steps/figuras_steps.py
Descripción: Step definitions para las pruebas BDD del sistema de figuras geométricas
Framework: behave
"""

import sys
import os
import math
import pytest
from behave import given, when, then, step
from typing import Dict, Any

# Agregar el directorio padre al path para importar los módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

# Importar las clases del sistema de figuras
try:
    from FiguraFactory import FiguraFactory
    from RepositorioFiguras import RepositorioFiguras
    from UnidadAdapter import UnidadAdapter
    from UnidadMedida import UnidadMedida
    from Figura import Figura
    from Circulo import Circulo
    from Cuadrado import Cuadrado
    from Cubo import Cubo
    from Esfera import Esfera
    from GeneradorID import GeneradorID
except ImportError as e:
    print(f"Error importando módulos: {e}")
    sys.exit(1)


# =============================================================================
# STEPS DE CONFIGURACIÓN INICIAL (Antecedentes)
# =============================================================================

@given('que tengo un sistema de figuras geométricas inicializado')
def step_sistema_inicializado(context):
    """Inicializa el sistema de figuras geométricas"""
    context.factory = FiguraFactory()
    context.figuras_creadas = []
    context.ultima_figura = None
    context.ultimo_resultado = None
    context.excepcion_capturada = None
    print("Sistema de figuras geométricas inicializado")


@given('que tengo un repositorio de figuras vacío')
def step_repositorio_vacio(context):
    """Crea un repositorio de figuras vacío"""
    # Usar archivo temporal para las pruebas
    context.repositorio = RepositorioFiguras("test_figuras.json", auto_guardar=False)
    context.repositorio._figuras.clear()  # Limpiar cualquier figura existente
    print("Repositorio de figuras vacío creado")


# =============================================================================
# STEPS PARA CREACIÓN DE FIGURAS
# =============================================================================

@given('que quiero crear una figura de tipo "{tipo}"')
def step_tipo_figura(context, tipo):
    """Define el tipo de figura a crear"""
    context.tipo_figura = tipo
    print(f"Preparando creación de figura tipo: {tipo}")


@when('creo la figura con dimensión {dimension:f}')
def step_crear_figura_dimension(context, dimension):
    """Crea una figura con la dimensión especificada"""
    try:
        context.ultima_figura = context.factory.crear_figura(context.tipo_figura, dimension)
        context.figuras_creadas.append(context.ultima_figura)
        print(f"Figura {context.tipo_figura} creada con dimensión {dimension}")
    except Exception as e:
        context.excepcion_capturada = e
        print(f"Error al crear figura: {e}")


@then('la figura debe ser creada exitosamente')
def step_figura_creada_exitosamente(context):
    """Verifica que la figura fue creada exitosamente"""
    assert context.ultima_figura is not None, "La figura no fue creada"
    assert context.excepcion_capturada is None, f"Se lanzó una excepción: {context.excepcion_capturada}"
    print("Figura creada exitosamente")


@then('debe tener el tipo "{tipo_esperado}"')
def step_verificar_tipo(context, tipo_esperado):
    """Verifica que la figura tenga el tipo esperado"""
    assert context.ultima_figura is not None, "No hay figura para verificar"
    assert context.ultima_figura.get_nombre() == tipo_esperado, \
        f"Tipo esperado: {tipo_esperado}, obtenido: {context.ultima_figura.get_nombre()}"
    print(f"Tipo verificado: {tipo_esperado}")


@then('debe tener un ID único generado')
def step_verificar_id_unico(context):
    """Verifica que la figura tenga un ID único"""
    assert context.ultima_figura is not None, "No hay figura para verificar"
    figura_id = context.ultima_figura.get_id()
    assert figura_id is not None and figura_id > 0, f"ID inválido: {figura_id}"
    print(f"ID único verificado: {figura_id}")


# =============================================================================
# STEPS PARA FIGURAS ESPECÍFICAS
# =============================================================================

@given('que tengo un círculo con radio {radio:f}')
def step_circulo_con_radio(context, radio):
    """Crea un círculo con el radio especificado"""
    context.ultima_figura = context.factory.crear_figura("circulo", radio)
    print(f"Círculo creado con radio {radio}")


@given('que tengo un cuadrado con lado {lado:f}')
def step_cuadrado_con_lado(context, lado):
    """Crea un cuadrado con el lado especificado"""
    context.ultima_figura = context.factory.crear_figura("cuadrado", lado)
    print(f"Cuadrado creado con lado {lado}")


@given('que tengo un cubo con lado {lado:f}')
def step_cubo_con_lado(context, lado):
    """Crea un cubo con el lado especificado"""
    context.ultima_figura = context.factory.crear_figura("cubo", lado)
    print(f"Cubo creado con lado {lado}")


@given('que tengo una esfera con radio {radio:f}')
def step_esfera_con_radio(context, radio):
    """Crea una esfera con el radio especificado"""
    context.ultima_figura = context.factory.crear_figura("esfera", radio)
    print(f"Esfera creada con radio {radio}")


# =============================================================================
# STEPS PARA CÁLCULOS DE PROPIEDADES
# =============================================================================

@when('calculo el área del círculo')
def step_calcular_area_circulo(context):
    """Calcula el área del círculo"""
    assert isinstance(context.ultima_figura, Circulo), "La figura no es un círculo"
    context.ultimo_resultado = context.ultima_figura.calcular_area()
    print(f"Área del círculo calculada: {context.ultimo_resultado}")


@when('calculo el perímetro del círculo')
def step_calcular_perimetro_circulo(context):
    """Calcula el perímetro del círculo"""
    assert isinstance(context.ultima_figura, Circulo), "La figura no es un círculo"
    context.ultimo_resultado = context.ultima_figura.calcular_perimetro()
    print(f"Perímetro del círculo calculado: {context.ultimo_resultado}")


@when('calculo el área del cuadrado')
def step_calcular_area_cuadrado(context):
    """Calcula el área del cuadrado"""
    assert isinstance(context.ultima_figura, Cuadrado), "La figura no es un cuadrado"
    context.ultimo_resultado = context.ultima_figura.calcular_area()
    print(f"Área del cuadrado calculada: {context.ultimo_resultado}")


@when('calculo el perímetro del cuadrado')
def step_calcular_perimetro_cuadrado(context):
    """Calcula el perímetro del cuadrado"""
    assert isinstance(context.ultima_figura, Cuadrado), "La figura no es un cuadrado"
    context.ultimo_resultado = context.ultima_figura.calcular_perimetro()
    print(f"Perímetro del cuadrado calculado: {context.ultimo_resultado}")


@when('calculo el volumen del cubo')
def step_calcular_volumen_cubo(context):
    """Calcula el volumen del cubo"""
    assert isinstance(context.ultima_figura, Cubo), "La figura no es un cubo"
    context.ultimo_resultado = context.ultima_figura.calcular_volumen()
    print(f"Volumen del cubo calculado: {context.ultimo_resultado}")


@when('calculo el volumen de la esfera')
def step_calcular_volumen_esfera(context):
    """Calcula el volumen de la esfera"""
    assert isinstance(context.ultima_figura, Esfera), "La figura no es una esfera"
    context.ultimo_resultado = context.ultima_figura.calcular_volumen()
    print(f"Volumen de la esfera calculado: {context.ultimo_resultado}")


# =============================================================================
# STEPS PARA VERIFICACIÓN DE RESULTADOS
# =============================================================================

@then('el área debe ser aproximadamente {valor_esperado:f}')
def step_verificar_area_aproximada(context, valor_esperado):
    """Verifica que el área sea aproximadamente el valor esperado"""
    assert context.ultimo_resultado is not None, "No hay resultado para verificar"
    assert abs(context.ultimo_resultado - valor_esperado) < 0.01, \
        f"Área esperada: {valor_esperado}, obtenida: {context.ultimo_resultado}"
    print(f"Área verificada: {context.ultimo_resultado} ≈ {valor_esperado}")


@then('el perímetro debe ser aproximadamente {valor_esperado:f}')
def step_verificar_perimetro_aproximado(context, valor_esperado):
    """Verifica que el perímetro sea aproximadamente el valor esperado"""
    assert context.ultimo_resultado is not None, "No hay resultado para verificar"
    assert abs(context.ultimo_resultado - valor_esperado) < 0.01, \
        f"Perímetro esperado: {valor_esperado}, obtenido: {context.ultimo_resultado}"
    print(f"Perímetro verificado: {context.ultimo_resultado} ≈ {valor_esperado}")


@then('el área debe ser {valor_esperado:f}')
def step_verificar_area_exacta(context, valor_esperado):
    """Verifica que el área sea exactamente el valor esperado"""
    assert context.ultimo_resultado is not None, "No hay resultado para verificar"
    assert context.ultimo_resultado == valor_esperado, \
        f"Área esperada: {valor_esperado}, obtenida: {context.ultimo_resultado}"
    print(f"Área verificada: {context.ultimo_resultado}")


@then('el perímetro debe ser {valor_esperado:f}')
def step_verificar_perimetro_exacto(context, valor_esperado):
    """Verifica que el perímetro sea exactamente el valor esperado"""
    assert context.ultimo_resultado is not None, "No hay resultado para verificar"
    assert context.ultimo_resultado == valor_esperado, \
        f"Perímetro esperado: {valor_esperado}, obtenido: {context.ultimo_resultado}"
    print(f"Perímetro verificado: {context.ultimo_resultado}")


@then('el volumen debe ser {valor_esperado:f}')
def step_verificar_volumen_exacto(context, valor_esperado):
    """Verifica que el volumen sea exactamente el valor esperado"""
    assert context.ultimo_resultado is not None, "No hay resultado para verificar"
    assert context.ultimo_resultado == valor_esperado, \
        f"Volumen esperado: {valor_esperado}, obtenido: {context.ultimo_resultado}"
    print(f"Volumen verificado: {context.ultimo_resultado}")


@then('el volumen debe ser aproximadamente {valor_esperado:f}')
def step_verificar_volumen_aproximado(context, valor_esperado):
    """Verifica que el volumen sea aproximadamente el valor esperado"""
    assert context.ultimo_resultado is not None, "No hay resultado para verificar"
    assert abs(context.ultimo_resultado - valor_esperado) < 0.01, \
        f"Volumen esperado: {valor_esperado}, obtenido: {context.ultimo_resultado}"
    print(f"Volumen verificado: {context.ultimo_resultado} ≈ {valor_esperado}")


# =============================================================================
# STEPS PARA REPOSITORIO
# =============================================================================

@given('que tengo un repositorio de figuras')
def step_repositorio_figuras(context):
    """Asegura que hay un repositorio de figuras disponible"""
    if not hasattr(context, 'repositorio'):
        context.repositorio = RepositorioFiguras("test_figuras.json", auto_guardar=False)
    print("Repositorio de figuras disponible")


@given('que creo un círculo con radio {radio:f}')
def step_crear_circulo_radio(context, radio):
    """Crea un círculo con el radio especificado"""
    context.ultima_figura = context.factory.crear_figura("circulo", radio)
    print(f"Círculo creado con radio {radio}")


@when('almaceno la figura en el repositorio')
def step_almacenar_figura(context):
    """Almacena la figura en el repositorio"""
    assert context.ultima_figura is not None, "No hay figura para almacenar"
    context.ultimo_id = context.repositorio.almacenar_figura(context.ultima_figura)
    print(f"Figura almacenada con ID: {context.ultimo_id}")


@then('la figura debe ser almacenada con un ID válido')
def step_verificar_almacenamiento(context):
    """Verifica que la figura fue almacenada con un ID válido"""
    assert context.ultimo_id is not None and context.ultimo_id > 0, \
        f"ID inválido: {context.ultimo_id}"
    print(f"Almacenamiento verificado con ID: {context.ultimo_id}")


@when('busco la figura por su ID')
def step_buscar_figura_por_id(context):
    """Busca la figura por su ID"""
    context.figura_recuperada = context.repositorio.obtener_figura(context.ultimo_id)
    print(f"Figura buscada por ID: {context.ultimo_id}")


@then('debo poder recuperar la figura correctamente')
def step_verificar_recuperacion(context):
    """Verifica que la figura fue recuperada correctamente"""
    assert context.figura_recuperada is not None, "No se pudo recuperar la figura"
    assert context.figura_recuperada.get_id() == context.ultimo_id, \
        f"ID no coincide: esperado {context.ultimo_id}, obtenido {context.figura_recuperada.get_id()}"
    print("Figura recuperada correctamente")


@then('la figura recuperada debe tener radio {radio_esperado:f}')
def step_verificar_radio_recuperado(context, radio_esperado):
    """Verifica que la figura recuperada tenga el radio esperado"""
    assert context.figura_recuperada is not None, "No hay figura recuperada"
    assert isinstance(context.figura_recuperada, Circulo), "La figura recuperada no es un círculo"
    radio_actual = context.figura_recuperada.get_radio()
    assert radio_actual == radio_esperado, \
        f"Radio esperado: {radio_esperado}, obtenido: {radio_actual}"
    print(f"Radio verificado: {radio_actual}")


# =============================================================================
# STEPS PARA CONVERSIÓN DE UNIDADES
# =============================================================================

@given('que tengo un valor de {valor:f} en centímetros')
def step_valor_en_centimetros(context, valor):
    """Define un valor en centímetros"""
    context.valor_original = valor
    context.unidad_original = UnidadMedida.CENTIMETROS
    print(f"Valor original: {valor} cm")


@when('convierto el valor a metros')
def step_convertir_a_metros(context):
    """Convierte el valor a metros"""
    context.valor_convertido = UnidadAdapter.convertir(
        context.valor_original, context.unidad_original, UnidadMedida.METROS
    )
    print(f"Valor convertido: {context.valor_convertido} m")


@then('el resultado debe ser {valor_esperado:f} metros')
def step_verificar_conversion_metros(context, valor_esperado):
    """Verifica que la conversión a metros sea correcta"""
    assert abs(context.valor_convertido - valor_esperado) < 0.001, \
        f"Conversión esperada: {valor_esperado} m, obtenida: {context.valor_convertido} m"
    print(f"Conversión verificada: {context.valor_convertido} m")


@when('convierto {valor:f} metros a milímetros')
def step_convertir_metros_a_milimetros(context, valor):
    """Convierte metros a milímetros"""
    context.valor_convertido = UnidadAdapter.convertir(
        valor, UnidadMedida.METROS, UnidadMedida.MILIMETROS
    )
    print(f"Conversión: {valor} m → {context.valor_convertido} mm")


@then('el resultado debe ser {valor_esperado:f} milímetros')
def step_verificar_conversion_milimetros(context, valor_esperado):
    """Verifica que la conversión a milímetros sea correcta"""
    assert abs(context.valor_convertido - valor_esperado) < 0.001, \
        f"Conversión esperada: {valor_esperado} mm, obtenida: {context.valor_convertido} mm"
    print(f"Conversión verificada: {context.valor_convertido} mm")


# =============================================================================
# STEPS PARA VALIDACIÓN DE ERRORES
# =============================================================================

@given('que intento crear figuras con dimensiones inválidas')
def step_dimensiones_invalidas(context):
    """Prepara para probar dimensiones inválidas"""
    context.excepciones = []
    print("Preparando pruebas de dimensiones inválidas")


@when('intento crear un círculo con radio {radio:f}')
def step_crear_circulo_radio_invalido(context, radio):
    """Intenta crear un círculo con radio inválido"""
    try:
        figura = context.factory.crear_figura("circulo", radio)
        context.excepcion_capturada = None
        print(f"Círculo creado inesperadamente con radio {radio}")
    except Exception as e:
        context.excepcion_capturada = e
        print(f"Excepción capturada al crear círculo con radio {radio}: {e}")


@when('intento crear un cuadrado con lado {lado:f}')
def step_crear_cuadrado_lado_invalido(context, lado):
    """Intenta crear un cuadrado con lado inválido"""
    try:
        figura = context.factory.crear_figura("cuadrado", lado)
        context.excepcion_capturada = None
        print(f"Cuadrado creado inesperadamente con lado {lado}")
    except Exception as e:
        context.excepcion_capturada = e
        print(f"Excepción capturada al crear cuadrado con lado {lado}: {e}")


@then('debe lanzarse una excepción de valor inválido')
def step_verificar_excepcion_valor_invalido(context):
    """Verifica que se lance una excepción por valor inválido"""
    assert context.excepcion_capturada is not None, "Se esperaba una excepción pero no se lanzó"
    assert isinstance(context.excepcion_capturada, (ValueError, TypeError)), \
        f"Tipo de excepción inesperado: {type(context.excepcion_capturada)}"
    print(f"Excepción verificada: {context.excepcion_capturada}")


# =============================================================================
# STEPS PARA MÚLTIPLES FIGURAS
# =============================================================================

@when('creo y almaceno múltiples figuras')
def step_crear_multiples_figuras(context):
    """Crea y almacena múltiples figuras según la tabla"""
    context.figuras_multiples = []
    context.ids_multiples = []
    
    for row in context.table:
        tipo = row['tipo']
        dimension = float(row['dimension'])
        
        # Crear la figura
        figura = context.factory.crear_figura(tipo, dimension)
        
        # Almacenar en el repositorio
        figura_id = context.repositorio.almacenar_figura(figura)
        
        context.figuras_multiples.append(figura)
        context.ids_multiples.append(figura_id)
        
        print(f"Figura {tipo} creada y almacenada con ID {figura_id}")


@when('creo y almaceno múltiples figuras:')
def step_crear_multiples_figuras_tabla(context):
    """Crea y almacena múltiples figuras según la tabla (versión con dos puntos)"""
    step_crear_multiples_figuras(context)


@then('el repositorio debe contener {cantidad:d} figuras')
def step_verificar_cantidad_figuras(context, cantidad):
    """Verifica que el repositorio contenga la cantidad esperada de figuras"""
    cantidad_actual = len(context.repositorio._figuras)
    assert cantidad_actual == cantidad, \
        f"Cantidad esperada: {cantidad}, actual: {cantidad_actual}"
    print(f"Cantidad de figuras verificada: {cantidad_actual}")


@then('puedo listar todas las figuras almacenadas')
def step_listar_figuras(context):
    """Verifica que se puedan listar todas las figuras"""
    figuras = context.repositorio.listar_figuras()
    assert len(figuras) > 0, "No se encontraron figuras en el repositorio"
    print(f"Se listaron {len(figuras)} figuras del repositorio")


@then('cada figura debe tener un ID único diferente')
def step_verificar_ids_unicos(context):
    """Verifica que cada figura tenga un ID único"""
    ids_unicos = set(context.ids_multiples)
    assert len(ids_unicos) == len(context.ids_multiples), \
        f"IDs duplicados encontrados: {context.ids_multiples}"
    print(f"IDs únicos verificados: {context.ids_multiples}")


# =============================================================================
# STEPS COMBINADOS (WHEN + THEN)
# =============================================================================

@step('cuando calculo el perímetro del círculo')
def step_calcular_perimetro_circulo_combinado(context):
    """Step combinado para calcular perímetro del círculo"""
    step_calcular_perimetro_circulo(context)


@step('cuando calculo el perímetro del cuadrado')
def step_calcular_perimetro_cuadrado_combinado(context):
    """Step combinado para calcular perímetro del cuadrado"""
    step_calcular_perimetro_cuadrado(context)


# =============================================================================
# STEPS ADICIONALES PARA COMPLETAR LOS ESCENARIOS
# =============================================================================

@step('dado que tengo una esfera con radio {radio:f}')
def step_crear_esfera_radio_combinado(context, radio):
    """Step combinado para crear esfera con radio específico"""
    step_esfera_con_radio(context, radio)


@step('cuando calculo el volumen de la esfera')
def step_calcular_volumen_esfera_combinado(context):
    """Step combinado para calcular volumen de la esfera"""
    step_calcular_volumen_esfera(context)


@step('cuando busco la figura por su ID')
def step_buscar_figura_por_id_combinado(context):
    """Step combinado para buscar figura por ID"""
    step_buscar_figura_por_id(context)


@step('cuando convierto {valor:f} metros a milímetros')
def step_convertir_metros_a_milimetros_combinado(context, valor):
    """Step combinado para conversión metros a milímetros"""
    step_convertir_metros_a_milimetros(context, valor)


@step('cuando intento crear un cuadrado con lado {lado:f}')
def step_crear_cuadrado_lado_invalido_combinado(context, lado):
    """Step combinado para crear cuadrado con lado inválido"""
    step_crear_cuadrado_lado_invalido(context, lado)