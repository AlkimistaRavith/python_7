import preguntas as p
import random

def shuffle_alt(pregunta):
    #Toma las alternativas del diccionario pregunta, en pregunta.py
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas) #Baraja las opciones de manera aleatoria.
    return pregunta['alternativas']

if __name__ == '__main__':
    #Se selecciona una pregunta, p.e.: 'basicas', 'pregunta_1'
    pregunta = p.pool_preguntas['basicas']['pregunta_1']

    # Resultados
    print(f"Pregunta: {pregunta['enunciado'][0]}") #Enunciado de la pregunta.
    print(f"Alternativas: {shuffle_alt(pregunta)}") #Alternativas, activando la función de random.shuffle. y mostrando la respuesta correcta (1).