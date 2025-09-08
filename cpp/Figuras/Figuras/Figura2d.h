#pragma once
#include <string>
#include "Figura.h"

class Figura2d : public Figura
{
public:
    explicit Figura2d(const std::string& nombre)
        : Figura(nombre, "2D") {
    }

    virtual double area() const = 0;
    virtual double perimetro() const = 0;

    ~Figura2d() override = default;
};
