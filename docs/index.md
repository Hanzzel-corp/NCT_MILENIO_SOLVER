# NCT Visual Engine - Documentación

> Motor de visualización cuaternaria basado en geometrías emergentes

---

## 📚 Índice de Documentación

- **[Arquitectura](./arquitectura.md)** - Estructura y componentes del sistema
- **[Referencia API](./api.md)** - Documentación de funciones y módulos
- **[Framework NCT](./nct-framework.md)** - El marco matemático cuaternario
- **[Ejemplos de Uso](./ejemplos.md)** - Guías prácticas y casos de uso

---

## 🚀 Inicio Rápido

### Instalación

```bash
# Clonar o navegar al repositorio
cd nct_milenio_solver

# Crear entorno virtual (recomendado)
python -m venv env
source env/bin/activate  # Linux/Mac
# o
env\Scripts\activate     # Windows

# Instalar dependencias
pip install numpy
```

### Ejecución Básica

```bash
python nct_visual_engine.py
```

**Salida esperada:**
- 40 ecuaciones NCT generadas
- Matriz ASCII 21×21
- Curva de frontera crítica
- Archivo `nct_equations.json`
- Export `linkedin_export.txt`

---

## 🎯 Propósito del Motor

El NCT Visual Engine demuestra cómo ecuaciones matemáticas distintas convergen hacia una única geometría emergente cuando se expresan como transiciones de estado en el espacio cuaternario C0–C3.

### ¿Qué problema resuelve?

Los problemas matemáticos clásicos se formulan en marcos lineales:
- Ecuaciones diferenciales
- Espectros de operadores
- Curvaturas geométricas
- Turbulencias fluidas
- Complejidad computacional

Este motor muestra que al eliminar la linealidad y expresarlos como transiciones de estado, **todos comparten la misma estructura energética subyacente**.

---

## 📁 Estructura del Proyecto

```
nct_milenio_solver/
├── nct_visual_engine.py      # Motor principal
├── nct_equations.json        # Datos de ecuaciones generadas
├── linkedin_export.txt       # Exportación formateada
├── README.md                 # Documentación inicial
├── env/                      # Entorno virtual
└── docs/                     # Documentación extendida
    ├── index.md
    ├── arquitectura.md
    ├── api.md
    ├── nct-framework.md
    └── ejemplos.md
```

---

## 🔧 Dependencias

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| Python | 3.8+ | Lenguaje base |
| NumPy | 1.20+ | Matrices y cálculo numérico |
| json | Built-in | Serialización de datos |
| datetime | Built-in | Timestamps |

---

## 📄 Licencia

Open Source — uso libre para investigación, estudio y divulgación.

**Créditos:** Pablo Zamora (Hanzzel Corp ∑Δ9)

---

## 🔗 Enlaces

- [README Principal](../README.md)
- [Código Fuente](../nct_visual_engine.py)
