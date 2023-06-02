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
    print("9. Crear un directorio en el path actual")
    print("10. Eliminar archivo vacío en directorio (MODO SEGURO)")
    print("11. Corrobrar existencia de un directorio")
    print("12. Limpiar pantalla de la consola")
    print("13. Crear un archivo de texto y escribir en el mismo")
    print("30. Salir")


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
        mostrar_uso_disco()

    elif comando == '9':
        print("Ingrese el nombre del directorio a crear: ")
        crear_archivo_en_directorio(str(input()))

    elif comando == '10':
        # Este puede romperme la pc así que probemoslo con cuidado
        print("Ingrese el nombre del archivo vacío a borrar (modo seguro)")
        eliminar_archivo_vacio_en_directorio(os.getcwd())

    elif comando == '11':
        print("Ingrese el directorio a corroborar")
        corroborar_existencia(str(input()))

    elif comando == '12':
        # Funciona únicamente en el cmd
        clear_screen()

    elif comando == '13':
        escribr_en_archivo(str(input("Ingrese el nombre del archivo a crear en el directorio actual: ")))

    elif comando == '30':
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
