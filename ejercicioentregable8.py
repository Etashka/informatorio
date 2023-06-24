from datetime import datetime
import getpass

class Usuario:
    def __init__(self, nombre, apellido, telefono, username, correo, contrasena):
        self.id = None
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.correo = correo
        self.contrasena = contrasena
        self.fecha_registro = datetime.now()
        self.avatar = None
        self.estado = "Activo"
        self.online = False

    def login(self):
        self.online = True
        print("Has iniciado sesión como:", self.username)

    def registrar(self):
        
        pass

class Publico(Usuario):
    def __init__(self, nombre, apellido, telefono, username, correo, contrasena):
        super().__init__(nombre, apellido, telefono, username, correo, contrasena)
        self.es_publico = True

    def comentar(self):
        comentario = input("Ingrese su comentario: ")
        fecha_actual = datetime.now()
        fecha_formato = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        print("Comentario:", comentario)
        print("Usuario:", self.username)
        print("Fecha y hora:", fecha_formato)

    def publicar(self):
        print("Los usuarios públicos no pueden publicar artículos.")

class Colaborador(Usuario):
    def __init__(self, nombre, apellido, telefono, username, correo, contrasena):
        super().__init__(nombre, apellido, telefono, username, correo, contrasena)
        self.es_colaborador = True

    def comentar(self):
        comentario = input("Ingrese su comentario: ")
        fecha_actual = datetime.now()
        fecha_formato = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        print("Comentario:", comentario)
        print("Usuario:", self.username)
        print("Fecha y hora:", fecha_formato)

    def publicar(self):
        titulo = input("Ingrese el título del artículo: ")
        resumen = input("Ingrese el resumen del artículo: ")
        contenido = input("Ingrese el contenido del artículo: ")
        fecha_actual = datetime.now()
        fecha_publicacion = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        # Realiza la lógica de publicación del artículo
        print("Artículo publicado por:", self.username)
        print("Título:", titulo)
        print("Resumen:", resumen)
        print("Contenido:", contenido)
        print("Fecha de publicación:", fecha_publicacion)

def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    telefono = input("Ingrese el teléfono del usuario: ")
    username = input("Ingrese el nombre de usuario: ")
    correo = input("Ingrese el correo electrónico del usuario: ")
    contrasena = getpass.getpass("Ingrese la contraseña del usuario: ")
    usuario = Usuario(nombre, apellido, telefono, username, correo, contrasena)
    print("Usuario registrado con éxito.")

def login_usuario():
    username = input("Ingrese el nombre de usuario: ")
    contrasena = getpass.getpass("Ingrese la contraseña: ")
    if username == "alejandra" and contrasena == "1234":
        usuario = Publico("Alejandra", "Apellido", "123456789", "alejandra", "alejandra@example.com", "1234")
        usuario.login()
        return usuario
    elif username == "nara" and contrasena == "1234":
        usuario = Colaborador("Nara", "Apellido", "123456789", "nara", "nara@example.com", "1234")
        usuario.login()
        return usuario
    else:
        print("Credenciales inválidas.")
        return None

opcion = input("Ingrese '1' para registrar usuarios o '2' para hacer login: ")
usuario = None

if opcion == "1":
    registrar_usuario()
elif opcion == "2":
    usuario = login_usuario()

if usuario:
    if isinstance(usuario, Publico) or isinstance(usuario, Colaborador):
        opcion = input("Ingrese '1' para comentar o '2' para publicar: ")
        if opcion == "1":
            usuario.comentar()
        elif opcion == "2":
            if isinstance(usuario, Colaborador):
                usuario.publicar()
            else:
                print("Los usuarios públicos no pueden publicar.")
    else:
        print("Debes iniciar sesión para realizar acciones.")
