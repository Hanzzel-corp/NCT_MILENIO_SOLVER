# Ejemplos de Uso - NCT Visual Engine

## Ejecución Básica

### Ejecutar el motor completo

```bash
# Navegar al directorio
cd nct_milenio_solver

# Activar entorno virtual (recomendado)
source env/bin/activate

# Ejecutar
python nct_visual_engine.py
```

**Salida esperada:**
```
🔷 NCT VISUAL ENGINE — EJECUCIÓN

Iteración 01: E = 2.802·C0 ⊗ (2.918 − C2) + -0.686·C0
Iteración 02: E = -2.746·C1 − (2.158 − C0) − 1.329·C1
...
Iteración 40: E = -2.003·C1 + (-0.209 − C1) + -2.427·C1

🧊 MATRIZ ASCII 21×21 — Estado del sistema:
 .:-=+*#%@
:=+*#%@#%@
...

📈 Curva emergente (frontera crítica):
+0.67 -0.45 +0.82 ...

💾 Guardado JSON → nct_equations.json
📤 Export LinkedIn generado → linkedin_export.txt

✔ Finalizado.
```

---

## Uso Programático

### Ejemplo 1: Importar funciones específicas

```python
from nct_visual_engine import (
    generate_equation,
    ascii_matrix,
    frontier_curve,
    save_json
)

# Generar una sola ecuación
eq = generate_equation()
print(f"Ecuación generada: {eq}")
# Salida: E = 1.234·C2 ⊗ (-0.567 − C1) ⊕ 2.891·C3
```

### Ejemplo 2: Generar conjunto de ecuaciones

```python
from nct_visual_engine import generate_equation
import random

# Generar dataset personalizado
dataset = []
for i in range(100):
    eq = generate_equation()
    val = round(random.uniform(-5, 5), 3)
    dataset.append({
        "id": i + 1,
        "equation": eq,
        "value": val,
        "category": "NCT_generated"
    })

# Usar para análisis posterior
print(f"Total de ecuaciones: {len(dataset)}")
```

### Ejemplo 3: Visualización personalizada

```python
from nct_visual_engine import ascii_matrix

# Generar múltiples matrices con diferentes semillas
seeds = [42, 123, 999, 2025]

for seed in seeds:
    matrix = ascii_matrix(seed)
    print(f"\n=== Matriz con semilla {seed} ===")
    print(matrix)
    print()
```

### Ejemplo 4: Análisis de frontera crítica

```python
from nct_visual_engine import frontier_curve
import numpy as np

# Datos simulados de experimento
experiment_data = [
    {"val": np.random.normal(0, 1)},
    {"val": np.random.normal(2, 0.5)},
    {"val": np.random.normal(-1, 0.3)},
    {"val": np.random.normal(0.5, 1.5)},
]

curve = frontier_curve(experiment_data)
print(f"Frontera crítica: {curve}")

# Interpretar resultados
values = [float(v) for v in curve.split()]
max_val = max(values)
min_val = min(values)

print(f"\nEstado de máxima energía: {max_val:+.2f}")
print(f"Estado de mínima energía: {min_val:+.2f}")
```

### Ejemplo 5: Exportación condicional

```python
from nct_visual_engine import save_json, linkedin_export
import os

def export_conditional(history, threshold=0):
    """
    Exporta solo si hay valores significativos.
    """
    # Calcular valor medio
    avg_val = sum(h["val"] for h in history) / len(history)
    
    if abs(avg_val) > threshold:
        json_file = save_json(history, "significant_equations.json")
        txt_file = linkedin_export(history, "significant_export.txt")
        print(f"Exportado: {json_file}, {txt_file}")
        return True
    else:
        print("Valores no significativos, omitiendo exportación")
        return False

# Uso
history = [...]  # Tu historial
export_conditional(history, threshold=0.5)
```

---

## Análisis de Resultados

### Ejemplo 6: Procesar archivo JSON generado

```python
import json

# Cargar ecuaciones generadas
with open("nct_equations.json", "r", encoding="utf-8") as f:
    equations = json.load(f)

# Análisis estadístico
values = [eq["val"] for eq in equations]
states = [eq["eq"].count("C0") for eq in equations]

print(f"Total de ecuaciones: {len(equations)}")
print(f"Valor medio: {sum(values)/len(values):.3f}")
print(f"Valor máximo: {max(values):.3f}")
print(f"Valor mínimo: {min(values):.3f}")
print(f"Uso de C0: {sum(states)} veces")

# Encontrar ecuaciones con valores extremos
max_eq = max(equations, key=lambda x: x["val"])
min_eq = min(equations, key=lambda x: x["val"])

print(f"\nEcuación con valor máximo ({max_eq['val']}):")
print(max_eq["eq"])

print(f"\nEcuación con valor mínimo ({min_eq['val']}):")
print(min_eq["eq"])
```

### Ejemplo 7: Visualización con matplotlib

```python
import json
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
with open("nct_equations.json", "r") as f:
    data = json.load(f)

iterations = [d["iter"] for d in data]
values = [d["val"] for d in data]

# Crear visualización
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Gráfico 1: Evolución de valores
ax1.plot(iterations, values, 'b-o', markersize=4)
ax1.axhline(y=0, color='r', linestyle='--', alpha=0.5)
ax1.set_xlabel('Iteración')
ax1.set_ylabel('Valor')
ax1.set_title('Evolución de Valores NCT')
ax1.grid(True, alpha=0.3)

# Gráfico 2: Frontera crítica (tanh suavizado)
arr = np.array(values)
smooth = np.tanh(arr / np.std(arr))
ax2.plot(iterations, smooth, 'g-s', markersize=4)
ax2.axhline(y=0, color='r', linestyle='--', alpha=0.5)
ax2.axhline(y=1, color='orange', linestyle=':', alpha=0.5)
ax2.axhline(y=-1, color='orange', linestyle=':', alpha=0.5)
ax2.set_xlabel('Iteración')
ax2.set_ylabel('Valor Suavizado (tanh)')
ax2.set_title('Frontera Crítica Emergente')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("nct_analysis.png", dpi=150)
plt.show()
```

