import preguntas as p

def verificar(alternativas, respuesta):
    try:
        # Converitr elección ["a","b","c","d"] a índice
        respuesta = ["a","b","c","d"].index(respuesta)

        # revisa si la alternativa seleccionada tiene un 1 (es correcta)
        if alternativas[respuesta][1] == 1:
            print("Respuesta Correcta")
            return True
        else:
            print("Respuesta Incorrecta")
            return False
    except ValueError:
        print("El ingreso no está en las opciones.")


if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)
