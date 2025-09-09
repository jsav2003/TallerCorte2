"""
MÃ³dulo para el repositorio de figuras - manejo de almacenamiento y persistencia.
"""
import os
from typing import List, Optional, Dict, Any
from figura import Figura
from serializador_figuras import PersistenciaArchivos

class RepositorioFiguras:
    """
    Repositorio para manejo de figuras geomÃ©tricas en memoria y persistencia.
    """

    def __init__(self, archivo_persistencia: str = "figuras.json", auto_guardar: bool = True):
        """
        Inicializa el repositorio.

        Args:
            archivo_persistencia (str): Nombre del archivo para persistencia
            auto_guardar (bool): Si debe guardar automÃ¡ticamente los cambios
        """
        self.figuras: Dict[int, Any] = {}  # Diccionario de figuras por ID

        # Asegurar que el archivo se cree en el mismo directorio que este script
        if not os.path.isabs(archivo_persistencia):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.archivo_persistencia = os.path.join(script_dir, archivo_persistencia)
        else:
            self.archivo_persistencia = archivo_persistencia

        self.persistencia = PersistenciaArchivos()
        self.auto_guardar = auto_guardar
        self.cargar_figuras()

    def _auto_guardar_si_habilitado(self):
        """Guarda automÃ¡ticamente si estÃ¡ habilitado el auto-guardado."""
        if self.auto_guardar:
            try:
                self.guardar_figuras()
            except Exception:
                # Si hay error en el auto-guardado, no interrumpir la operaciÃ³n
                pass

    def almacenar_figura(self, figura) -> int:
        """
        Almacena una figura en el repositorio.

        Args:
            figura: Instancia de figura geomÃ©trica

        Returns:
            int: ID de la figura almacenada
        """
        if not isinstance(figura, Figura):
            raise ValueError("El objeto debe ser una instancia de Figura")

        figura_id = figura.get_id()
        self.figuras[figura_id] = figura
        self._auto_guardar_si_habilitado()  # Guardar automÃ¡ticamente
        return figura_id

    def obtener_figura(self, figura_id: int):
        """
        Obtiene una figura por su ID.

        Args:
            figura_id (int): ID de la figura

        Returns:
            Figura o None: La figura si existe, None en caso contrario
        """
        return self.figuras.get(figura_id)

    def obtener_todas_figuras(self) -> List:
        """
        Obtiene todas las figuras almacenadas.

        Returns:
            List: Lista con todas las figuras
        """
        return list(self.figuras.values())

    def eliminar_figura(self, figura_id: int) -> bool:
        """
        Elimina una figura del repositorio.

        Args:
            figura_id (int): ID de la figura a eliminar

        Returns:
            bool: True si se eliminÃ³, False si no existÃ­a
        """
        if figura_id in self.figuras:
            del self.figuras[figura_id]
            self._auto_guardar_si_habilitado()  # Guardar automÃ¡ticamente
            return True
        return False

    def contar_figuras(self) -> int:
        """
        Cuenta el nÃºmero de figuras almacenadas.

        Returns:
            int: NÃºmero de figuras
        """
        return len(self.figuras)

    def buscar_por_tipo(self, tipo_figura: str) -> List:
        """
        Busca figuras por tipo.

        Args:
            tipo_figura (str): Tipo de figura a buscar

        Returns:
            List: Lista de figuras del tipo especificado
        """
        tipo_figura = tipo_figura.lower()
        figuras_encontradas = []

        for figura in self.figuras.values():
            if figura.get_nombre().lower() == tipo_figura:
                figuras_encontradas.append(figura)

        return figuras_encontradas

    def limpiar_repositorio(self):
        """Elimina todas las figuras del repositorio."""
        self.figuras.clear()
        # Reiniciar el generador de IDs
        from generador_id import GeneradorID
        generador = GeneradorID()
        generador.reiniciar_contador()
        self._auto_guardar_si_habilitado()  # Guardar automÃ¡ticamente

    def guardar_figuras(self) -> bool:
        """
        Guarda todas las figuras en el archivo de persistencia.

        Returns:
            bool: True si se guardÃ³ exitosamente
        """
        figuras_lista = list(self.figuras.values())
        return self.persistencia.guardar_figuras_archivo(figuras_lista, self.archivo_persistencia)

    def cargar_figuras(self) -> bool:
        """
        Carga figuras desde el archivo de persistencia.

        Returns:
            bool: True si se cargÃ³ exitosamente
        """
        figuras, exito = self.persistencia.cargar_figuras_archivo(self.archivo_persistencia)

        if exito:
            # Limpiar repositorio actual
            self.figuras.clear()

            # Cargar nuevas figuras
            for figura in figuras:
                self.figuras[figura.get_id()] = figura

        return exito

    def obtener_estadisticas(self) -> Dict[str, Any]:
        """
        Obtiene estadÃ­sticas del repositorio.

        Returns:
            Dict: EstadÃ­sticas del repositorio
        """
        # Contar figuras por tipo
        figuras_por_tipo = {}
        area_total_2d = 0.0
        volumen_total_3d = 0.0
        perimetro_total_2d = 0.0
        count_2d = 0
        count_3d = 0

        for figura in self.figuras.values():
            tipo = figura.get_nombre()
            figuras_por_tipo[tipo] = figuras_por_tipo.get(tipo, 0) + 1

            # Calcular mÃ©tricas
            if hasattr(figura, 'calcular_area'):
                area_total_2d += figura.calcular_area()
                count_2d += 1
            if hasattr(figura, 'calcular_volumen'):
                volumen_total_3d += figura.calcular_volumen()
                count_3d += 1
            if hasattr(figura, 'calcular_perimetro'):
                perimetro_total_2d += figura.calcular_perimetro()

        estadisticas = {
            'total_figuras': len(self.figuras),
            'tipos_unicos': len(figuras_por_tipo),
            'figuras_por_tipo': figuras_por_tipo,
            'area_total_2d': area_total_2d,
            'volumen_total_3d': volumen_total_3d,
            'perimetro_total_2d': perimetro_total_2d,
            'area_promedio_2d': area_total_2d / count_2d if count_2d > 0 else 0,
            'volumen_promedio_3d': volumen_total_3d / count_3d if count_3d > 0 else 0,
            'perimetro_promedio_2d': perimetro_total_2d / count_2d if count_2d > 0 else 0,
            'ids_disponibles': list(self.figuras.keys()),
            'archivo_persistencia': self.archivo_persistencia,
            'archivo_existe': self.persistencia.archivo_existe(self.archivo_persistencia)
        }

        return estadisticas

    def guardar_en_archivo(self, nombre_archivo: str) -> bool:
        """
        Guarda las figuras en un archivo especÃ­fico.

        Args:
            nombre_archivo (str): Nombre del archivo

        Returns:
            bool: True si se guardÃ³ exitosamente
        """
        try:
            # Asegurar que el archivo se guarde en el directorio correcto
            if not os.path.isabs(nombre_archivo):
                script_dir = os.path.dirname(os.path.abspath(__file__))
                ruta_completa = os.path.join(script_dir, nombre_archivo)
            else:
                ruta_completa = nombre_archivo

            return self.persistencia.guardar_figuras_archivo(list(self.figuras.values()), ruta_completa)
        except Exception:
            return False

    def cargar_desde_archivo(self, nombre_archivo: str) -> int:
        """
        Carga figuras desde un archivo especÃ­fico.

        Args:
            nombre_archivo (str): Nombre del archivo

        Returns:
            int: NÃºmero de figuras cargadas
        """
        try:
            # Asegurar que cargamos desde el directorio correcto
            if not os.path.isabs(nombre_archivo):
                script_dir = os.path.dirname(os.path.abspath(__file__))
                ruta_completa = os.path.join(script_dir, nombre_archivo)
            else:
                ruta_completa = nombre_archivo

            figuras_cargadas, exito = self.persistencia.cargar_figuras_archivo(ruta_completa)
            if exito and figuras_cargadas:
                for figura in figuras_cargadas:
                    self.figuras[figura.get_id()] = figura
                self._auto_guardar_si_habilitado()  # Guardar automÃ¡ticamente
                return len(figuras_cargadas)
            return 0
        except Exception:
            return 0

    def limpiar(self) -> None:
        """Limpia todas las figuras del repositorio."""
        self.figuras.clear()
        # Reiniciar el generador de IDs
        from generador_id import GeneradorID
        generador = GeneradorID()
        generador.reiniciar_contador()
        self._auto_guardar_si_habilitado()  # Guardar automÃ¡ticamente
