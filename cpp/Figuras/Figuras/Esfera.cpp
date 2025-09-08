#include "Esfera.h"
#include <cmath>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

Esfera::Esfera(double radio) : Figura3d("Esfera"), radio_(radio) {}

double Esfera::area() const {
    return 4.0 * M_PI * radio_ * radio_;
}

double Esfera::volumen() const {
    return (4.0 / 3.0) * M_PI * radio_ * radio_ * radio_;
}
