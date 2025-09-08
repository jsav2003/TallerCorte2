#include "Circulo.h"
#include <cmath>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

Circulo::Circulo(double radio) : Figura2d("Círculo"), radio_(radio) {}

double Circulo::area() const {
    return M_PI * radio_ * radio_;
}

double Circulo::perimetro() const {
    return 2 * M_PI * radio_;
}
