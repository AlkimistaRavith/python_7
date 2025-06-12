# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys

# valores iniciales - 
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'


# ----------------------------------------

os.system(op_sys) # limpiar pantalla

print('Bienvenido a la Trivia')
opcion = input('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
        
    > ''')
# 1. validar opcion
opcion = validate(opcion, ['0', '1'])


# 2. Definir el comportamiento de Salir
if opcion == '0':
    print('Nos vemos pronto!')
    time.sleep(2)
    os.system(op_sys)
    sys.exit()
    # finaliza programa

# 3. Validar el número de preguntas por nivel
while True:
    p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
    if p_level.isdigit() and 1 <= int(p_level) <= 3:
        p_level = int(p_level)
        break
    else:
        print('Por favor, ingrese un número válido entre 1 y 3.')
    

# Funcionamiento de preguntas
while correcto and n_pregunta < 3*p_level:
    
    if continuar == 'y':
        #contador de preguntas
        n_pregunta += 1
        # 4. Validar el número de nivel
        nivel = choose_level(n_pregunta, p_level).lower()
        
        
        print(f'Pregunta {n_pregunta}:')
        # 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
        pregunta, alternativas = choose_q(nivel)
        print(f"El enunciado es: {pregunta}")
        print("Las alternativas son:")

        #6. Imprimir el enunciado y sus alternativas en pantalla
        letras = ["a","b","c","d"]
        for i, alternativa in enumerate(alternativas):
            texto = alternativa[0]
            print(f"{letras[i]}. {texto}")
        
        respuesta = input('Escoja la alternativa correcta:\n> ').lower()
        # 7. Validar la respuesta entregada
        respuesta = validate(respuesta, ["a","b","c","d"])
        # 8. Verificar si la respuesta es correcta o no
        correcto = verificar(alternativas, respuesta)
        
        if correcto and n_pregunta < 3*p_level:
            print('Muy bien sigue así!')
            continuar = input('Desea continuar? [y/n]: ').lower()
            #9. Validar si es que se responde y o n
            continuar = validate(continuar, ['y', 'n'])
            if continuar == 'n':
                print('Gracias por jugar. ¡Hasta la próxima!')
                break
            os.system(op_sys)
        elif correcto and n_pregunta == 3*p_level:
            print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
            time.sleep(3)
            os.system(op_sys)
        else: 
            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
            time.sleep(3)
            exit()
    else: 
        print('Nos vemos la proxima vez, sigue practicando')
        time.sleep(3)
        exit()
            
            
