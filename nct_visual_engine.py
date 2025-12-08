import json
import random
import numpy as np
from datetime import datetime

# =======================================================
#     NCT VISUAL ENGINE — José Zamora / Hanzzel Corp ∑Δ9
# =======================================================

OPS = ["⊕", "⊗", "+", "−"]
C   = ["C0", "C1", "C2", "C3"]

def generate_equation():
    """Genera una ecuación cuaternaria estilo NCT."""
    a, b, c = [round(random.uniform(-3, 3), 3) for _ in range(3)]
    x, y, z = random.choice(C), random.choice(C), random.choice(C)
    op1, op2 = random.choice(OPS), random.choice(OPS)

    return f"E = {a}·{x} {op1} ({b} − {y}) {op2} {c}·{z}"


# 1️⃣ =====================================================
#        VISUALIZACIÓN ASCII 21×21
# =========================================================

def ascii_matrix(seed_val):
    """Genera una matriz 21×21 basada en un estado numérico."""
    np.random.seed(seed_val)
    M = np.random.randn(21, 21)

    chars = " .:-=+*#%@"
    scaled = ((M - M.min()) / (M.max() - M.min()) * (len(chars)-1)).astype(int)

    grid = "\n".join("".join(chars[v] for v in row) for row in scaled)
    return grid


# 2️⃣ =====================================================
#        CURVA EMERGENTE — “FRONTERA CRÍTICA”
# =========================================================

def frontier_curve(history):
    """Devuelve una representación simple de la frontera crítica."""
    values = [h["val"] for h in history]
    arr = np.array(values)

    # Suavizado NCT (no lineal)
    smooth = np.tanh(arr / np.std(arr))

    curve = " ".join(f"{v:+.2f}" for v in smooth)
    return curve


# 3️⃣ =====================================================
#          GUARDAR TODAS LAS ECUACIONES EN JSON
# =========================================================

def save_json(history, filename="nct_equations.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)
    return filename


# 4️⃣ =====================================================
#     EXPORT AUTOMÁTICO FORMATO LINKEDIN (PAPER STYLE)
# =========================================================

def linkedin_export(history, filename="linkedin_export.txt"):
    header = (
        "📘 **NCT Unified Equation Generator — Research Log**\n"
        "Hanzzel Corp ∑Δ9 — José Zamora\n"
        "===========================================\n\n"
        "Este documento resume la evolución cuaternaria de ecuaciones "
        "generadas en el marco NCT para ilustrar sistemas no lineales, "
        "no secuenciales y sin dependencia espacio–temporal.\n\n"
    )

    body = ""
    for h in history:
        body += f"• Iteración {h['iter']:02d} → {h['eq']}\n"

    full = header + body

    with open(filename, "w", encoding="utf-8") as f:
        f.write(full)

    return filename


# =======================================================
#                   EJECUCIÓN PRINCIPAL
# =======================================================

if __name__ == "__main__":
    history = []

    print("\n🔷 NCT VISUAL ENGINE — EJECUCIÓN\n")

    for i in range(1, 41):
        eq = generate_equation()
        val = round(random.uniform(-3, 3), 3)

        history.append({
            "iter": i,
            "eq": eq,
            "val": val,
            "timestamp": datetime.now().isoformat()
        })

        print(f"Iteración {i:02d}: {eq}")

    # --- ASCII 21×21 ---
    seed_val = int(abs(history[-1]["val"] * 100))
    ascii_art = ascii_matrix(seed_val)

    print("\n🧊 MATRIZ ASCII 21×21 — Estado del sistema:")
    print(ascii_art)

    # --- Frontera crítica ---
    curve = frontier_curve(history)
    print("\n📈 Curva emergente (frontera crítica):")
    print(curve)

    # --- Guardado JSON ---
    json_file = save_json(history)
    print(f"\n💾 Guardado JSON → {json_file}")

    # --- Export LinkedIn ---
    txt_file = linkedin_export(history)
    print(f"📤 Export LinkedIn generado → {txt_file}")

    print("\n✔ Finalizado.\n")
