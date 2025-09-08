#pragma once
#include <string>
#include "Figura.h"

class Figura3d : public Figura
{
public:
    explicit Figura3d(const std::string& nombre)
        : Figura(nombre, "3D") {
    }

    virtual double area() const = 0;     // área superficial
    virtual double volumen() const = 0;

    ~Figura3d() override = default;
};
