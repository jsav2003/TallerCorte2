#pragma once
#include "Figura3d.h"

class Esfera : public Figura3d {
public:
    explicit Esfera(double radio);
    double area() const override;     // área superficial
    double volumen() const override;

    // Nuevo: getter
    double radio() const noexcept { return radio_; }

private:
    double radio_;
};
