# Requisitos técnicos:
# Metodos y propiedades de string
# Indexar estructura de datos
# Todos los tipos de datos 
# Se te pide crear un programa que le pida al usuario que ingresar un texto
# cualquiera, por ejemplo, un artículo o una frase.
# Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
# elección.
# Nuestro código va a procesar esa información para realizar los análisis
# necesarios para devolverle al usuario la siguiente información:
# 1- Cantidad de veces que aparece cada una de letras que eligió.
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
# string
# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
# minúscula.
# 2- Cuantas palabras hay en total en todo el texto.
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
# 3- Cual es la primera letra y cuál es la última. (Indexación)
# 4- Mostrar el texto en orden inverso.
# 5- Decir si la palabra "python" aparece en el texto.
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
# string para mostrar al usuario.
# Pedimos al usuario que ingrese un texto y las letras a buscar

texto = input("Ingrese un texto: ")
letras = input("Ingrese 3 letras a buscar (separadas por espacios): ").lower().split()


cantidades = {}
i = 0
while i < len(letras):
    letra = letras[i]
    cantidades[letra] = texto.lower().count(letra)
    i += 1


palabras = texto.split()
cantidad_palabras = 0
while palabras:
    cantidad_palabras += 1
    palabras.pop()


primera_letra = texto[0]
ultima_letra = texto.rstrip(",.;:!?")[-1]


texto_inverso = ""
i = len(texto) - 1
while i >= 0:
    texto_inverso += texto[i]
    i -= 1


aparece_python = False
palabras = texto.lower().split()
while palabras:
    palabra = palabras.pop()
    if palabra == "python":
        aparece_python = True

mensaje_python = "La palabra 'python' aparece en el texto." if aparece_python else "La palabra 'python' no aparece en el texto."


print("Cantidad de veces que aparecen las letras:")
i = 0
while i < len(letras):
    letra = letras[i]
    print(f"{letra}: {cantidades[letra]}")
    i += 1

print(f"Cantidad total de palabras: {cantidad_palabras}")
print(f"Primera letra: {primera_letra}")
print(f"Última letra: {ultima_letra}")
print(f"Texto en orden inverso: {texto_inverso}")
print(mensaje_python)