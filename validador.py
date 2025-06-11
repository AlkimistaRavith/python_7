
def validate(opciones, eleccion):
    # Mientras no se seleccione una opcion valida, pedirá nuevamente una elección.
    while eleccion not in opciones:
        print(f"Opción no válida, ingrese una de las opciones válidas: {opciones}")
        eleccion = input("Ingrese una opción: ").lower()
    return eleccion

  


if __name__ == '__main__':
    
     opciones = ["a", "b", "c", "d"]  #validación con letras
    # opciones = ["0", "1"] #validación con numeros 
    # (alternan) el # entre opciones de letras o numeros, para probar.
    eleccion = input('Ingresa una Opción: ').lower()
    resultado = validate(opciones, eleccion)
    print(f"Opción válida ingresada: {resultado}")