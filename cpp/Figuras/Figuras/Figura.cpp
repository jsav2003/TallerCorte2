#include "Figura.h"
#include <utility>

Figura::Figura(std::string nombre, std::string tipo)
    : nombre_(std::move(nombre)), tipo_(std::move(tipo)) {
}
