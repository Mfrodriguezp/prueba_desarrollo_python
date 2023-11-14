#Escribe una función en Python que cuente la cantidad de palabras en una cadena de texto


def contador_palabras (texto) :
    #se realiza la separación de palabras por espacios
    palabras_encontradas = texto.split(" ")
    #de la lista que se genera, se cuentan los elementos de la misma para determinar la cantidad
    #de palabras
    cantidad_palabras = len(palabras_encontradas)
    respuesta = f"En el texto ingresado se encontraron {cantidad_palabras} palabra(s)"
    return respuesta

texto = input("Ingrese por favor el texto para analizar: ")

print(contador_palabras(texto))