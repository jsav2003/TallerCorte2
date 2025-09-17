# language: es
# Archivo: features/figuras.feature
# Descripción: Pruebas BDD para el sistema de figuras geométricas
# Framework: behave
# Ejecutar con: python -m behave

Característica: Sistema de Figuras Geométricas
  Como usuario del sistema de figuras geométricas
  Quiero poder crear, gestionar y realizar cálculos con diferentes figuras
  Para automatizar el manejo de propiedades geométricas

  Antecedentes:
    Dado que tengo un sistema de figuras geométricas inicializado
    Y que tengo un repositorio de figuras vacío

  Esquema del escenario: Crear figuras geométricas usando FiguraFactory
    Dado que quiero crear una figura de tipo "<tipo>"
    Cuando creo la figura con dimensión <dimension>
    Entonces la figura debe ser creada exitosamente
    Y debe tener el tipo "<tipo_esperado>"
    Y debe tener un ID único generado

    Ejemplos:
      | tipo    | dimension | tipo_esperado |
      | circulo | 5.0       | Círculo       |
      | cuadrado| 4.0       | Cuadrado      |
      | cubo    | 3.0       | Cubo          |
      | esfera  | 6.0       | Esfera        |

  Escenario: Calcular propiedades de un círculo
    Dado que tengo un círculo con radio 5.0
    Cuando calculo el área del círculo
    Entonces el área debe ser aproximadamente 78.54
    Y cuando calculo el perímetro del círculo
    Entonces el perímetro debe ser aproximadamente 31.42

  Escenario: Calcular propiedades de un cuadrado
    Dado que tengo un cuadrado con lado 4.0
    Cuando calculo el área del cuadrado
    Entonces el área debe ser 16.0
    Y cuando calculo el perímetro del cuadrado
    Entonces el perímetro debe ser 16.0

  Escenario: Calcular volumen de figuras 3D
    Dado que tengo un cubo con lado 3.0
    Cuando calculo el volumen del cubo
    Entonces el volumen debe ser 27.0
    Y dado que tengo una esfera con radio 3.0
    Y cuando calculo el volumen de la esfera
    Entonces el volumen debe ser aproximadamente 113.10

  Escenario: Almacenar y recuperar figuras del repositorio
    Dado que tengo un repositorio de figuras
    Y que creo un círculo con radio 2.5
    Cuando almaceno la figura en el repositorio
    Entonces la figura debe ser almacenada con un ID válido
    Y cuando busco la figura por su ID
    Entonces debo poder recuperar la figura correctamente
    Y la figura recuperada debe tener radio 2.5

  Escenario: Convertir unidades de medida
    Dado que tengo un valor de 100.0 en centímetros
    Cuando convierto el valor a metros
    Entonces el resultado debe ser 1.0 metros
    Y cuando convierto 1.0 metros a milímetros
    Entonces el resultado debe ser 1000.0 milímetros

  Escenario: Validar dimensiones inválidas
    Dado que intento crear figuras con dimensiones inválidas
    Cuando intento crear un círculo con radio -5.0
    Entonces debe lanzarse una excepción de valor inválido
    Y cuando intento crear un cuadrado con lado 0.0
    Entonces debe lanzarse una excepción de valor inválido

  Escenario: Gestionar múltiples figuras en el repositorio
    Dado que tengo un repositorio de figuras
    Cuando creo y almaceno múltiples figuras:
      | tipo     | dimension |
      | circulo  | 1.0       |
      | cuadrado | 2.0       |
      | cubo     | 3.0       |
    Entonces el repositorio debe contener 3 figuras
    Y puedo listar todas las figuras almacenadas
    Y cada figura debe tener un ID único diferente