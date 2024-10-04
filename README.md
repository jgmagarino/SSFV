
---

# Aplicación para el Cálculo de Sistemas Solares Fotovoltaicos (SSFV)

> “La energía solar nos enseña que la naturaleza es nuestra aliada, y que podemos aprovechar sus recursos sin agotarlos.”

### Integrantes:
- **Jose Manuel Gomez Magariño**
- **Osbel Duardo Lopez**

---

## Índice
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Problema a Resolver](#problema-a-resolver)
3. [Objetivo de la Aplicación](#objetivo-de-la-aplicación)
4. [Funcionalidades Principales](#funcionalidades-principales)
5. [Tecnologías Utilizadas](#tecnologías-utilizadas)
6. [Instalación y Uso](#instalación-y-uso)
7. [Entidades del Sistema](#entidades-del-sistema)
8. [Diagramas](#diagramas)
9. [Pruebas y Validación](#pruebas-y-validación)
10. [Conclusiones y Recomendaciones Futuras](#conclusiones-y-recomendaciones-futuras)
11. [Bibliografía](#bibliografía)

---

## Descripción del Proyecto
La aplicación permite realizar cálculos detallados para el diseño de **Sistemas Solares Fotovoltaicos (SSFV)**, optimizando el tiempo y precisión en el proceso de análisis. Facilita la toma de decisiones sobre parámetros clave como el tipo de panel, la Hora Solar Pico (HSP) y la orientación de los paneles, generando informes útiles sobre energía, potencia y viabilidad económica del proyecto.

## Problema a Resolver
El desarrollo de un SSFV eficiente implica cálculos complejos que pueden consumir mucho tiempo. Esta aplicación soluciona este problema al automatizar los cálculos necesarios para un diseño eficiente, permitiendo a los usuarios enfocarse en la toma de decisiones estratégicas.

## Objetivo de la Aplicación
La herramienta permite realizar cálculos basados en:
- Tipo de panel solar.
- Hora Solar Pico (HSP) específica de la ubicación.
- Orientación y superficie disponible para la instalación.
  
Los resultados incluyen energía útil, potencia instalada, área ocupada y el número de paneles necesarios, además de facilitar un análisis económico de la inversión.

---

## Funcionalidades Principales
1. **Gestión de Entidades**: Registro y eliminación de paneles, HSP, tecnologías y sistemas solares.
2. **Cálculos Intuitivos**: Selección de parámetros con cálculos automáticos.
3. **Visualización Detallada**: Transparencia en el cálculo y presentación clara de resultados.

---

## Tecnologías Utilizadas
| Tecnología | Descripción |
|------------|-------------|
| **Python** | Lenguaje de programación utilizado para toda la lógica de la aplicación. |
| **SQLite** | Base de datos local para gestionar eficientemente la información del sistema. |
| **Flet**   | Framework multiplataforma que permite desarrollar aplicaciones móviles y de escritorio. |

---

## Instalación y Uso

### Requisitos Previos
- Python 3.x
- SQLite

### Instrucciones de Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/nombre-repositorio.git
   ```
2. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar la aplicación:
   ```bash
   python main.py
   ```

### Uso
1. Selecciona los parámetros de diseño (panel, HSP, orientación).
2. La aplicación generará automáticamente los cálculos.
3. Visualiza los resultados y el análisis económico.

---

## Entidades del Sistema

| Entidad | Atributos Clave |
|---------|-----------------|
| **Panel** | `id_panel`, `peack_power`, `cell_material`, `area`, `price`, `price_kwh_sen` |
| **HSP** | `place`, `value` |
| **Tecnología** | `material`, `surface` |
| **Sistema** | `name`, `panel_id`, `place`, `progress`, `description` |
| **Cálculo del Sistema** | `id_calc`, `system_name`, `useful_energy`, `number_panels`, `area`, `peak_power` |
| **Cálculo Económico** | `id_calc`, `system_name`, `cost`, `income`, `recovery_period` |

---

## Diagramas

- **Diagrama de Entidad-Relación**: Visualiza cómo se relacionan las entidades principales del sistema.
  
  ![Diagrama ER](path_to_image/diagrama_ER.png)

- **Diagrama de Clases**: Representa la estructura de las clases y sus interacciones.
  
  ![Diagrama de Clases](path_to_image/diagrama_clases.png)

- **Diagrama de Flujo**: Ilustra el flujo de cálculo dentro de la aplicación.
  
  ![Diagrama de Flujo](path_to_image/diagrama_flujo.png)

---

## Pruebas y Validación
Para validar la funcionalidad de la aplicación, se realizaron pruebas utilizando datos reales de paneles como el **Panel Hiku**. Se colaboró con el equipo del **CEMA** para verificar la precisión de los cálculos obtenidos.

---

## Conclusiones y Recomendaciones Futuras
La aplicación ha demostrado ser una herramienta eficiente para los cálculos necesarios en la creación de SSFV, permitiendo análisis precisos y rápidos.

### Recomendaciones Futuras:
1. **Exportación de Datos**: Añadir la opción de exportar a CSV o PDF.
2. **Compatibilidad con Otras Apps**: Integrar opciones para compartir resultados.
3. **Optimización de la Interfaz**: Mejorar la usabilidad y estética de la UI.
4. **Actualización Continua**: Incluir las últimas tendencias en energía solar.

---

## Bibliografía

- [Documentación SQLite](https://docs.python.org/3/library/sqlite3.html)
- [Documentación Flet](https://flet.dev/docs/)
- [Panel Hiku](https://efectosolar.es/tienda/paneles-solares/canadian-solar-450w-nueva-serie-hiku/)

---

### Mejoras en esta Versión del README:

1. **Tabla de Contenidos**: Facilita la navegación entre secciones.
2. **Tablas**: Claridad en la presentación de tecnologías y entidades.
3. **Imágenes**: Se pueden incluir diagramas que hagan el README más visual.
4. **Instrucciones de Instalación**: Facilita que otros desarrolladores puedan usar y probar la aplicación fácilmente.

¿Te gustaría implementar alguna de estas mejoras en tu README actual?
