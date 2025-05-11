from validador import parser

ejemplos = [
    "(4 + 5) * 2",
    "3 - (2 + )",
    "7 + 3 * (10 / (12 / (3 + 1) - 1))",
    "(4 + ) * 5",
    "3 + 2",
    "3 + (4 - 1"
]

for entrada in ejemplos:
    print(f"Evaluando: {entrada}")
    try:
        parser.parse(entrada + '\n')  # Agregamos '\n' para marcar fin de entrada
        print("Expresión válida\n")
    except:
        print("Expresión inválida\n")
