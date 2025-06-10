
def validate(opciones, eleccion):
    # Definir validación de eleccion
    while eleccion not in opciones:
        print(f"Opción no válida, ingrese una de las opciones válidas: {opciones}")
        eleccion = input("Ingrese una opción: ").lower()
    return eleccion
    


if __name__ == '__main__':
    opciones = ["a", "b", "c", "d"]
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    
    resultado = validate(opciones, eleccion)
    print(f"Opción válida ingresada: {resultado}")
    
    
    
