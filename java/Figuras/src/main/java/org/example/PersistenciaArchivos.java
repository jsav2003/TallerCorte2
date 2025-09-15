package org.example;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Clase para manejar la persistencia de figuras en archivos.
 */
public class PersistenciaArchivos {

    /**
     * Guarda una lista de figuras en un archivo.
     * @param figuras lista de figuras a guardar
     * @param archivo ruta del archivo donde guardar
     * @return true si se guardó exitosamente, false en caso contrario
     */
    public boolean guardarEnArchivo(List<Figura> figuras, String archivo) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(archivo))) {
            oos.writeObject(figuras);
            return true;
        } catch (IOException e) {
            System.err.println("Error al guardar en archivo: " + e.getMessage());
            return false;
        }
    }

    /**
     * Carga una lista de figuras desde un archivo.
     * @param archivo ruta del archivo desde donde cargar
     * @return lista de figuras cargadas o null si hay error
     */
    @SuppressWarnings("unchecked")
    public List<Figura> cargarDesdeArchivo(String archivo) {
        File file = new File(archivo);
        if (!file.exists()) {
            return new ArrayList<>();
        }

        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(archivo))) {
            return (List<Figura>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Error al cargar desde archivo: " + e.getMessage());
            return new ArrayList<>();
        }
    }
}
