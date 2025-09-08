#pragma once
#include <string>
#include <utility>

class Figura {
protected:
    std::string nombre_;
    std::string tipo_;

public:
    // Declaración (definición en Figura.cpp)
    Figura(std::string nombre, std::string tipo);

    virtual ~Figura() = default;

    // Getters
    const std::string& getNombre() const noexcept { return nombre_; }
    const std::string& getTipo()   const noexcept { return tipo_; }

    // Setters eliminados para evitar 'unusedFunction'
};
