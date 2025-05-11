from validador import parser

ejemplos = [
    "(4 + 5) * (TRUE AND FALSE)",
    "(TRUE AND FALSE) / (4 - 1)",
    "1 + ",
    "NOT TRUE",
    "(TRUE AND FALSE) OR (NOT TRUE)",  # Corregido
    "(3 + 2) * (TRUE AND FALSE",
    "(2 AND 3) / (4 - 1)",
]

for entrada in ejemplos:
    print(f"Evaluando: {entrada}")
    try:
        result = parser.parse(entrada)
        print(f"Expresión válida: {result}\n")
    except SyntaxError as e:
        print(f"Expresión inválida: {e}\n")