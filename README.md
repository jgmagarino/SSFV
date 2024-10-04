Aplicación para el Cálculo de Sistemas Solares Fotovoltaicos (SSFV)
“La energía solar nos enseña que la naturaleza es nuestra aliada, y que podemos aprovechar sus recursos sin agotarlos.”

Integrantes
Jose Manuel Gomez Magariño
Osbel Duardo Lopez
Problematica
El desarrollo de un Sistema Solar Fotovoltaico (SSFV) eficiente requiere múltiples cálculos que pueden ser complejos y consumir tiempo. Esta aplicación busca optimizar ese proceso, permitiendo realizar cálculos de manera rápida y precisa para facilitar la toma de decisiones sobre los parámetros del diseño de un SSFV.

Objetivo
La aplicación está diseñada para ayudar en el cálculo y análisis de los aspectos clave en la creación de un SSFV, tales como:

Tipo de Panel: Selección adecuada del panel solar.
Hora Solar Pico (HSP): Consideración de la HSP específica del lugar.
Orientación de los Paneles: Determinación de la mejor orientación.
Potencia y Área Disponibles: Evaluación de la potencia a instalar y el área disponible.
A partir de estos datos, la aplicación proporciona información clave como energía útil, potencia del sistema, área ocupada y número de paneles requeridos. Esto permite realizar análisis económicos y evaluar la viabilidad del proyecto.

Público Objetivo
La aplicación está dirigida a investigadores y profesionales del Centro de Estudios Medio-Ambientales (CEMA), quienes necesitan herramientas eficientes para el análisis y diseño de sistemas solares.

Justificación para el Desarrollo de una APK
El desarrollo de una aplicación móvil responde a la necesidad de accesibilidad y facilidad de uso en cualquier momento y lugar, permitiendo a los usuarios realizar cálculos complejos de forma intuitiva y mejorando la eficiencia en la toma de decisiones.

Funcionalidades de la APK
Gestión de Entidades: Registro y eliminación de Paneles, HSP, Tecnologías y Sistemas.
Cálculos Intuitivos: Interfaz simple para seleccionar parámetros, con cálculos automáticos.
Visualización de Cálculos: Detalle del proceso de cálculo para mayor transparencia y comprensión.
Tecnologías Utilizadas
Python: Utilizado por su facilidad de uso y su amplio ecosistema de librerías.
SQLite: Base de datos local para gestionar eficientemente la información.
Flet: Framework multiplataforma para el desarrollo de aplicaciones móviles, con posible expansión a escritorio y web.
Entidades del Sistema
Panel
id_panel: Identificador único.
peack_power: Potencia pico (W).
cell_material: Material de las celdas.
area: Área ocupada (m²).
price: Precio del panel (cup).
price_kwh_sen: Ganancia por kWh (cup).
HSP (Hora Solar Pico)
place: Ubicación de la HSP registrada.
value: Valor de la HSP.
Tecnología
material: Material de las celdas.
surface: Superficie requerida para generar un W.
Sistema
name: Nombre del sistema.
panel_id: Tipo de panel utilizado.
place: Lugar de construcción.
progress: Progreso de la construcción.
description: Descripción opcional.
Cálculo del Sistema
id_calc: Identificador único del cálculo.
system_name: Nombre del sistema asociado.
useful_energy: Energía útil.
number_panels: Número de paneles.
area: Área ocupada (m²).
peak_power: Potencia pico del sistema.
Cálculo Económico
id_calc: Identificador único del cálculo.
system_name: Nombre del sistema.
cost: Costo total del sistema.
income: Ingresos generados.
recovery_period: Período de recuperación (años).
Diagramas
Diagrama de Entidad-Relación: Muestra la estructura de la base de datos y las relaciones entre las entidades.
Diagrama de Clases: Presenta las clases utilizadas, incluyendo sus atributos y métodos.
Diagrama de Flujo: Representa el proceso de cálculo y cómo se transforman las entradas en los resultados finales.
Proceso de Desarrollo
Inicialmente, se consideró el uso de archivos JSON, pero se optó por SQLite para garantizar una mejor integridad y organización de los datos. Además, se aplicaron principios de programación orientada a objetos y el uso del patrón Singleton para el manejo eficiente de instancias.

Pruebas y Validación
Se realizaron pruebas con datos reales (como los paneles Hiku) y en colaboración con el equipo de CEMA, se verificaron los cálculos, logrando resultados precisos y satisfactorios.

Conclusiones
Se desarrolló una APK ligera y funcional que facilita la construcción de sistemas solares fotovoltaicos. En futuras versiones, se planean nuevas funcionalidades como la exportación de datos y la compatibilidad con otras aplicaciones.

Recomendaciones Futuras
Implementar funcionalidades adicionales:

Exportación de datos a formatos como CSV o PDF.
Compartir resultados a través de redes sociales o correo electrónico.
Optimización de la Interfaz:

Mejora de la experiencia del usuario con una interfaz más atractiva.
Actualización continua:

Mantener la aplicación actualizada con los últimos avances en energía solar.
Bibliografía
Documentación SQLite: https://docs.python.org/3/library/sqlite3.html
Documentación Flet: https://flet.dev/docs/
Panel Hiku: https://efectosolar.es/tienda/paneles-solares/canadian-solar-450w-nueva-serie-hiku/
