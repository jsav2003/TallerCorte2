#pragma once
#include <iostream>
#include <string>
#include <limits>
#include "Cubo.h"
#include "Esfera.h"
#include "Circulo.h"
#include "Cuadrado.h"

class Gestionar
{
public:
    Gestionar();

    void mostrarMenu();
    std::string obtenerOpcion();
    double obtenerNumeroPositivo(const std::string& mensaje);
    void crearCubo();
    void crearEsfera();
    void crearCirculo();
    void crearCuadrado();
    bool procesarOpcion(const std::string& opcion);
    void pausar();
    void ejecutar();
};
