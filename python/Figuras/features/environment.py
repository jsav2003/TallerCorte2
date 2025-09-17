# -*- coding: utf-8 -*-
"""
Archivo: features/environment.py
Descripción: Configuración del entorno para las pruebas BDD con behave
Framework: behave
"""

import os
import sys
import tempfile
import shutil
from typing import Any

# Agregar el directorio padre al path para importar los módulos
def before_all(context: Any) -> None:
    """
    Configuración inicial antes de ejecutar todas las pruebas
    
    Args:
        context: Contexto de behave que mantiene el estado durante las pruebas
    """
    print("\n" + "="*60)
    print("INICIANDO PRUEBAS BDD - SISTEMA DE FIGURAS GEOMÉTRICAS")
    print("="*60)
    
    # Configurar el path para importar módulos del proyecto
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    
    if project_dir not in sys.path:
        sys.path.insert(0, project_dir)
    
    # Crear directorio temporal para archivos de prueba
    context.temp_dir = tempfile.mkdtemp(prefix="figuras_test_")
    context.original_cwd = os.getcwd()
    
    print(f"Directorio temporal de pruebas: {context.temp_dir}")
    print(f"Directorio del proyecto: {project_dir}")
    
    # Inicializar contadores para estadísticas
    context.test_stats = {
        'scenarios_passed': 0,
        'scenarios_failed': 0,
        'steps_passed': 0,
        'steps_failed': 0
    }


def before_feature(context: Any, feature: Any) -> None:
    """
    Configuración antes de ejecutar cada feature
    
    Args:
        context: Contexto de behave
        feature: Feature que se va a ejecutar
    """
    print(f"\n📋 EJECUTANDO FEATURE: {feature.name}")
    print("-" * 50)
    
    # Reiniciar el generador de IDs para cada feature
    try:
        from GeneradorID import GeneradorID
        GeneradorID._ultimo_id = 0
        print("✅ Generador de IDs reiniciado")
    except ImportError:
        print("⚠️  No se pudo importar GeneradorID")


def before_scenario(context: Any, scenario: Any) -> None:
    """
    Configuración antes de ejecutar cada escenario
    
    Args:
        context: Contexto de behave
        scenario: Escenario que se va a ejecutar
    """
    print(f"\n🎯 ESCENARIO: {scenario.name}")
    
    # Cambiar al directorio temporal para archivos de prueba
    os.chdir(context.temp_dir)
    
    # Limpiar archivos de prueba anteriores
    for file in os.listdir(context.temp_dir):
        if file.endswith('.json'):
            os.remove(os.path.join(context.temp_dir, file))
    
    # Inicializar variables de contexto para el escenario
    context.ultima_figura = None
    context.ultimo_resultado = None
    context.excepcion_capturada = None
    context.figuras_creadas = []
    context.ultimo_id = None
    context.figura_recuperada = None
    context.valor_original = None
    context.valor_convertido = None
    context.unidad_original = None
    context.excepciones = []
    context.figuras_multiples = []
    context.ids_multiples = []


def after_scenario(context: Any, scenario: Any) -> None:
    """
    Limpieza después de ejecutar cada escenario
    
    Args:
        context: Contexto de behave
        scenario: Escenario que se ejecutó
    """
    # Actualizar estadísticas
    if scenario.status == "passed":
        context.test_stats['scenarios_passed'] += 1
        print(f"✅ ESCENARIO PASÓ: {scenario.name}")
    else:
        context.test_stats['scenarios_failed'] += 1
        print(f"❌ ESCENARIO FALLÓ: {scenario.name}")
        if hasattr(context, 'excepcion_capturada') and context.excepcion_capturada:
            print(f"   Error: {context.excepcion_capturada}")
    
    # Limpiar variables de contexto específicas del escenario
    scenario_vars = [
        'ultima_figura', 'ultimo_resultado', 'excepcion_capturada',
        'figuras_creadas', 'ultimo_id', 'figura_recuperada',
        'valor_original', 'valor_convertido', 'unidad_original',
        'excepciones', 'figuras_multiples', 'ids_multiples'
    ]
    
    for var in scenario_vars:
        if hasattr(context, var):
            delattr(context, var)


