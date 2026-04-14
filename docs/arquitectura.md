# Arquitectura del NCT Visual Engine

## Visión General

El motor está diseñado como un sistema de generación y visualización de ecuaciones cuaternarias emergentes, organizado en capas funcionales independientes.

```
┌─────────────────────────────────────────┐
│           CAPA DE PRESENTACIÓN           │
│  - Matriz ASCII 21×21                   │
│  - Curva de frontera crítica            │
│  - Logs de consola                      │
├─────────────────────────────────────────┤
│           CAPA DE PROCESAMIENTO          │
│  - Generador de ecuaciones NCT          │
│  - Algoritmo de suavizado no lineal     │
│  - Normalización de valores             │
├─────────────────────────────────────────┤
│           CAPA DE ALMACENAMIENTO       │
│  - Exportación JSON                     │
│  - Exportación LinkedIn (txt)           │
│  - Historial de iteraciones             │
├─────────────────────────────────────────┤
│           CAPA DE DATOS                  │
│  - Estados C0, C1, C2, C3               │
│  - Operadores ⊕, ⊗, +, −                │
│  - Coeficientes aleatorios              │
└─────────────────────────────────────────┘
```

---

## Componentes Principales

### 1. Generador de Ecuaciones (`generate_equation`)

**Propósito:** Crear ecuaciones cuaternarias sintácticamente válidas.

**Estrategia:**
- Selección aleatoria de coeficientes (rango -3 a 3)
- Selección aleatoria de estados C0–C3
- Combinación de operadores mixtos (⊕, ⊗ para NCT; +, − para lineal)

**Formato de salida:**
```
E = {coef1}·{estado1} {op1} ({coef2} − {estado2}) {op2} {coef3}·{estado3}
```

**Ejemplo:**
```
E = 2.802·C0 ⊗ (2.918 − C2) + -0.686·C0
```

---

### 2. Motor de Visualización ASCII (`ascii_matrix`)

**Propósito:** Generar representaciones visuales del estado del sistema.

**Algoritmo:**
1. Inicializar generador de números aleatorios con semilla derivada del estado
2. Crear matriz 21×21 con distribución normal
3. Escalar valores al rango de caracteres ASCII
4. Mapear a gradiente visual: ` .:-=+*#%@`

**Gradiente de intensidad:**
```
Espacio  →  Punto  →  Dos puntos  →  Guion  →  Igual  →  Más  →  Asterisco  →  #  →  %  →  @
 (bajo)                                                       (alto)
```

---

### 3. Analizador de Frontera Crítica (`frontier_curve`)

**Propósito:** Detectar transiciones de fase en la evolución del sistema.

**Método:**
- Extrae valores de iteraciones históricas
- Aplica suavizado no lineal mediante `tanh()`
- Normaliza por desviación estándar

**Fórmula:**
```python
smooth = np.tanh(arr / np.std(arr))
```

**Interpretación:**
- Valores cercanos a +1.0: Estado de alta energía/emergencia
- Valores cercanos a -1.0: Estado de baja energía/colapso
- Valores cercanos a 0.0: Estado de equilibrio/frontera crítica

---

### 4. Sistema de Exportación

#### Exportador JSON (`save_json`)
- **Formato:** Estructura jerárquica con metadatos
- **Campos:** iteración, ecuación, valor, timestamp
- **Uso:** Análisis de datos, procesamiento posterior

#### Exportador LinkedIn (`linkedin_export`)
- **Formato:** Texto plano con formato académico
- **Audiencia:** Divulgación científica en redes
- **Contenido:** Encabezado formal + listado de ecuaciones

---

## Flujo de Datos

```
┌─────────────┐
│   Inicio    │
└──────┬──────┘
       │
       ▼
┌─────────────────┐     ┌─────────────────┐
│  Generar eq.    │────▶│  Almacenar en   │
│  (40 iteraciones)│     │  history[]      │
└─────────────────┘     └────────┬────────┘
                                 │
       ┌─────────────────────────┼─────────────────────────┐
       │                         │                         │
       ▼                         ▼                         ▼
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│    JSON     │         │    ASCII    │         │   LinkedIn  │
│   Export    │         │   Matrix    │         │   Export    │
└─────────────┘         └─────────────┘         └─────────────┘
       │                         │                         │
       └─────────────────────────┼─────────────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────┐
                    │  Frontier Curve     │
                    │  (Frontera crítica) │
                    └─────────────────────┘
```

---

## Estados Cuánticos (C0–C3)

| Estado | Significado | Rol en el sistema |
|--------|-------------|-------------------|
| C0 | **Vacío / Potencial** | Estado base, punto de partida |
| C1 | **Activación** | Transición inicial, energía emergente |
| C2 | **Resonancia** | Estado estable, oscilación sostenida |
| C3 | **Colapso / Emergencia** | Estado final, transición de fase |

**Propiedad fundamental:** El sistema evoluciona entre estos estados sin seguir una secuencia temporal lineal predeterminada.

---

## Operadores Matemáticos

| Operador | Tipo | Semántica NCT |
|----------|------|---------------|
| `⊕` | Cuaternario | Suma no conmutativa, preserva fase |
| `⊗` | Cuaternario | Producto tensorial, acoplamiento de estados |
| `+` | Lineal | Suma estándar (interoperabilidad) |
| `−` | Lineal | Resta estándar (interoperabilidad) |

---

## Consideraciones de Diseño

### 1. No linealidad intencional
El motor no sigue una ecuación diferencial ni una secuencia causal. Cada iteración es un estado válido por sí mismo.

### 2. Emergencia vs. Causación
Las geometrías emergentes no son "resultado" de las ecuaciones previas, sino manifestaciones del estado actual del sistema.

### 3. Separación de concerns
- Generación de datos ≠ Visualización
- Procesamiento interno ≠ Exportación externa
- Estado transitorio ≠ Historial persistente

### 4. Extensibilidad
La arquitectura permite añadir nuevos exportadores, visualizaciones o estados cuánticos sin modificar el núcleo.

---

## Diagrama de Secuencia

```
Usuario          Main Loop        Generator       Visualizer      Exporter
  │                │                │               │              │
  │──ejecutar()──▶│                │               │              │
  │                │──inicializar──▶│               │              │
  │                │                │               │              │
  │                │◀──equation────│               │              │
  │                │  (40 veces)    │               │              │
  │                │                │               │              │
  │                │────────────────┼──────────────▶│              │
  │                │                │               │──generar──▶│
  │                │                │               │   ASCII      │
  │                │                │               │◀───────────│
  │                │                │               │              │
  │                │────────────────┼───────────────┼────────────▶│
  │                │                │               │  exportar    │
  │                │                │               │  JSON/TXT    │
  │                │                │               │              │
  │                │──calcular────▶│               │              │
  │                │  frontera      │               │              │
  │                │                │               │              │
  │◀──resultado───│                │               │              │
```
