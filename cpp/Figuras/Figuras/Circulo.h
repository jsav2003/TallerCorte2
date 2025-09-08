#pragma once
#include "Figura2d.h"

class Circulo : public Figura2d {
public:
    explicit Circulo(double radio);
    double area() const override;
    double perimetro() const override;

    // Nuevo: getter para marcar uso del miembro y exponer API
    double radio() const noexcept { return radio_; }

private:
    double radio_;
};
