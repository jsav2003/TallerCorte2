#include "Cubo.h"

Cubo::Cubo(double lado) : Figura3d("Cubo"), lado_(lado) {}

double Cubo::area() const {
    return 6 * lado_ * lado_;
}

double Cubo::volumen() const {
    return lado_ * lado_ * lado_;
}
