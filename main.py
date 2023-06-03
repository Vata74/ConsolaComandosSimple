import os
import shutil
import platform
import subprocess
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


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
        if not os.path.exists(archivo):
            print("El archivo especificado no existe.")
            return
        if os.path.isdir(archivo):
            print("No se puede mostrar un directorio como archivo de texto.")
            return
        with open(archivo, 'r') as file:
            contenido = file.read()
            print(f"Contenido de {archivo}:\n{contenido}")
    except Exception as e:
        print(f"Error al mostrar el archivo de texto: {str(e)}")


# Agrega estas comprobaciones en la función mostrar_uso_disco()

def mostrar_uso_disco():
    try:
        if not os.path.exists(os.getcwd()):
            print("El directorio actual no existe.")
            return
        uso = shutil.disk_usage(os.getcwd())
        print(os.getcwd())
        print(f"Espacio usado del disco {os.path.splitdrive(os.getcwd())[0]} {round(uso.used / (2**30), 2)} GB")
        print(f"Espacio libre del disco {os.path.splitdrive(os.getcwd())[0]} {round(uso.free / (2**30), 2)} GB")
    except Exception as e:
        print(f"Error al mostrar el uso de disco: {str(e)}")



def copiar_archivo(origen, destino):
    try:
        if not os.path.exists(origen):
            print("El archivo de origen no existe.")
            return
        if os.path.isdir(origen):
            print("No se puede copiar un directorio.")
            return
        shutil.copy2(origen, destino)
        print(f"Archivo {origen} copiado a {destino}.")
    except shutil.SameFileError:
        print("El archivo de destino es el mismo que el de origen.")
    except Exception as e:
        print(f"Error al copiar el archivo: {str(e)}")


def mover_archivo(origen, destino):
    try:
        if not os.path.exists(origen):
            print("El archivo de origen no existe.")
            return
        if os.path.isdir(origen):
            print("No se puede mover un directorio.")
            return
        shutil.move(origen, destino)
        print(f"Archivo {origen} movido a {destino}.")
    except Exception as e:
        print(f"Error al mover el archivo: {str(e)}")


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
    comandos = [
        ("LISTAR", "Listar directorios y archivos (solo nombres)"),
        ("INFORMACION", "Listar directorios y archivos (nombres e información extra)"),
        ("IR", "Moverse de un directorio a otro"),
        ("MOSTRAR", "Mostrar archivo de texto"),
        ("COPIAR", "Copiar archivos"),
        ("MOVER", "Mover archivos"),
        ("PID", "Mostrar PID del proceso"),
        ("USODISCO", "Revisar el uso de disco"),
        ("CREARD", "Crear un directorio en el path actual"),
        ("ELIMINAR", "Eliminar archivo vacío en directorio (MODO SEGURO)"),
        ("COMPROBAR", "Corrobrar existencia de un directorio"),
        ("LIMPIAR", "Limpiar pantalla de la consola"),
        ("CREART", "Crear un archivo de texto y escribir en el mismo"),
        ("SALIR", "Salir")
    ]
    print("")
    print("Consola interactiva - Comandos disponibles:")
    print("")
    for comando, descripcion in comandos:
        print(f"{comando.ljust(15)}{descripcion}")
    print("")


def ejecutar_comando(comando):
    if comando == "ayuda":
        mostrar_menu()

    elif comando == 'listar':
        listar_directorios_archivos()

    elif comando == 'informacion':
        listar_directorios_archivos(nombres_extra=True)

    elif comando == 'ir':
        directorio = input("Ingrese el directorio al que desea moverse: ")
        moverse_directorio(directorio)

    elif comando == 'mostrar':
        archivo = input("Ingrese el archivo de texto que desea mostrar: ")
        mostrar_archivo_texto(archivo)

    elif comando == 'copiar':
        origen = input("Ingrese la ruta del archivo que desea copiar: ")
        destino = input("Ingrese la ruta de destino para la copia: ")
        copiar_archivo(origen, destino)

    elif comando == 'mover':
        origen = input("Ingrese la ruta del archivo que desea mover: ")
        destino = input("Ingrese la ruta de destino para el movimiento: ")
        mover_archivo(origen, destino)

    elif comando == 'pid':
        mostrar_pid()

    elif comando == 'uso':
        mostrar_uso_disco()

    elif comando == 'creard':
        print("Ingrese el nombre del directorio a crear: ")
        crear_archivo_en_directorio(str(input()))

    elif comando == 'eliminar':
        # Este puede romperme la pc así que probemoslo con cuidado
        print("Ingrese el nombre del archivo vacío a borrar (modo seguro)")
        eliminar_archivo_vacio_en_directorio(os.getcwd())

    elif comando == 'comprobar':
        print("Ingrese el directorio a comprobar")
        corroborar_existencia(str(input()))

    elif comando == 'limpiar':
        clear_screen()

    elif comando == 'creart':
        escribr_en_archivo(str(input("Ingrese el nombre del archivo a crear en el directorio actual: ")))

    elif comando == 'salir':
        print("¡Hasta luego!")
        return False
    else:
        print("Comando inválido. Intente nuevamente.")

    return True


def consola():
    mostrar_pid()

    while True:
        directorio = os.getcwd()
        # AHORA FUNCIONA SOLAMENTE EN LA CONSOLA EJECUTANDO CON "python main.py"
        # PERO YA FUNCIONA EL AUTOCOMPLETADO
        comando = prompt(f"{directorio}> ", completer=completer)
        if not ejecutar_comando(comando.lower()):
            break


comandos = [
    "ayuda",
    "listar",
    "informacion",
    "ir",
    "mostrar",
    "copiar",
    "mover",
    "pid",
    "usodisco",
    "creard",
    "eliminar",
    "comprobar",
    "limpiar",
    "creart",
    "salir"
]

comandos_mayusculas = [comando.upper() for comando in comandos]
comandos.extend(comandos_mayusculas)
completer = WordCompleter(comandos)

consola()