---

## Casos de Uso Avanzados

### Ejemplo 8: Sistema de monitoreo continuo

```python
from nct_visual_engine import generate_equation, frontier_curve
from datetime import datetime
import time
import json

def monitor_system(duration_seconds=60, interval=5):
    """
    Monitorea el sistema generando ecuaciones periódicamente.
    """
    history = []
    start_time = time.time()
    iteration = 0
    
    print(f"🔷 Iniciando monitoreo por {duration_seconds}s...")
    
    while time.time() - start_time < duration_seconds:
        iteration += 1
        eq = generate_equation()
        
        # Simular valor de sensor (en caso real, leer de hardware)
        import random
        val = round(random.uniform(-3, 3), 3)
        
        entry = {
            "iter": iteration,
            "eq": eq,
            "val": val,
            "timestamp": datetime.now().isoformat()
        }
        history.append(entry)
        
        # Mostrar cada 5 iteraciones
        if iteration % 5 == 0:
            curve = frontier_curve(history[-10:])  # Últimas 10
            print(f"[{iteration}] Últimas fronteras: {curve[:50]}...")
        
        time.sleep(interval)
    
    # Guardar resultados
    with open("monitor_log.json", "w") as f:
        json.dump(history, f, indent=2)
    
    print(f"✔ Monitoreo completado. {iteration} entradas guardadas.")
    return history

# Ejecutar (descomentar para usar)
# monitor_system(duration_seconds=30, interval=2)
```

### Ejemplo 9: Comparación de estados cuánticos

```python
from nct_visual_engine import generate_equation, C
import random

def analyze_state_distribution(n_samples=1000):
    """
    Analiza la distribución de estados C0-C3 en ecuaciones generadas.
    """
    state_counts = {"C0": 0, "C1": 0, "C2": 0, "C3": 0}
    
    for _ in range(n_samples):
        eq = generate_equation()
        for state in C:
            state_counts[state] += eq.count(state)
    
    total = sum(state_counts.values())
    
    print("Distribución de estados cuánticos:")
    print("=" * 40)
    for state, count in sorted(state_counts.items()):
        percentage = (count / total) * 100
        bar = "█" * int(percentage / 2)
        print(f"{state}: {count:4d} ({percentage:5.1f}%) {bar}")
    print("=" * 40)
    print(f"Total de apariciones: {total}")
    
    return state_counts

# Ejecutar análisis
stats = analyze_state_distribution(500)
```

---

## Integración con Otros Sistemas

### Ejemplo 10: API web simple (Flask)

```python
# Requiere: pip install flask

from flask import Flask, jsonify
from nct_visual_engine import generate_equation, ascii_matrix
import random

app = Flask(__name__)

@app.route('/api/equation', methods=['GET'])
def get_equation():
    """Endpoint para generar ecuación NCT."""
    eq = generate_equation()
    return jsonify({
        "equation": eq,
        "value": round(random.uniform(-3, 3), 3),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/matrix/<int:seed>', methods=['GET'])
def get_matrix(seed):
    """Endpoint para obtener matriz ASCII."""
    matrix = ascii_matrix(seed)
    return jsonify({
        "seed": seed,
        "matrix": matrix,
        "dimensions": "21x21"
    })

# Ejecutar: python -c "from app import app; app.run(debug=True)"
```

### Ejemplo 11: Línea de comandos personalizada

```python
#!/usr/bin/env python3
# nct_cli.py - Interfaz de línea de comandos

import argparse
from nct_visual_engine import generate_equation, ascii_matrix, save_json
import json

def main():
    parser = argparse.ArgumentParser(description="NCT Visual Engine CLI")
    parser.add_argument("-n", "--count", type=int, default=10,
                       help="Número de ecuaciones a generar")
    parser.add_argument("-o", "--output", type=str, default="output.json",
                       help="Archivo de salida")
    parser.add_argument("--matrix", action="store_true",
                       help="Mostrar matriz ASCII")
    parser.add_argument("--seed", type=int, default=42,
                       help="Semilla para matriz")
    
    args = parser.parse_args()
    
    print(f"🔷 Generando {args.count} ecuaciones...")
    
    history = []
    for i in range(1, args.count + 1):
        eq = generate_equation()
        import random
        val = round(random.uniform(-3, 3), 3)
        history.append({"iter": i, "eq": eq, "val": val})
        print(f"  {i:3d}: {eq}")
    
    if args.matrix:
        print("\n🧊 Matriz ASCII:")
        print(ascii_matrix(args.seed))
    
    save_json(history, args.output)
    print(f"\n💾 Guardado en: {args.output}")

if __name__ == "__main__":
    main()
```

**Uso:**
```bash
python nct_cli.py -n 20 --matrix --seed 123 -o mi_output.json
```

---

## Solución de Problemas

### Error: `ModuleNotFoundError: No module named 'numpy'`

**Solución:**
```bash
pip install numpy
```

### Error: Archivos no se generan

**Verificar permisos:**
```python
import os
print(os.getcwd())  # Verificar directorio actual
print(os.access('.', os.W_OK))  # Verificar permisos de escritura
```

### Matriz ASCII vacía o corrupta

**Causa probable:** Semilla no válida o problema con NumPy.

**Solución:**
```python
# Asegurar semilla entera positiva
seed = abs(int(your_value)) % 10000
matrix = ascii_matrix(seed)
```
