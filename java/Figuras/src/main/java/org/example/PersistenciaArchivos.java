package org.example;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import java.io.IOException;
import java.lang.reflect.Type;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

public class PersistenciaArchivos {

    private static final Gson gson = new GsonBuilder().setPrettyPrinting().create();

    public static boolean guardarEnArchivo(Map<Integer, Figura> figuras, String archivo) {
        try {
            Path path = Paths.get(archivo);
            Path parent = path.getParent();
            if (parent != null && !Files.exists(parent)) {
                Files.createDirectories(parent);
            }
            //System.out.println("Guardando JSON en: " + path.toAbsolutePath());
            List<Map<String, Object>> datos = new ArrayList<>();
            for (Figura f : figuras.values()) {
                datos.add(figuraADict(f));
            }
            String json = gson.toJson(datos);
            Files.write(path, json.getBytes(StandardCharsets.UTF_8),
                        StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
            //System.out.println("JSON guardado correctamente.");
            return true;
        } catch (IOException e) {
            System.err.println("Error al guardar archivo: " + e.getMessage());
            return false;
        }
    }

    public static List<Figura> cargarDesdeArchivo(String archivo) {
        List<Figura> figuras = new ArrayList<>();
        Path path = Paths.get(archivo);
        System.out.println("Cargando JSON desde: " + path.toAbsolutePath());
        if (!Files.exists(path)) {
            System.out.println("Archivo no existe, devolviendo lista vacía.");
            return figuras;
        }
        try {
            String json = Files.readString(path, StandardCharsets.UTF_8);
            Type listType = new TypeToken<List<Map<String, Object>>>(){}.getType();
            List<Map<String, Object>> datosFiguras = gson.fromJson(json, listType);
            if (datosFiguras != null) {
                for (Map<String, Object> datos : datosFiguras) {
                    Figura f = dictAFigura(datos);
                    if (f != null) {
                        figuras.add(f);
                    }
                }
            }
            System.out.println("JSON cargado, figuras encontradas: " + figuras.size());
        } catch (IOException e) {
            System.err.println("Error al cargar archivo: " + e.getMessage());
        }
        return figuras;
    }

    // Helper: convierte Figura a mapa
    private static Map<String, Object> figuraADict(Figura figura) {
        Map<String, Object> datos = new HashMap<>();
        datos.put("id", figura.getId());
        datos.put("nombre", figura.getNombre());
        datos.put("tipo", figura.getTipo());
        if (figura instanceof Circulo) {
            datos.put("radio", ((Circulo) figura).getRadio());
        } else if (figura instanceof Cuadrado) {
            datos.put("lado", ((Cuadrado) figura).getLado());
        } else if (figura instanceof Cubo) {
            datos.put("lado", ((Cubo) figura).getLado());
        } else if (figura instanceof Esfera) {
            datos.put("radio", ((Esfera) figura).getRadio());
        }
        return datos;
    }

    // Helper: convierte mapa a Figura
    private static Figura dictAFigura(Map<String, Object> datos) {
        try {
            String nombre = datos.get("nombre").toString().toLowerCase();
            int id = ((Number) datos.get("id")).intValue();
            if (datos.containsKey("radio")) {
                double radio = ((Number) datos.get("radio")).doubleValue();
                if (nombre.equals("círculo")) {
                    return new Circulo(radio, id);
                } else if (nombre.equals("esfera")) {
                    return new Esfera(radio, id);
                }
            } else if (datos.containsKey("lado")) {
                double lado = ((Number) datos.get("lado")).doubleValue();
                if (nombre.equals("cuadrado")) {
                    return new Cuadrado(lado, id);
                } else if (nombre.equals("cubo")) {
                    return new Cubo(lado, id);
                }
            }
        } catch (Exception e) {
            System.err.println("Error al convertir datos a figura: " + e.getMessage());
        }
        return null;
    }
}
