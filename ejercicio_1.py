#definimos la funcion
def factorial(numero) :
    #se evalúa si el número ingresado es igual 1
    if numero == 1 :
        return 1
    #si se evalúa que el número ingresado mayor a 1
    #pasará al else
    else :
        #En este apartado, tendremos el número el cual se multiplicará a sí mismo por el número restado 1
        #esto se repetirá hasta que el último número obtenido sea == 1 y hará el respectivo proceso
        return numero * factorial(numero -1)
    
#solicitud de dato por pantalla
dato = int(input("Por favor ingrese un número entero no negativo: "))

#validacion de ingreso de números enteros positivos 
while dato < 1 :
    dato = int(input("Por favor ingrese un número entero no negativo: "))
    
numero = dato

print(factorial(numero))

