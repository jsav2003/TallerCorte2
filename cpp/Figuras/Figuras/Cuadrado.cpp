#include "Cuadrado.h"

Cuadrado::Cuadrado(double lado) : Figura2d("Cuadrado"), lado_(lado) {}

double Cuadrado::area() const {
    return lado_ * lado_;
}

double Cuadrado::perimetro() const {
    return 4 * lado_;
}
