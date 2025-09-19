package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Repositorio para gestionar la colección de figuras geométricas
 */
public class RepositorioFiguras {

    private final Map<Integer, Figura> figuras;
    private final String archivoPersistencia;
    private final boolean autoGuardar;

    /**
     * Constructor del repositorio
     * 
     * @param archivoPersistencia Archivo para persistencia de datos
     * @param autoGuardar         Si debe guardar automáticamente al modificar
     */
    public RepositorioFiguras(String archivoPersistencia, boolean autoGuardar) {
        this.figuras = new HashMap<>();
        this.archivoPersistencia = archivoPersistencia != null ? archivoPersistencia : "figuras.json";
        this.autoGuardar = autoGuardar;

        // Si el archivo no existe, crear uno vacío
        Path path = Paths.get(this.archivoPersistencia);
        if (Files.notExists(path)) {
            // Guardar lista vacía para inicializar el archivo
            PersistenciaArchivos.guardarEnArchivo(this.figuras, this.archivoPersistencia);
            //System.out.println("Archivo de persistencia creado: " + this.archivoPersistencia);
        } else {
            // Cargar datos existentes
            cargarFiguras();
        }
    }

    /**
     * Constructor por defecto
     */
    public RepositorioFiguras() {
        this("figuras.json", true);
    }

    /**
     * Almacena una figura en el repositorio
     * 
     * @param figura Figura a almacenar
     * @return ID de la figura almacenada
     */
    public int almacenarFigura(Figura figura) {
        if (figura == null) {
            throw new IllegalArgumentException("La figura no puede ser null");
        }
        int idFigura = figura.getId();
        this.figuras.put(idFigura, figura);
        System.out.println("Figura almacenada en memoria: ID " + idFigura);

        if (autoGuardar) {
            boolean ok = PersistenciaArchivos.guardarEnArchivo(this.figuras, archivoPersistencia);
            System.out.println("Guardado automático: " + (ok ? "éxito" : "falló"));
        }

        return idFigura;
    }

    /**
     * Obtiene una figura por su ID
     * 
     * @param figuraId ID de la figura a buscar
     * @return Figura encontrada o null
     */
    public Figura obtenerFigura(int figuraId) {
        return this.figuras.get(figuraId);
    }

    /**
     * Obtiene todas las figuras del repositorio
     * 
     * @return Lista de todas las figuras
     */
    public List<Figura> obtenerTodasFiguras() {
        return new ArrayList<>(this.figuras.values());
    }

    /**
     * Elimina una figura del repositorio
     * 
     * @param figuraId ID de la figura a eliminar
     * @return true si se eliminó, false si no existía
     */
    public boolean eliminarFigura(int figuraId) {
        boolean existia = this.figuras.containsKey(figuraId);
        if (existia) {
            this.figuras.remove(figuraId);
            System.out.println("Figura eliminada de memoria: ID=" + figuraId);
            if (autoGuardar) {
                boolean ok = PersistenciaArchivos.guardarEnArchivo(this.figuras, archivoPersistencia);
                System.out.println("Resultado guardado tras eliminación: " + ok);
            }
        }
        return existia;
    }

    /**
     * Cuenta el número total de figuras
     * 
     * @return Número de figuras en el repositorio
     */
    public int contarFiguras() {
        return this.figuras.size();
    }

    /**
     * Lista todas las figuras en el repositorio
     * 
     * @return Lista de todas las figuras almacenadas
     */
    public List<Figura> listarFiguras() {
        return new ArrayList<>(this.figuras.values());
    }

    /**
     * Busca figuras por tipo
     * 
     * @param tipo Tipo de figura a buscar
     * @return Lista de figuras del tipo especificado
     */
    public List<Figura> buscarPorTipo(String tipo) {
        String tipoLower = tipo.toLowerCase();
        return this.figuras.values().stream()
                .filter(figura -> figura.getNombre().toLowerCase().equals(tipoLower))
                .collect(Collectors.toList());
    }

    /**
     * Elimina todas las figuras del repositorio
     */
    public void limpiarRepositorio() {
        this.figuras.clear();
        GeneradorID.resetear();
        if (this.autoGuardar) {
            guardarFiguras();
        }
    }

    /**
     * Guarda las figuras en el archivo de persistencia
     * 
     * @return true si se guardó exitosamente
     */
    public boolean guardarFiguras() {
        return PersistenciaArchivos.guardarEnArchivo(this.figuras, this.archivoPersistencia);
    }

    /**
     * Carga las figuras desde el archivo de persistencia
     * 
     * @return true si se cargó exitosamente
     */
    public boolean cargarFiguras() {
        try {
            System.out.println("Invocando carga de figuras desde: " + archivoPersistencia);
            List<Figura> lista = PersistenciaArchivos.cargarDesdeArchivo(archivoPersistencia);
            for (Figura f : lista) {
                figuras.put(f.getId(), f);
            }
            System.out.println("Carga completa, total en memoria: " + figuras.size());
            return true;
        } catch (Exception e) {
            System.err.println("Error en cargarFiguras: " + e.getMessage());
            return false;
        }
    }

    /**
     * Obtiene estadísticas del repositorio
     * 
     * @return Mapa con estadísticas
     */
    public Map<String, Integer> obtenerEstadisticas() {
        Map<String, Integer> estadisticas = new HashMap<>();
        estadisticas.put("total", this.figuras.size());
        estadisticas.put("círculo", 0);
        estadisticas.put("cuadrado", 0);
        estadisticas.put("cubo", 0);
        estadisticas.put("esfera", 0);

        for (Figura figura : this.figuras.values()) {
            String nombre = figura.getNombre().toLowerCase();
            estadisticas.put(nombre, estadisticas.getOrDefault(nombre, 0) + 1);
        }

        return estadisticas;
    }

    /**
     * Obtiene el archivo de persistencia configurado
     * 
     * @return Ruta del archivo de persistencia
     */
    public String getArchivoPersistencia() {
        return this.archivoPersistencia;
    }

    /**
     * Indica si el auto guardado está habilitado
     * 
     * @return true si está habilitado el auto guardado
     */
    public boolean isAutoGuardar() {
        return this.autoGuardar;
    }
}