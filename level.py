def choose_level(n_pregunta, p_level):
    if p_level == 2:
        if n_pregunta <= 2:
            return "basica"
        elif n_pregunta <= 4:
            return "intermedia"
        else:
            return "avanzada"
    elif p_level == 3:
        if n_pregunta <= 3:
            return "basica"
        elif n_pregunta <= 6:
            return "intermedia"
        else:
            return "avanzada"


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias