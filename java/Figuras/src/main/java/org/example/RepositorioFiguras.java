package org.example;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Repositorio para gestionar la colección de figuras geométricas
 */
public class RepositorioFiguras {
    
    private final Map<Integer, Figura> figuras;
    private final String archivoPersistencia;
    private final PersistenciaArchivos persistencia;
    private final boolean autoGuardar;
    
    /**
     * Constructor del repositorio
     * @param archivoPersistencia Archivo para persistencia de datos
     * @param autoGuardar Si debe guardar automáticamente al modificar
     */
    public RepositorioFiguras(String archivoPersistencia, boolean autoGuardar) {
        this.figuras = new HashMap<>();
        this.archivoPersistencia = archivoPersistencia != null ? archivoPersistencia : "figuras.json";
        this.persistencia = new PersistenciaArchivos();
        this.autoGuardar = autoGuardar;
        
        // Cargar figuras existentes
        cargarFiguras();
    }
    
    /**
     * Constructor por defecto
     */
    public RepositorioFiguras() {
        this("figuras.json", true);
    }
    
    /**
     * Almacena una figura en el repositorio
     * @param figura Figura a almacenar
     * @return ID de la figura almacenada
     */
    public int almacenarFigura(Figura figura) {
        if (figura == null) {
            throw new IllegalArgumentException("La figura no puede ser null");
        }
        
        int idFigura = figura.getId();
        this.figuras.put(idFigura, figura);
        
        // Actualizar el generador de ID si es necesario
        GeneradorID.actualizarSiMayor(idFigura);
        
        if (this.autoGuardar) {
            guardarFiguras();
        }
        
        return idFigura;
    }
    
    /**
     * Obtiene una figura por su ID
     * @param figuraId ID de la figura a buscar
     * @return Figura encontrada o null
     */
    public Figura obtenerFigura(int figuraId) {
        return this.figuras.get(figuraId);
    }
    
    /**
     * Obtiene todas las figuras del repositorio
     * @return Lista de todas las figuras
     */
    public List<Figura> obtenerTodasFiguras() {
        return new ArrayList<>(this.figuras.values());
    }
    
    /**
     * Elimina una figura del repositorio
     * @param figuraId ID de la figura a eliminar
     * @return true si se eliminó, false si no existía
     */
    public boolean eliminarFigura(int figuraId) {
        boolean existia = this.figuras.containsKey(figuraId);
        if (existia) {
            this.figuras.remove(figuraId);
            if (this.autoGuardar) {
                guardarFiguras();
            }
        }
        return existia;
    }
    
    /**
     * Cuenta el número total de figuras
     * @return Número de figuras en el repositorio
     */
    public int contarFiguras() {
        return this.figuras.size();
    }
    
    /**
     * Lista todas las figuras en el repositorio
     * @return Lista de todas las figuras almacenadas
     */
    public List<Figura> listarFiguras() {
        return new ArrayList<>(this.figuras.values());
    }
    
    /**
     * Busca figuras por tipo
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
     * @return true si se guardó exitosamente
     */
    public boolean guardarFiguras() {
        return PersistenciaArchivos.guardarEnArchivo(this.figuras, this.archivoPersistencia);
    }
    
    /**
     * Carga las figuras desde el archivo de persistencia
     * @return true si se cargó exitosamente
     */
    public boolean cargarFiguras() {
        try {
            List<Figura> figurasCargadas = PersistenciaArchivos.cargarDesdeArchivo(this.archivoPersistencia);
            
            for (Figura figura : figurasCargadas) {
                this.figuras.put(figura.getId(), figura);
                GeneradorID.actualizarSiMayor(figura.getId());
            }
            
            return true;
            
        } catch (Exception e) {
            System.err.println("Error al cargar figuras: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * Obtiene estadísticas del repositorio
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
     * @return Ruta del archivo de persistencia
     */
    public String getArchivoPersistencia() {
        return this.archivoPersistencia;
    }
    
    /**
     * Indica si el auto guardado está habilitado
     * @return true si está habilitado el auto guardado
     */
    public boolean isAutoGuardar() {
        return this.autoGuardar;
    }
}