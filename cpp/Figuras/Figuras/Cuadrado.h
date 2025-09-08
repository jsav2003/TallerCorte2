#pragma once
#include "Figura2d.h"

class Cuadrado : public Figura2d {
public:
    explicit Cuadrado(double lado);
    double area() const override;
    double perimetro() const override;

    // Nuevo: getter
    double lado() const noexcept { return lado_; }

private:
    double lado_;
};
