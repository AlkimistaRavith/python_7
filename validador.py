
def validate(opciones, eleccion):
    # Mientras no se seleccione una opcion valida, pedirá nuevamente una elección.
    while eleccion not in opciones:
        print(f"Opción no válida, ingrese una de las opciones válidas: {opciones}")
        eleccion = input("Ingrese una opción: ").lower()
    return eleccion

#opciones de validación
opciones = ["a", "b", "c", "d"]    


if __name__ == '__main__':
    eleccion = input('Ingresa una Opción: ').lower()

    resultado = validate(opciones, eleccion)
    print(f"Opción válida ingresada: {resultado}")