def choose_level(n_pregunta, p_level):
    p_totales = p_level * 3 #Total de preguntas que se obtienen en X preguntas por nivel.

    if n_pregunta > p_totales or n_pregunta < 1: #Validación del N° de la pregunta, no puede exceder el total de preguntas.
        print(f"El número ingresado de la pregunta no existe. \n Por favor ingresar un número entre 1 y {p_totales}, para {p_level} preguntas por nivel.")
        return ""
    #diccionario para guardar los numeros de las preguntas según su nivel.
    preguntas = {
        "Basicas": [],
        "Intermedias": [],
        "Avanzadas": []
    }

    for i in range(1, p_level + 1):
        preguntas["Basicas"].append(i) #lista las preguntas basicas en los primeros numeros.
        preguntas["Intermedias"].append(i + p_level) #lista las preguntas intermedias en los numeros medios.
        preguntas["Avanzadas"].append(i + 2 * p_level) #lista las preguntas avanzadas en los últimos numeros.

    for nivel, indices in preguntas.items():
        #El numero de pregunta solicitado está en una de las lista del diccionario(indices), entrega el resultado correspondiente (nivel).
        if n_pregunta in indices:
            return nivel
            
    

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # [avanzadas] Error: la selección (7,2) es incorrecta, ya que para 2 preguntas por nivel, da un total de 6 preguntas, no existe la prgunta 7.
    print(choose_level(4, 3)) # intermedias
