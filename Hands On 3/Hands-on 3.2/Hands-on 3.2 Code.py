from validador import parser

ejemplos = [
    "(1 AND 0) OR (NOT 1)",
    "(1 AND (0 OR 1)",
    "1 AND 0",
    "NOT 1",
    "1 OR 0"
]

for entrada in ejemplos:
    print(f"Evaluando: {entrada}")
    try:
        parser.parse(entrada + '\n')
        print("Expresión válida\n")
    except:
        print("Expresión inválida\n")
