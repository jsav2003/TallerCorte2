package org.example;

import java.util.Scanner;

/**
 * Clase para leer entrada del usuario.
 */
public class LectorEntrada {
    
    private Scanner scanner;

    /**
     * Constructor del lector de entrada.
     */
    public LectorEntrada() {
        this.scanner = new Scanner(System.in);
    }

    /**
     * Lee un número entero dentro de un rango.
     * @param mensaje mensaje a mostrar al usuario
     * @param minimo valor mínimo permitido
     * @param maximo valor máximo permitido
     * @return el entero leído
     */
    public int leerEntero(String mensaje, int minimo, int maximo) {
        int valor;
        do {
            System.out.print(mensaje);
            while (!scanner.hasNextInt()) {
                System.out.println("Por favor, ingrese un número entero válido.");
                System.out.print(mensaje);
                scanner.next();
            }
            valor = scanner.nextInt();
            if (valor < minimo || valor > maximo) {
                System.out.printf("El valor debe estar entre %d y %d.%n", minimo, maximo);
            }
        } while (valor < minimo || valor > maximo);
        
        return valor;
    }

    /**
     * Lee un número flotante mayor o igual al mínimo.
     * @param mensaje mensaje a mostrar al usuario
     * @param minimo valor mínimo permitido
     * @return el flotante leído
     */
    public double leerFlotante(String mensaje, double minimo) {
        double valor;
        do {
            System.out.print(mensaje);
            while (!scanner.hasNextDouble()) {
                System.out.println("Por favor, ingrese un número válido.");
                System.out.print(mensaje);
                scanner.next();
            }
            valor = scanner.nextDouble();
            if (valor < minimo) {
                System.out.printf("El valor debe ser mayor o igual a %.2f.%n", minimo);
            }
        } while (valor < minimo);
        
        return valor;
    }

    /**
     * Lee una cadena de texto.
     * @param mensaje mensaje a mostrar al usuario
     * @return la cadena leída
     */
    public String leerCadena(String mensaje) {
        System.out.print(mensaje);
        scanner.nextLine(); // Limpiar buffer
        return scanner.nextLine().trim();
    }

    /**
     * Solicita confirmación del usuario.
     * @param mensaje mensaje de confirmación
     * @return true si confirma, false en caso contrario
     */
    public boolean confirmarAccion(String mensaje) {
        System.out.print(mensaje + " (s/n): ");
        String respuesta = scanner.next().toLowerCase();
        return respuesta.equals("s") || respuesta.equals("si") || respuesta.equals("y") || respuesta.equals("yes");
    }
}
