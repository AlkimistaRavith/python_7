def choose_level(n_pregunta, p_level):
    p_totales = p_level * 3
    if n_pregunta > p_totales or n_pregunta < 1:
        print(f"El número ingresado de la pregunta no existe. \nPor favor ingresar un número entre 1 y {p_totales}, para {p_level} preguntas por nivel.")
        return None

    preguntas = {
        "Basica": [],
        "Intermedia": [],
        "Avanzada": []
    }

    for i in range(1, p_level + 1):
        preguntas["Basica"].append(i)
        preguntas["Intermedia"].append(i + p_level)
        preguntas["Avanzada"].append(i + 2 * p_level)

    for nivel, indices in preguntas.items():
        if n_pregunta in indices:
            return nivel


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # [avanzadas] Error: la selección (7,2) es incorrecta, ya que para 2 preguntas por nivel, da un total de 6 preguntas, no existe la prgunta 7.
    print(choose_level(4, 3)) # intermedias