def after_feature(context: Any, feature: Any) -> None:
    """
    Limpieza después de ejecutar cada feature
    
    Args:
        context: Contexto de behave
        feature: Feature que se ejecutó
    """
    print(f"\n📋 FEATURE COMPLETADA: {feature.name}")
    print(f"   Estado: {'✅ PASÓ' if feature.status == 'passed' else '❌ FALLÓ'}")
    
    # Limpiar archivos temporales de la feature
    for file in os.listdir(context.temp_dir):
        if file.endswith('.json'):
            try:
                os.remove(os.path.join(context.temp_dir, file))
            except OSError:
                pass


def after_all(context: Any) -> None:
    """
    Limpieza final después de ejecutar todas las pruebas
    
    Args:
        context: Contexto de behave
    """
    print("\n" + "="*60)
    print("RESUMEN DE PRUEBAS BDD - SISTEMA DE FIGURAS GEOMÉTRICAS")
    print("="*60)
    
    # Mostrar estadísticas finales
    total_scenarios = context.test_stats['scenarios_passed'] + context.test_stats['scenarios_failed']
    pass_rate = (context.test_stats['scenarios_passed'] / total_scenarios * 100) if total_scenarios > 0 else 0
    
    print(f"📊 ESTADÍSTICAS:")
    print(f"   Escenarios ejecutados: {total_scenarios}")
    print(f"   Escenarios pasaron: {context.test_stats['scenarios_passed']} ✅")
    print(f"   Escenarios fallaron: {context.test_stats['scenarios_failed']} ❌")
    print(f"   Tasa de éxito: {pass_rate:.1f}%")
    
    # Restaurar directorio original
    os.chdir(context.original_cwd)
    
    # Limpiar directorio temporal
    try:
        shutil.rmtree(context.temp_dir)
        print(f"🧹 Directorio temporal limpiado: {context.temp_dir}")
    except OSError as e:
        print(f"⚠️  Error al limpiar directorio temporal: {e}")
    
    # Mensaje final
    if context.test_stats['scenarios_failed'] == 0:
        print("\n🎉 ¡TODAS LAS PRUEBAS BDD PASARON EXITOSAMENTE!")
    else:
        print(f"\n⚠️  {context.test_stats['scenarios_failed']} PRUEBA(S) FALLARON")
    
    print("="*60)


def before_step(context: Any, step: Any) -> None:
    """
    Configuración antes de ejecutar cada step (opcional)
    
    Args:
        context: Contexto de behave
        step: Step que se va a ejecutar
    """
    # Se puede usar para logging detallado si es necesario
    pass


def after_step(context: Any, step: Any) -> None:
    """
    Configuración después de ejecutar cada step (opcional)
    
    Args:
        context: Contexto de behave
        step: Step que se ejecutó
    """
    # Actualizar estadísticas de steps
    if step.status == "passed":
        context.test_stats['steps_passed'] += 1
    else:
        context.test_stats['steps_failed'] += 1
        # Para debugging, se puede agregar logging aquí
        if step.status == "failed" and hasattr(step, 'exception'):
            print(f"   ⚠️  Step falló: {step.name}")
            print(f"      Error: {step.exception}")


# Configuraciones adicionales de behave
def pytest_configure(config):
    """Configuración específica para pytest si se usa"""
    pass


# Función auxiliar para verificar imports
def verificar_imports() -> bool:
    """
    Verifica que todos los imports necesarios estén disponibles
    
    Returns:
        bool: True si todos los imports están disponibles
    """
    modulos_requeridos = [
        'FiguraFactory',
        'RepositorioFiguras', 
        'UnidadAdapter',
        'UnidadMedida',
        'Figura',
        'Circulo',
        'Cuadrado',
        'Cubo',
        'Esfera',
        'GeneradorID'
    ]
    
    imports_exitosos = []
    imports_fallidos = []
    
    for modulo in modulos_requeridos:
        try:
            __import__(modulo)
            imports_exitosos.append(modulo)
        except ImportError:
            imports_fallidos.append(modulo)
    
    if imports_fallidos:
        print(f"⚠️  Imports fallidos: {imports_fallidos}")
        return False
    else:
        print(f"✅ Todos los imports exitosos: {imports_exitosos}")
        return True