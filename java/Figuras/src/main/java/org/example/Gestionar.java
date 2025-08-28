package org.example;

import java.util.Scanner;

public class Gestionar {

    private final Scanner scanner;

    public Gestionar() {
        scanner = new Scanner(System.in);
    }

    public void mostrarMenu() {
        System.out.println("\n========================================");
        System.out.println("    GESTOR DE FIGURAS GEOMÉTRICAS");
        System.out.println("========================================");
        System.out.println("1. Crear Cubo");
        System.out.println("2. Crear Esfera");
        System.out.println("3. Crear Círculo");
        System.out.println("4. Crear Cuadrado");
        System.out.println("5. Salir");
        System.out.println("----------------------------------------");
    }

    public String obtenerOpcion() {

        while (true) {

            System.out.print("Seleccione una opción (1-5): ");
            String opcion = scanner.nextLine();
            if (opcion.matches("[1-5]")) {
                return opcion;
            } else {
                System.out.println("❌ Error: Ingrese una opción válida (1-5)");
            }
        }
    }

    public Double obtenerNumeroPositivo(String mensaje) {

        while (true) {
            System.out.print(mensaje);
            try {
                double valor = Double.parseDouble(scanner.nextLine());
                if (valor > 0) {
                    return valor;
                } else {
                    System.out.println("❌ Error: El valor debe ser mayor que 0");
                }
            } catch (NumberFormatException e) {
                System.out.println("❌ Error: Ingrese un número válido");
            }
        }
    }

    public void crearCubo() {
        Double lado = obtenerNumeroPositivo("Ingrese la longitud del lado del cubo: ");
        if (lado != null) {
            Cubo cubo = new Cubo(lado);
            System.out.printf("✓ Volumen del cubo: %.2f unidades³%n", cubo.calcularVolumen());
        }
    }

    public void crearEsfera() {
        Double radio = obtenerNumeroPositivo("Ingrese el radio de la esfera: ");
        if (radio != null) {
            Esfera esfera = new Esfera(radio);
            System.out.printf("✓ Volumen de la esfera: %.2f unidades³%n", esfera.calcularVolumen());
        }
    }

    public void crearCirculo() {
        Double radio = obtenerNumeroPositivo("Ingrese el radio del círculo: ");
        if (radio != null) {
            Circulo circulo = new Circulo(radio);
            System.out.printf("✓ Área del círculo: %.2f unidades²%n", circulo.calcularArea());
            System.out.printf("✓ Perímetro del círculo: %.2f unidades%n", circulo.calcularPerimetro());
        }
    }

    public void crearCuadrado() {
        Double lado = obtenerNumeroPositivo("Ingrese la longitud del lado del cuadrado: ");
        if (lado != null) {
            Cuadrado cuadrado = new Cuadrado(lado);
            System.out.printf("✓ Área del cuadrado: %.2f unidades²%n", cuadrado.calcularArea());
            System.out.printf("✓ Perímetro del cuadrado: %.2f unidades%n", cuadrado.calcularPerimetro());
        }
    }

    public boolean procesarOpcion(String opcion) {

        switch (opcion) {

            case "1":
                crearCubo();
                break;
            case "2":
                crearEsfera();
                break;
            case "3":
                crearCirculo();
                break;
            case "4":
                crearCuadrado();
                break;
            case "5":
                System.out.println("\n¡Gracias por usar el programa!");
                System.out.println("¡Hasta luego! 👋");
                return false;
        }
        return true;
    }

    public void pausar() {
        System.out.print("\nPresiona Enter para continuar...");
        scanner.nextLine();
    }

    public void ejecutar() {

        System.out.println("¡Bienvenido al Gestor de Figuras Geométricas!");

        while (true) {

            mostrarMenu();

            String opcion = obtenerOpcion();

            boolean continuar = procesarOpcion(opcion);

            if (!continuar) {
                break;
            }
            pausar();
        }
    }
}