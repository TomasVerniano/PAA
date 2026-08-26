def clasificarAccion(users):
    for user in users:

        if "victoria" in user or "derrota" in user:
            print("Categoría: Combate")
        elif "descubrimiento" in user or "sin_hallazgos" in user:
            print("Categoría: Exploración")
        elif "mensaje_enviado" in user:
            print("Categoría: Interacción Social")

users = [
    ["user01", 120, "victoria"],
    ["user02", 300, "descubrimiento"],
    ["user03", 180, "mensaje_enviado"],
    ["user04", 90, "derrota"],
    ["user05", 240, "sin_hallazgos"]
]

clasificarAccion(users)