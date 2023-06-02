import os
import shutil
import subprocess

def listar_directorios_archivos(nombres_extra=False):
    if nombres_extra:
        for item in os.listdir():
            ruta = os.path.abspath(item)
            info = os.stat(item)
            print(f"Nombre: {item}")
            print(f"Tamaño: {info.st_size} bytes")
            print(f"Permisos: {info.st_mode}")
            print(f"Ruta: {ruta}\n")
    else:
        for item in os.listdir():
            print(item)


def moverse_directorio(directorio):
    try:
        os.chdir(directorio)
        print(f"Directorio actual: {os.getcwd()}")
    except FileNotFoundError:
        print("El directorio especificado no existe.")


def mostrar_archivo_texto(archivo):
    try:
        with open(archivo, 'r') as file:
            contenido = file.read()
            print(f"Contenido de {archivo}:\n{contenido}")
    except FileNotFoundError:
        print("El archivo especificado no existe.")
    except IsADirectoryError:
        print("No se puede mostrar un directorio como archivo de texto.")



def mostrar_uso_disco():
    try:
        uso = shutil.disk_usage(os.getcwd())
        print(os.getcwd())
        print(f"Espacio usado del disco {os.path.splitdrive(os.getcwd())[0]} {round(uso.used / (2**30), 2)} GB")
        print(f"Espacio libre del disco {os.path.splitdrive(os.getcwd())[0]} {round(uso.free / (2**30), 2)} GB")
    except FileNotFoundError:
        print("Archivo no encontrado")

def copiar_archivo(origen, destino):
    try:

        shutil.copy2(origen, destino)
        print(f"Archivo copiado de {origen} a {destino}.")
    except FileNotFoundError:
        print("El archivo de origen no existe.")
    except shutil.SameFileError:
        print("El archivo de destino es el mismo que el de origen.")
    except IsADirectoryError:
        print("No se puede copiar un directorio.")


def mover_archivo(origen, destino):
    try:
        shutil.move(origen, destino)
        print(f"Archivo movido de {origen} a {destino}.")
    except FileNotFoundError:
        print("El archivo de origen no existe.")
    except shutil.Error as e:
        print(f"Error al mover el archivo: {e}")


def mostrar_pid():
    pid = os.getpid()
    print(f"El PID del proceso actual es: {pid}")


def crear_archivo_en_directorio(directorio):
    os.mkdir(directorio)

def mostrar_menu():
    print("Consola interactiva - Comandos disponibles:")
    print("1. Listar directorios y archivos (solo nombres)")
    print("2. Listar directorios y archivos (nombres e información extra)")
    print("3. Moverse de un directorio a otro")
    print("4. Mostrar archivo de texto")
    print("5. Copiar archivos")
    print("6. Mover archivos")
    print("7. Mostrar PID del proceso")
    print("8. Revisar el uso de disco")
    print("11. Salir")


def ejecutar_comando(comando):
    if comando == "ayuda":
        mostrar_menu()

    elif comando == '1':
        listar_directorios_archivos()
    elif comando == '2':
        listar_directorios_archivos(nombres_extra=True)
    elif comando == '3':
        directorio = input("Ingrese el directorio al que desea moverse: ")
        moverse_directorio(directorio)
    elif comando == '4':
        archivo = input("Ingrese el archivo de texto que desea mostrar: ")
        mostrar_archivo_texto(archivo)
    elif comando == '5':
        origen = input("Ingrese la ruta del archivo que desea copiar: ")
        destino = input("Ingrese la ruta de destino para la copia: ")
        copiar_archivo(origen, destino)
    elif comando == '6':
        origen = input("Ingrese la ruta del archivo que desea mover: ")
        destino = input("Ingrese la ruta de destino para el movimiento: ")
        mover_archivo(origen, destino)
    elif comando == '7':
        mostrar_pid()
    elif comando == '8':
        # destino = input("Ingrese la ruta absoluta para ver el uso de disco en ella")
        mostrar_uso_disco()

    elif comando == '9':
        print("Ingrese el nombre del directorio a crear: ")
        crear_archivo_en_directorio(str(input()))

    elif comando == '11':
        print("¡Hasta luego!")
        return False
    else:
        print("Comando inválido. Intente nuevamente.")

    return True


def consola():
    mostrar_pid()
    while True:

        directorio = os.getcwd()
        print(os.getcwd(), end="> ")
        comando = str(input())
        if not ejecutar_comando(comando):
            break


consola()
