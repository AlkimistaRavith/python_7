import preguntas as p
import random
from shuffle import shuffle_alt

# Diccionario interno para saber que preguntas están disponibles.
opciones_disponibles = {
    "basicas": [1, 2, 3],
    "intermedias": [1, 2, 3],
    "avanzadas": [1, 2, 3]
}

def choose_q(dificultad):
    # Elegir aleatoriamente una pregunta disponible, de la dificultad
    n_elegido = random.choice(opciones_disponibles[dificultad])
    opciones_disponibles[dificultad].remove(n_elegido)

    # Obtener pregunta del pool
    clave = f"pregunta_{n_elegido}"
    pregunta = p.pool_preguntas[dificultad][clave]

    # Obtener enunciado y alternativas mezcladas
    enunciado = pregunta["enunciado"][0]
    alternativas = shuffle_alt(pregunta)

    return enunciado, alternativas

if __name__ == "__main__":
    #Para iterar varias veces, eliminando preguntas de distinto nivel en cada iteracion 
    # y dejando un mensaje si no quedan preguntas de un nivel
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    print(opciones_disponibles)

    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    print(opciones_disponibles)

    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    print(opciones_disponibles)
