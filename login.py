#Lo propuesto por el profesor en clases fue crear un login con listas, aquí dejo mi idea

#Creo la lista con los usuarios
usuarios = ["pepe", "juan", "vilma"]
#Creo la lista con las contraseñas 
contraseñas = ["pepe", "juan", "vilma"]
#Solicito usuario y contraseña del usuario
usuario_ingresado = input("Ingresa tu nombre de usuario: ")
contraseña_ingresada = input("Ingresa tu contraseña: ")
#Inicio el IF si el usuario ingresado está en el sistema
if usuario_ingresado in usuarios:
    # busco el índice del elemento "usuario_ingresado" dentro de la lista "usuarios"
    # (necesario para acceder a la contraseña correspondiente al usuario ingresado en la lista "contraseñas")
    indice_usuario = usuarios.index(usuario_ingresado)
    #Comparo si la contraseña es igual a la que está en la lista
    if contraseña_ingresada == contraseñas[indice_usuario]:
        #Imprimo resultado exitoso
        print("Inicio de sesión exitoso")
    else:
        print("Contraseña incorrecta")
        #Indico que el usuario no se encuentra
else:
    print("El usuario ingresado no existe")

############################################################################################

# Tambien se lo podría hacer con diccionarios

usuarios = {
    "juan": "juan",
    "pepe": "pepe20",
    "maria": "maria20"
}
#Solicito que ingrese usuario
usuario_ingresado = input("Ingresa tu nombre de usuario: ")
#Verifico si el usuario ingresado está en la lista
if usuario_ingresado in usuarios:
    #Si está en la lista solicito la contraseña
    contraseña_ingresada = input("Ingresa tu contraseña: ")
    #Comparo si las contraseñas son correctas
    if usuarios[usuario_ingresado] == contraseña_ingresada:
        print("Inicio de sesión exitoso")
    else:

        print("Contraseña incorrecta")
#Si el usuario no está en la lista entonces le pregunto si quiere hacer un usuario nuevo        
else:
    crear_usuario = input("El usuario ingresado no existe, ¿deseas crear un nuevo usuario? (s/n): ")
    if crear_usuario == "s":
        #pedimos la contraseña
        contraseña_nueva = input("Ingresa una contraseña para tu nuevo usuario: ")
        # guardamos el usuario que puso el cliente al comienzo
        usuarios[usuario_ingresado] = contraseña_nueva
        print("Nuevo usuario creado con éxito")
    else:
        print("Inicio de sesión cancelado")


############################################################################################

numeros = input("Introduce 3 números separados por espacios: ")
num1, num2, num3 = numeros.split()

if num1 >= num2 and num1 >= num3:
    mas_grande = num1
elif num2 >= num1 and num2 >= num3:
    mas_grande = num2
else:
    mas_grande = num3

print("El número más grande es:", mas_grande)