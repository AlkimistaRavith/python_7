import preguntas as p

def print_pregunta(enunciado, alternativas):
    # Imprimir el enunciado
    print(enunciado)

    # Letras asociadas
    letras = ['A', 'B', 'C', 'D']

    for i, alternativa in enumerate(alternativas):
        texto = alternativa[0]
        print(f"{letras[i]}. {texto}")

if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])

    # Enunciado básico 1
    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4