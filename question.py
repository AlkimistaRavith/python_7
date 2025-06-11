import preguntas as p
import random
from shuffle import shuffle_alt

# Diccionario interno para hacer seguimiento de preguntas disponibles por dificultad
opciones_disponibles = {
    'basicas': [1, 2, 3],
    'intermedias': [1, 2, 3],
    'avanzadas': [1, 2, 3]
}

def choose_q(dificultad):
    if not opciones_disponibles[dificultad]:
        raise ValueError(f"No quedan preguntas disponibles en el nivel '{dificultad}'.")

    # Elegir aleatoriamente una pregunta disponible
    n_elegido = random.choice(opciones_disponibles[dificultad])
    opciones_disponibles[dificultad].remove(n_elegido)

    # Obtener pregunta del pool
    clave = f'pregunta_{n_elegido}'
    pregunta = p.pool_preguntas[dificultad][clave]

    # Obtener enunciado y alternativas mezcladas
    enunciado = pregunta['enunciado'][0]
    alternativas = shuffle_alt(pregunta)

    return enunciado, alternativas

if __name__ == '__main__':
    opciones = ['1', '2', '3']
    opcion_nivel = '1'
    while opcion_nivel in opciones:
        try:
            opcion_nivel = input("Selecciona nivel de dificultad (1 = básicas, 2 = intermedias, 3 = avanzadas, otro para salir): ")
            
            if opcion_nivel == '1':
                nivel = 'basicas'
            elif opcion_nivel == '2':
                nivel = 'intermedias'
            elif opcion_nivel == '3':
                nivel = 'avanzadas'
            else:
                print("Fin")
                break

            pregunta, alternativas = choose_q(nivel)
            print(f'El enunciado es: {pregunta}')
            print('Las alternativas son:')
            for alt in alternativas:
                print(alt)
        except ValueError as e:
            print(e)
        continue