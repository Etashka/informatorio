import pprint
###########################################################################

# 1-Crear un diccionario con los nombres de tres frutas y sus respectivos precios y
#mostrar el diccionario completo.

frutas = {'manzana': 1.5, 'banana': 2.0, 'naranja': 1.0}

# Utilizamos pprint para que quede mas "bonito" visualmente. El pprint lo que hace es realizar el salto de pagina
# Y como no funcionaba en mi terminal solo con pprint, agreguè el width =1 para forzar el salto de linea
pprint.pprint(frutas, width=1)

###################################################################################

#2-Crear una lista con los nombres de tres ciudades y agregar una cuarta ciudad al
#final de la lista.

ciudades = ['Resistencia', 'Corrientes', 'Córdoba']

ciudades.append('Mendoza')

print(ciudades)

###################################################################################
#3-Crear una lista con los nombres de tres países y mostrar el segundo país de la
#lista.

paises = ['Argentina', 'Bolivia', 'España']


print(paises[1])

###################################################################################

#4-Crear un diccionario con los nombres de tres personas y sus respectivas
#edades. Mostrar la edad de la tercera persona en el diccionario

# el ejercicio no lo pide, pero en mi lógica...¿cómo va a saber la persona que busque en el diccionario
# que la tercer persona es "Pedro"? Entonces necesitaba enumerar para que, con saber la posición podamos encontrar la edad
# entonces cree una tupla, pasé a diccionario y lo enumeré para encontrar lo pedido sòlo por la posición

tupla_personas = (('Juan', 25), ('María', 30), ('Pedro', 35))
diccionario_personas = dict(enumerate (tupla_personas))
tercer_valor = diccionario_personas[2][1]
print (tercer_valor,"años")

###################################################################################

#5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más
#grande en el conjunto.
num = set(range(1, 11))
nummax = max(num)
# la "f"  es para que en {nummax} salga el numero y no solo {nummax}
print(f'El número más grande en el conjunto es: {nummax}')

###################################################################################

#7-Crear un diccionario con los nombres de tres ciudades y sus respectivas
#poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva
#población. Mostrar el diccionario resultante..
ciudades = {
    "Ciudad de Buenos Aires": 89186530,
    "Corrientes": 14601480,
    "Salta": 11247720
}
ciudades["Colonia"] = 15150197
pprint.pprint(ciudades,width=1)

###################################################################################

#8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[::-1]es un slicing que se utiliza para invertir una lista en Python
numeros_inverso = numeros[::-1]
print("El inverso de su lista es:", numeros_inverso)

###################################################################################
#9-Crear una lista con los nombres de tres países y ordenar la lista en orden
#alfabético. Mostrar la lista resultante

paises = ['Mexico', 'Argentina', 'Bolivia', ]
#sort() se utiliza para ordenar una lista en su lugar, o sea, modifica la lista original
paises.sort()
print("Los paises se encuentran ordenados alfabeticamente", paises)
###################################################################################
#10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la
#lista. Mostrar la lista resultante.

frutas = ['manzana', 'banana', 'naranja']
print("La lista de frutas es",frutas)
fruta_delete = frutas.pop(1)
#  print("Se elimina",fruta_delete)
#  print("Y queda entonces",frutas)
###################################################################################
#11-Crear una lista con los nombres de tres animales y agregar una cuarta animal
#al principio de la lista. Mostrar la lista resultante.

animales = ['gato', 'perro', 'conejo']
print("La lista de animales es",animales)
animales.insert(0, 'ratón')
print("Se agrega ratòn y queda la lista en:")
print(animales)
###################################################################################

#12-Crear una lista con los nombres de tres países y reemplazar el segundo país de
#la lista por otro país. Mostrar la lista resultante.

paises = ["Argentina", "Bolivia", "Peru"]
nuevo_pais = input("Ingresa el nombre del país por el que quieres reemplazar a " + paises[1] + ": ")
paises[1] = nuevo_pais
print(paises)

###################################################################################
# 13-Crear una lista con los nombres de tres colores y agregar dos colores más al
# final de la lista. Mostrar la lista resultante.
# Creamos una lista con tres colores
colores = ["rojo", "verde", "azul"]
nuevo_color1 = input("Ingresa el nombre del primer color que quieres agregar: ")
nuevo_color2 = input("Ingresa el nombre del segundo color que quieres agregar: ")
colores.append(nuevo_color1)
colores.append(nuevo_color2)
print(colores)
###################################################################################
# 14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los
# elementos de la tupla.
numeros = (1, 2, 3, 4, 5)
suma = sum(numeros)
print("La suma de los números del 1 al 5 es:", suma)
###################################################################################