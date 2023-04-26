#1-Escribe un programa que solicite al usuario su nombre y lo imprima en la pantalla

name = input("Por favor, ingrese su nombre: ")
print("¡Hola " + name + "!")

#2-Escribe un programa que solicite al usuario su nombre y luego imprima un
#mensaje de bienvenida.

name = input("Por favor, ingrese su nombre: ")
print("¡Bienvenido(a) " + name + " a nuestro curso!")

#3-Crea un programa que pida al usuario su edad y lo imprima en pantalla.

year = input("Por favor, ingrese su edad: ")
print("Su edad es: " + year)

#4-Crea un programa que calcule la suma de dos números y lo imprima en
# pantalla.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
print("La suma de " + str(num1) + " y " + str(num2) + " es: " + str(suma))

#5-Crea un programa que pida al usuario dos números enteros y muestre en
#pantalla su cociente y su resto. 
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
cociente = num1 // num2
resto = num1 % num2
print("El cociente de " + str(num1) + " dividido por " + str(num2) + " es: " + str(cociente))
print("El resto de " + str(num1) + " dividido por " + str(num2) + " es: " + str(resto))

#6-Crea un programa que pida al usuario el radio de un círculo y calcule su área.
#La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
#Supongamos que pi = 3.1416

pi = 3.1416
radio = float(input("Ingrese el radio del círculo: "))
area = pi * (radio ** 2)
print("El área del círculo es: " + str(area))

#7-Escribe un programa que calcule el área de un triángulo a partir de la base y la
#altura dadas.

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es: " + str(area))

#8-Crea un programa que pida al usuario el radio de un círculo y muestre su
#diámetro, su circunferencia y su área.
#Supón que pi es aproximadamente 3.14159.

pi = 3.14159
radio = float(input("Ingrese el radio del círculo: "))
diametro = 2 * radio
circunferencia = 2 * pi * radio
area = pi * (radio ** 2)
print("El diámetro del círculo es: " + str(diametro))
print("La circunferencia del círculo es: " + str(circunferencia))
print("El área del círculo es: " + str(area))


#9-Escribe un programa que solicite al usuario dos números y luego imprima la
#suma, la resta, la multiplicación y la división de los dos números.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2

print("La suma es: " + str(suma))
print("La resta es: " + str(resta))
print("La multiplicación es: " + str(mult))
print("La división es: " + str(div))

#10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a
#euros.
#Supón que el tipo de cambio es de 0.84 euros por dólar.

dolares = float(input("Ingrese la cantidad en dólares: "))
tipo_cambio = 0.84
euros = dolares * tipo_cambio
print("La cantidad en euros es: " + str(euros))

#11-Crea un programa que pida al usuario una palabra y muestre en pantalla
#cuántas letras tiene.
#Pss psssss toma... .len()

palabra = input("Ingrese una palabra: ")
num_letras = len(palabra)
print("La palabra tiene " + str(num_letras) + " letras.")


#12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
#dd/mm/aaaa y luego imprima su edad en años.
#Utiliza la función .split()

import datetime

fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
fecha_valida = False
while not fecha_valida:
    try:
        dia, mes, anio = fecha_nacimiento.split('/')
        fecha_nacimiento = datetime.date(int(anio), int(mes), int(dia))
        fecha_valida = True
    except ValueError:
        print("Formato de fecha incorrecto. Ingrese la fecha en formato dd/mm/aaaa.")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
fecha_actual = datetime.date.today()
edad = (fecha_actual - fecha_nacimiento) // datetime.timedelta(days=365)
print("Su edad es: " + str(edad) + " años.")

#13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
#imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
edad_en_10_anios = edad + 10
print("Hola " + nombre + ", en 10 años tendrás " + str(edad_en_10_anios) + " años.")

#14-Escribe un programa que solicite al usuario un número entero y luego
#imprima el doble y el triple de ese número.

numero = int(input("Ingrese un número entero: "))
doble = numero * 2
triple = numero * 3
print("El doble de " + str(numero) + " es " + str(doble))
print("El triple de " + str(numero) + " es " + str(triple))

#15-Escribe un programa que solicite al usuario una temperatura en grados
#Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
#La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(str(celsius) + " grados Celsius son equivalentes a " + str(fahrenheit) + " grados Fahrenheit")

#16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
#e imprima su índice de masa corporal (IMC).
#La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print("Tu índice de masa corporal es: ", imc)

#17-Escribe un programa que solicite al usuario dos palabras y luego las imprima
#en orden inverso.
#Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
#"mundo hola".
#Importante!!! Utiliza un solo print() 😈.

palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

print(palabra2, palabra1)

#18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de
#residencia, y lo muestre en pantalla Utilizando una sola línea de código.
#*Recuerda el print() del ejercicio anterior 

print("Nombre:", input("Ingresa tu nombre: "), "Edad:", input("Ingresa tu edad: "), "Ciudad de residencia:", input("Ingresa tu ciudad de residencia: "))

#19-Escribe un programa que solicite al usuario un número decimal y luego
#imprima la parte entera y decimal por separado.

num_decimal = float(input("Ingresa un número decimal: "))
parte_entera = int(num_decimal)
parte_decimal = num_decimal - parte_entera
print("Parte entera:", parte_entera)
print("Parte decimal:", parte_decimal)

## DESAFIO 1 :
#Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
#sus ventas totales y el departamento comercial te solicita que ayudes a los
#vendedores a calcular sus comisiones creando un programa que les pregunte su
#nombre y cuánto han vendido en éste mes.
#Tu programa le va a responder con una frase que incluya su nombre y el monto

#que le corresponde por las comisiones

nombre = input("¿Cuál es tu nombre? ")
ventas = float(input("¿Cuánto has vendido este mes? "))

comisiones = ventas * 0.06

print("¡Hola, " + nombre + "! Este mes has vendido $" + str(ventas) + " y tus comisiones son de $" + str(comisiones) + ". ¡Felicitaciones!")


#  DESAFIO 2 :
#Escribe un programa que solicite al usuario su información personal, incluyendo
#su nombre completo, edad, estatura, peso, dirección y número de teléfono.
#A continuación, el programa deberá imprimir un mensaje con los datos
#ingresados por el usuario en el siguiente formato:
#La información ingresada es la siguiente:
#Nombre completo: [nombre completo]
#Edad: [edad]
#Estatura: [estatura] cm
#Peso: [peso] kg
#Dirección: [dirección]
#Número de teléfono: [número de teléfono]


nombre = input("Ingrese su nombre completo: ")
edad = input("Ingrese su edad: ")
estatura = input("Ingrese su estatura en centímetros: ")
peso = input("Ingrese su peso en kilogramos: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")

print("La información ingresada es la siguiente:")
print("Nombre completo: " + nombre)
print("Edad: " + edad)
print("Estatura: " + estatura + " cm")
print("Peso: " + peso + " kg")
print("Dirección: " + direccion)
print("Número de teléfono: " + telefono)

