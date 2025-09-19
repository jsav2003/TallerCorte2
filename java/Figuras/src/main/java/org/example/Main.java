package org.example;

/**
 * Módulo principal del programa - Punto de entrada
 */
public class Main {
    
    /**
     * Método principal para iniciar la aplicación
     * @param args Argumentos de línea de comandos
     */
    public static void main(String[] args) {
        Gestionar gestor = new Gestionar();
        gestor.ejecutar();
    }
}