import os
import shutil
import platform
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
    print("Directorio creado")


def eliminar_archivo_vacio_en_directorio(directorio):
    os.rmdir(directorio)
    print("Directorio eliminado")




def corroborar_existencia(directorio):
    if(os.path.exists(directorio)):
        print("Directorio existente")
    else:
        print(f"No existe el directorio {directorio}")


def escribr_en_archivo(nombre_del_archivo):
    # Abre el archivo en modo escritura y escribe el contenido
    nombre_del_archivo_txt = nombre_del_archivo+".txt"
    with open(nombre_del_archivo_txt, 'w') as file:
        file.write(str(input("Ingrese el contenido del archivo de texto: ")))
    print(f"Se ha escrito en el archivo '{nombre_del_archivo}'.")

def clear_screen():
    # Limpia la pantalla según el sistema operativo
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')