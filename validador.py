
def validate(opcion, opciones):
    # Mientras no se seleccione una opcion valida, pedirá nuevamente una elección.
    while opcion not in opciones:
        print(f"Opción no válida, ingrese una de las opciones válidas: {opciones}")
        opcion = input("Ingrese una opción: ").lower()
    return opcion

  


if __name__ == '__main__':
    
    opciones = ["a", "b", "c", "d"]  #validación con letras
    opciones = ["0", "1"] #validación con numeros 
    # (alternan) el # entre opciones de letras o numeros, para probar.
    opcion = input('Ingresa una Opción: ').lower()
    resultado = validate(opciones, opcion)
    print(f"Opción válida ingresada: {resultado}")