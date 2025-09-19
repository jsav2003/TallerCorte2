package org.example;

import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

/**
 * Clase para manejar la entrada de datos del usuario
 */
public class LectorEntrada {
    
    private static final Scanner scanner = new Scanner(System.in);
    
    /**
     * Lee un número entero del usuario con validación
     * @param mensaje Mensaje a mostrar al usuario
     * @param minimo Valor mínimo permitido (null si no hay mínimo)
     * @param maximo Valor máximo permitido (null si no hay máximo)
     * @return Número entero válido ingresado por el usuario
     */
    public static int leerEntero(String mensaje, Integer minimo, Integer maximo) {
        while (true) {
            try {
                System.out.print(mensaje);
                int valor = scanner.nextInt();
                scanner.nextLine(); // Limpiar buffer
                
                if (minimo != null && valor < minimo) {
                    System.out.println("El valor debe ser mayor o igual a " + minimo);
                    continue;
                }
                
                if (maximo != null && valor > maximo) {
                    System.out.println("El valor debe ser menor o igual a " + maximo);
                    continue;
                }
                
                return valor;
                
            } catch (InputMismatchException e) {
                System.out.println("Por favor, ingrese un número entero válido.");
                scanner.nextLine(); // Limpiar buffer
            }
        }
    }
    
    /**
     * Lee un número flotante del usuario con validación
     * @param mensaje Mensaje a mostrar al usuario
     * @param minimo Valor mínimo permitido (null si no hay mínimo)
     * @return Número flotante válido ingresado por el usuario
     */
    public static double leerFlotante(String mensaje, Double minimo) {
        while (true) {
            try {
                System.out.print(mensaje);
                double valor = scanner.nextDouble();
                scanner.nextLine(); // Limpiar buffer
                
                if (minimo != null && valor < minimo) {
                    System.out.println("El valor debe ser mayor o igual a " + minimo);
                    continue;
                }
                
                return valor;
                
            } catch (InputMismatchException e) {
                System.out.println("Por favor, ingrese un número válido.");
                scanner.nextLine(); // Limpiar buffer
            }
        }
    }
    
    /**
     * Lee una cadena de texto del usuario
     * @param mensaje Mensaje a mostrar al usuario
     * @return Cadena ingresada por el usuario
     */
    public static String leerCadena(String mensaje) {
        while (true) {
            System.out.print(mensaje);
            String valor = scanner.nextLine().trim();
            if (!valor.isEmpty()) {
                return valor;
            }
            System.out.println("Por favor, ingrese un valor válido.");
        }
    }
    
    /**
     * Solicita confirmación del usuario (s/n)
     * @param mensaje Mensaje de confirmación
     * @return true si el usuario confirma, false en caso contrario
     */
    public static boolean confirmarAccion(String mensaje) {
        while (true) {
            System.out.print(mensaje + " (s/n): ");
            String respuesta = scanner.nextLine().trim().toLowerCase();
            
            if (respuesta.equals("s") || respuesta.equals("si") || respuesta.equals("sí") || 
                respuesta.equals("y") || respuesta.equals("yes")) {
                return true;
            } else if (respuesta.equals("n") || respuesta.equals("no")) {
                return false;
            } else {
                System.out.println("Por favor, responda 's' para sí o 'n' para no.");
            }
        }
    }
    
    /**
     * Permite al usuario seleccionar una opción de una lista
     * @param mensaje Mensaje a mostrar
     * @param opciones Lista de opciones disponibles
     * @return Índice de la opción seleccionada (base 0)
     */
    public static int seleccionarOpcion(String mensaje, List<String> opciones) {
        System.out.println(mensaje);
        for (int i = 0; i < opciones.size(); i++) {
            System.out.println((i + 1) + ". " + opciones.get(i));
        }
        
        while (true) {
            try {
                System.out.print("Seleccione una opción: ");
                int seleccion = scanner.nextInt();
                scanner.nextLine(); // Limpiar buffer
                
                if (seleccion >= 1 && seleccion <= opciones.size()) {
                    return seleccion - 1;
                } else {
                    System.out.println("Por favor, seleccione un número entre 1 y " + opciones.size());
                }
                
            } catch (InputMismatchException e) {
                System.out.println("Por favor, ingrese un número válido.");
                scanner.nextLine(); // Limpiar buffer
            }
        }
    }
}