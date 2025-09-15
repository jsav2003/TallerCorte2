package org.example;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Repositorio para almacenar y gestionar figuras geométricas.
 */
public class RepositorioFiguras {
    
    private Map<Integer, Figura> figuras;
    private String archivoPersistencia;
    private PersistenciaArchivos persistencia;
    private boolean autoGuardar;

    /**
     * Constructor del repositorio de figuras.
     * @param archivoPersistencia ruta del archivo para persistencia
     * @param autoGuardar indica si debe guardar automáticamente
     */
    public RepositorioFiguras(String archivoPersistencia, boolean autoGuardar) {
        this.figuras = new HashMap<>();
        this.archivoPersistencia = archivoPersistencia;
        this.persistencia = new PersistenciaArchivos();
        this.autoGuardar = autoGuardar;
        cargarFiguras();
    }

    /**
     * Almacena una figura en el repositorio.
     * @param figura la figura a almacenar
     * @return el ID de la figura almacenada
     */
    public int almacenarFigura(Figura figura) {
        if (figura == null) {
            throw new IllegalArgumentException("La figura no puede ser nula");
        }
        
        figuras.put(figura.getId(), figura);
        
        if (autoGuardar) {
            guardarFiguras();
        }
        
        return figura.getId();
    }

    /**
     * Obtiene una figura por su ID.
     * @param figuraId el ID de la figura
     * @return la figura encontrada o null si no existe
     */
    public Figura obtenerFigura(int figuraId) {
        return figuras.get(figuraId);
    }

    /**
     * Obtiene todas las figuras del repositorio.
     * @return lista con todas las figuras
     */
    public List<Figura> obtenerTodasFiguras() {
        return new ArrayList<>(figuras.values());
    }

    /**
     * Elimina una figura del repositorio.
     * @param figuraId el ID de la figura a eliminar
     * @return true si se eliminó exitosamente, false en caso contrario
     */
    public boolean eliminarFigura(int figuraId) {
        boolean eliminado = figuras.remove(figuraId) != null;
        
        if (eliminado && autoGuardar) {
            guardarFiguras();
        }
        
        return eliminado;
    }

    /**
     * Cuenta el número total de figuras.
     * @return el número de figuras en el repositorio
     */
    public int contarFiguras() {
        return figuras.size();
    }

    /**
     * Busca figuras por tipo.
     * @param tipo el tipo de figura a buscar
     * @return lista de figuras del tipo especificado
     */
    public List<Figura> buscarPorTipo(String tipo) {
        return figuras.values().stream()
                .filter(figura -> figura.getTipo().equalsIgnoreCase(tipo))
                .collect(Collectors.toList());
    }

    /**
     * Limpia el repositorio eliminando todas las figuras.
     */
    public void limpiarRepositorio() {
        figuras.clear();
        
        if (autoGuardar) {
            guardarFiguras();
        }
    }

    /**
     * Guarda las figuras en el archivo de persistencia.
     * @return true si se guardó exitosamente, false en caso contrario
     */
    public boolean guardarFiguras() {
        try {
            return persistencia.guardarEnArchivo(new ArrayList<>(figuras.values()), archivoPersistencia);
        } catch (Exception e) {
            System.err.println("Error al guardar figuras: " + e.getMessage());
            return false;
        }
    }

    /**
     * Carga las figuras desde el archivo de persistencia.
     * @return true si se cargó exitosamente, false en caso contrario
     */
    public boolean cargarFiguras() {
        try {
            List<Figura> figurasComputadas = persistencia.cargarDesdeArchivo(archivoPersistencia);
            if (figurasComputadas != null) {
                figuras.clear();
                for (Figura figura : figurasComputadas) {
                    figuras.put(figura.getId(), figura);
                    GeneradorID.getInstance().actualizarSiMayor(figura.getId());
                }
                return true;
            }
        } catch (Exception e) {
            System.err.println("Error al cargar figuras: " + e.getMessage());
        }
        return false;
    }
}
