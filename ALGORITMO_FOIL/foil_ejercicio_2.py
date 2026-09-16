import math

datos = [
    {"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True},
    {"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False},
    {"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}
]

def a():
    P = sum(1 for d in datos if d["en_formacion"])
    N = sum(1 for d in datos if not d["en_formacion"])

    filtrados = [d for d in datos if d["nivel_educativo"] == "terciario"]
    p = sum(1 for d in filtrados if d["en_formacion"])
    n = sum(1 for d in filtrados if not d["en_formacion"])

    def log2_safe(x):
        return math.log2(x) if x > 0 else float('-inf')

    foil_gain = p * (log2_safe(p / (p + n)) - log2_safe(P / (P + N)))

    print(f"P = {P}, N = {N}")
    print(f"p = {p}, n = {n}")
    print(f"p / (p + n) = {p / (p + n):.3f}")
    print(f"P / (P + N) = {P / (P + N):.3f}")
    print(f"log2(p / (p + n)) = {log2_safe(p / (p + n)):.3f}")
    print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
    print(f"FOIL Gain = {foil_gain:.3f}")

def c():
    P = sum(1 for d in datos if d["en_formacion"])
    N = sum(1 for d in datos if not d["en_formacion"])

    filtrados = [d for d in datos if d["edad"] <= 23]
    p = sum(1 for d in filtrados if d["en_formacion"])
    n = sum(1 for d in filtrados if not d["en_formacion"])

    def log2_safe(x):
        return math.log2(x) if x > 0 else float('-inf')

    foil_gain = p * (log2_safe(p / (p + n)) - log2_safe(P / (P + N)))

    print(f"P = {P}, N = {N}")
    print(f"p = {p}, n = {n}")
    print(f"p / (p + n) = {p / (p + n):.3f}")
    print(f"P / (P + N) = {P / (P + N):.3f}")
    print(f"log2(p / (p + n)) = {log2_safe(p / (p + n)):.3f}")
    print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
    print(f"FOIL Gain = {foil_gain:.3f}")

print("Punto A: ")
a()

print("Punto C: ")
c()
