#pragma once
#include "Figura3d.h"

class Cubo : public Figura3d {
public:
    explicit Cubo(double lado);
    double area() const override;     // área superficial
    double volumen() const override;

    // Nuevo: getter
    double lado() const noexcept { return lado_; }

private:
    double lado_;
};
