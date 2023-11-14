#Punto 1

#La diferencia entre las listas y las tuplas consiste en que
#las listas permite modificar cada uno de los elementos que contiene
# mientras que con las tuplas los datos que esta contenga no se podrán modificar
# pero si se pueden redefinir.

#Las tuplas suelen ser útiles para el almacenamiento de datos que no van a cambiar
# optimizando así el uso de memoria. En el caso de las listas, estas son útiles emplearlas
# cuando tenemos datos que se van a estar modificando constantemente.


# Punto 2




#Punto 3
#factorial de un número
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


print(factorial(5))
