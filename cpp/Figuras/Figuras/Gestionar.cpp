#include "Gestionar.h"
#include <iomanip>
#include <sstream>

Gestionar::Gestionar() {}

void Gestionar::mostrarMenu() {
    std::cout << "\n========================================\n";
    std::cout << "    GESTOR DE FIGURAS GEOMETRICAS\n";
    std::cout << "========================================\n";
    std::cout << "1. Crear Cubo\n";
    std::cout << "2. Crear Esfera\n";
    std::cout << "3. Crear Circulo\n";
    std::cout << "4. Crear Cuadrado\n";
    std::cout << "5. Salir\n";
    std::cout << "----------------------------------------\n";
}

std::string Gestionar::obtenerOpcion() {
    std::string opcion;
    while (true) {
        std::cout << "Seleccione una opcion (1-5): ";
        std::getline(std::cin, opcion);
        if (opcion.length() == 1 && opcion >= "1" && opcion <= "5") {
            return opcion;
        }
        else {
            std::cout << "Error: Ingrese una opcion valida (1-5)\n";
        }
    }
}

double Gestionar::obtenerNumeroPositivo(const std::string& mensaje) {
    std::string input;
    double valor;
    while (true) {
        std::cout << mensaje;
        std::getline(std::cin, input);
        std::stringstream ss(input);
        if (ss >> valor && ss.eof() && valor > 0) {
            return valor;
        }
        else {
            std::cout << "Error: Ingrese un numero valido mayor que 0\n";
        }
    }
}

void Gestionar::crearCubo() {
    double lado = obtenerNumeroPositivo("Ingrese la longitud del lado del cubo: ");
    Figura3d* objeto = new Cubo(lado);
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Figura: " << objeto->getNombre() << " (" << objeto->getTipo() << ")\n";
    std::cout << "Volumen: " << objeto->volumen() << std::endl;
    std::cout << "Area: " << objeto->area() << std::endl;
    delete objeto;
}

void Gestionar::crearEsfera() {
    double radio = obtenerNumeroPositivo("Ingrese el radio de la esfera: ");
    Figura3d* objeto = new Esfera(radio);
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Figura: " << objeto->getNombre() << " (" << objeto->getTipo() << ")\n";
    std::cout << "Volumen: " << objeto->volumen() << std::endl;
    std::cout << "Area: " << objeto->area() << std::endl;
    delete objeto;
}

void Gestionar::crearCirculo() {
    double radio = obtenerNumeroPositivo("Ingrese el radio del circulo: ");
    Figura2d* objeto = new Circulo(radio);
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Figura: " << objeto->getNombre() << " (" << objeto->getTipo() << ")\n";
    std::cout << "Area: " << objeto->area() << std::endl;
    std::cout << "Perimetro: " << objeto->perimetro() << std::endl;
    delete objeto;
}

void Gestionar::crearCuadrado() {
    double lado = obtenerNumeroPositivo("Ingrese la longitud del lado del cuadrado: ");
    Figura2d* objeto = new Cuadrado(lado);
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Figura: " << objeto->getNombre() << " (" << objeto->getTipo() << ")\n";
    std::cout << "Area: " << objeto->area() << std::endl;
    std::cout << "Perimetro: " << objeto->perimetro() << std::endl;
    delete objeto;
}

bool Gestionar::procesarOpcion(const std::string& opcion) {
    if (opcion == "1")      crearCubo();
    else if (opcion == "2") crearEsfera();
    else if (opcion == "3") crearCirculo();
    else if (opcion == "4") crearCuadrado();
    else if (opcion == "5") {
        std::cout << "\nGracias por usar el programa!\nHasta luego!\n";
        return false;
    }
    return true;
}

void Gestionar::pausar() {
    std::cout << "\nPresiona Enter para continuar...";
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

void Gestionar::ejecutar() {
    std::cout << "Bienvenido al Gestor de Figuras Geometricas!\n";
    while (true) {
        mostrarMenu();
        std::string opcion = obtenerOpcion();
        bool continuar = procesarOpcion(opcion);
        if (!continuar) break;
        pausar();
    }
}
