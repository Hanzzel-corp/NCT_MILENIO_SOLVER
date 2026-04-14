# Referencia API - NCT Visual Engine

## Módulos y Funciones

---

## `generate_equation()`

Genera una ecuación cuaternaria sintácticamente válida en formato NCT.

**Firma:**
```python
def generate_equation() -> str
```

**Retorna:** `str` - Ecuación formateada

**Formato de salida:**
```
E = {coeficiente}·{estado} {operador} ({coeficiente} − {estado}) {operador} {coeficiente}·{estado}
```

**Ejemplo:**
```python
>>> generate_equation()
'E = 2.345·C1 ⊗ (-1.234 − C0) ⊕ 0.987·C2'
```

**Parámetros internos:**

| Variable | Rango | Descripción |
|----------|-------|-------------|
| `a, b, c` | [-3.0, 3.0] | Coeficientes numéricos |
| `x, y, z` | C0, C1, C2, C3 | Estados cuánticos |
| `op1, op2` | ⊕, ⊗, +, − | Operadores matemáticos |

---

## `ascii_matrix(seed_val)`

Genera una matriz visual ASCII 21×21 representando el estado del sistema.

**Firma:**
```python
def ascii_matrix(seed_val: int) -> str
```

**Parámetros:**
- `seed_val` (`int`): Semilla para el generador de números aleatorios

**Retorna:** `str` - Matriz formateada con caracteres ASCII

**Ejemplo:**
```python
>>> ascii_matrix(123)
' .:-=+*#%@...\n...#%@+:...\n...etc'
```

**Gradiente de caracteres:**
```python
chars = " .:-=+*#%@"
# 0 = espacio (valor mínimo)
# 9 = @ (valor máximo)
```

**Algoritmo:**
1. Fijar semilla con `np.random.seed(seed_val)`
2. Generar matriz 21×21 con distribución normal
3. Normalizar al rango [0, 9]
4. Mapear a caracteres ASCII

---

## `frontier_curve(history)`

Calcula la curva de frontera crítica a partir del historial de iteraciones.

**Firma:**
```python
def frontier_curve(history: list[dict]) -> str
```

**Parámetros:**
- `history` (`list[dict]`): Lista de diccionarios con clave `"val"`

**Retorna:** `str` - Serie de valores suavizados formateados

**Ejemplo:**
```python
>>> history = [{"val": 1.5}, {"val": -0.5}, {"val": 2.0}]
>>> frontier_curve(history)
'+0.91 -0.46 +0.96'
```

**Procesamiento:**
```python
# 1. Extraer valores
values = [h["val"] for h in history]

# 2. Convertir a array NumPy
arr = np.array(values)

# 3. Suavizado no lineal con tangente hiperbólica
smooth = np.tanh(arr / np.std(arr))

# 4. Formatear a 2 decimales con signo
" ".join(f"{v:+.2f}" for v in smooth)
```

---

## `save_json(history, filename)`

Exporta el historial de ecuaciones a formato JSON.

**Firma:**
```python
def save_json(history: list[dict], filename: str = "nct_equations.json") -> str
```

**Parámetros:**
- `history` (`list[dict]`): Historial completo de iteraciones
- `filename` (`str`, opcional): Nombre del archivo de salida

**Retorna:** `str` - Nombre del archivo generado

**Formato JSON:**
```json
[
    {
        "iter": 1,
        "eq": "E = 2.802·C0 ⊗ (2.918 − C2) + -0.686·C0",
        "val": 1.122,
        "timestamp": "2025-12-08T12:51:17.501213"
    },
    ...
]
```

---

## `linkedin_export(history, filename)`

Genera un documento formateado para publicación académica/difusión.

**Firma:**
```python
def linkedin_export(history: list[dict], filename: str = "linkedin_export.txt") -> str
```

**Parámetros:**
- `history` (`list[dict]`): Historial de iteraciones
- `filename` (`str`, opcional): Nombre del archivo de salida

**Retorna:** `str` - Nombre del archivo generado

**Formato de salida:**
```
📘 **NCT Unified Equation Generator — Research Log**
Hanzzel Corp ∑Δ9 — José Zamora
===========================================

Este documento resume la evolución cuaternaria...

• Iteración 01 → E = ...
• Iteración 02 → E = ...
...
```

---

## Constantes Globales

```python
OPS = ["⊕", "⊗", "+", "−"]  # Operadores matemáticos
C   = ["C0", "C1", "C2", "C3"]  # Estados cuánticos
```

---

## Estructura de Datos del Historial

Cada entrada en `history` es un diccionario con:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `iter` | `int` | Número de iteración (1-40) |
| `eq` | `str` | Ecuación NCT generada |
| `val` | `float` | Valor numérico aleatorio asociado |
| `timestamp` | `str` | ISO 8601 timestamp de generación |

**Ejemplo:**
```python
{
    "iter": 5,
    "eq": "E = 0.192·C2 ⊗ (0.606 − C3) ⊕ 2.316·C3",
    "val": 1.066,
    "timestamp": "2025-12-08T12:51:17.501213"
}
```

---

## Casos de Uso

### Caso 1: Generar ecuaciones personalizadas

```python
from nct_visual_engine import generate_equation

# Generar 10 ecuaciones
equations = [generate_equation() for _ in range(10)]
for eq in equations:
    print(eq)
```

### Caso 2: Visualizar estado específico

```python
from nct_visual_engine import ascii_matrix

# Visualizar estado con semilla 42
matrix = ascii_matrix(42)
print(matrix)
```

### Caso 3: Analizar frontera de datos externos

```python
from nct_visual_engine import frontier_curve

# Datos personalizados
custom_data = [
    {"val": 1.5},
    {"val": -2.3},
    {"val": 0.8}
]

curve = frontier_curve(custom_data)
print(f"Frontera crítica: {curve}")
```

### Caso 4: Exportar a JSON

```python
from nct_visual_engine import save_json

# Crear historial manual
history = [
    {
        "iter": 1,
        "eq": "E = 1.0·C0 + (0.0 − C1) ⊕ 1.0·C2",
        "val": 0.5,
        "timestamp": "2025-01-01T00:00:00"
    }
]

filename = save_json(history, "mi_archivo.json")
print(f"Guardado en: {filename}")
```

---

## Diagrama de Dependencias

```
nct_visual_engine.py
├── json (built-in)
├── random (built-in)
├── numpy (external)
└── datetime (built-in)
```

**Requisitos mínimos:**
- Python 3.8+
- NumPy 1.20+
