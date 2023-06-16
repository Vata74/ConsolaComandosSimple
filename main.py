import os
import platform
import shutil
import time

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


def mostrar_uso_disco():
    try:
        if not os.path.exists(os.getcwd()):
            print("El directorio actual no existe.")
            return
        uso = shutil.disk_usage(os.getcwd())
        print(f"Espacio usado del disco {os.path.splitdrive(os.getcwd())[0]} {round(uso.used / (2 ** 30), 2)} GB")
        print(f"Espacio libre del disco {os.path.splitdrive(os.getcwd())[0]} {round(uso.free / (2 ** 30), 2)} GB")
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
    try:
        if os.path.exists(directorio):
            print("El directorio ya existe.")
            return
        os.mkdir(directorio)
        print("Directorio creado")
    except Exception as e:
        print(f"Error al crear el directorio: {str(e)}")


def eliminar_archivo_vacio_en_directorio(directorio):
    try:
        if not os.path.exists(directorio):
            print("El directorio no existe.")
            return
        if not os.path.isdir(directorio):
            print("No se puede eliminar un archivo vacío en un directorio.")
            return
        os.rmdir(directorio)
        print("Directorio eliminado")
    except Exception as e:
        print(f"Error al eliminar el directorio: {str(e)}")


def corroborar_existencia(directorio):
    if (os.path.exists(directorio)):
        print("Directorio existente")
    else:
        print(f"No existe el directorio {directorio}")


def escribir_en_archivo(nombre_del_archivo):
    # Abre el archivo en modo escritura y escribe el contenido
    nombre_del_archivo_txt = nombre_del_archivo + ".txt"
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
    '''
    comandos = [
        ("AYUDA", "Proporciona información de Ayuda para los comandos\n"),
        ("------------------DIRECTORIOS------------------"),
        ("LISTAR", "Listar directorios y archivos (solo nombres)"),
        ("INFO", "Listar directorios y archivos (nombres e información extra)"),
        ("IR", "Moverse de un directorio a otro"),
        ("CREARD", "Crear un directorio en la ruta actual"),
        ("COMPROBAR", "Corrobrar existencia de un directorio\n"),
        ("------------------ARCHIVOS---------------------"),
        ("CREART", "Crear y escribir un archivo de texto"),
        ("MOSTRAR", "Mostrar archivo de texto"),
        ("ELIMINAR", "Eliminar archivo vacío en directorio (MODO SEGURO)"),
        ("COPIAR", "Copiar archivos"),
        ("MOVER", "Mover archivos\n"),
        ("------------------ALMACENAMIENTO----------------"),
        ("USO", "Revisar el uso de disco en el directorio actual\n"),
        ("------------------BÚSQUEDA----------------------"),
        ("BUSCAR", "Buscar un archivo en el directorio"),
        ("CANTIDAD", "Cantidad de archivos en el directorio\n"),
        ("------------------CONSOLA-----------------------"),
        ("LIMPIAR", "Limpiar pantalla de la consola"),
        ("SALIR", "Salir de la consola"),
        ("------------------PID---------------------------"),
        ("PID", "Mostrar PID del proceso")
    ]
    print("")
    print("Consola interactiva - Comandos disponibles:")
    print("")
    for comando, descripcion in comandos:
        print(f"{comando.ljust(23)}{descripcion}")
    print("")
    '''

    #Perdón vata, saqué lo otro porque no me estaba funcionando bien, si querés cambiarlo cambialo

    print("AYUDA Proporciona información de Ayuda para los comandos\n\n "
                "------------------DIRECTORIOS------------------\n"
                "LISTAR Listar directorios y archivos (solo nombres)\n"          
                "INFO Listar directorios y archivos (nombres e información extra)\n"
                "IR Moverse de un directorio a otro\n"
                "CREARD Crear un directorio en la ruta actual\n"
                "COMPROBAR Corrobrar existencia de un directorio\n\n"
                "------------------ARCHIVOS---------------------\n"
                "CREART Crear y escribir un archivo de texto\n"
                "MOSTRAR Mostrar archivo de texto\n"
                "ELIMINAR Eliminar archivo vacío en directorio (MODO SEGURO)\n"
                "COPIAR Copiar archivos\n"
                "MOVER Mover archivos\n\n"
                "------------------CPU---------------------\n"
                "CPU Ver detalles del cpu\n\n"
                "------------------SISTEMA---------------------\n"
                "ARQUITECTURA Ver arquitectura del sistema\n"
                "PERMISOS Ver los permisos de lectura/escritura de un archivo del directorio actual\n\n"
                "------------------ALMACENAMIENTO----------------\n"
                "USO Revisar el uso de disco actual\n\n"
                "------------------PYTHON----------------\n"
                "PYTHON Versión de Python\n\n"
                "------------------BÚSQUEDA----------------------\n"
                "BUSCAR Buscar un archivo en el directorio\n"
                "CANTIDAD Cantidad de archivos en el directorio\n\n"
                "------------------CONSOLA-----------------------\n"
                "LIMPIAR Limpiar pantalla de la consola\n"
                "SALIR Salir de la consola\n\n"
                "------------------PID---------------------------\n"
                "PID Mostrar PID del proceso\n\n")

def buscar_archivo(nombre_archivo):
    for root, dirs, files in os.walk(os.getcwd()):
        if nombre_archivo in files:
            print(f"Archivo {nombre_archivo} encontrado en {root}.")
            return
    print(f"No se encontró el archivo {nombre_archivo}.")


def obtener_cantidad_archivos(directorio):
    if not os.path.isdir(directorio):
        print("El directorio especificado no existe.")
        return

    lista_elementos = os.listdir(directorio)
    cantidad_archivos = 0

    for elemento in lista_elementos:
        ruta_elemento = os.path.join(directorio, elemento)
        if os.path.isfile(ruta_elemento):
            cantidad_archivos += 1

    return cantidad_archivos

def info_cpu():
    print(f" Cantidad de núcleos del cpu: {os.cpu_count()}")
    print(f" Información detallada: {platform.processor()}")

def arquitectura_del_sistema():
    print(f"Arquitectura del sistema: {platform.architecture()})")
    print(f"Detalles del sistema: {platform.uname()}")

def version_de_python():
    print(f"Versión de Python: {platform.python_version()}")
    print(f"Compilador de Python: {platform.python_compiler()}")

def ver_permisos(archivo):

    if(os.path.exists(archivo)):
        if(os.access(archivo, os.R_OK)):
            print(f"Tienes permiso de lectura en el archivo {archivo}")
        if(os.access(archivo, os.W_OK)):
            print(f"Tienes permiso de escritura en el archivo {archivo}")
        if not (os.access(archivo, os.W_OK)) and not (os.access(archivo, os.R_OK)):
            print(f"No tienes permisos de lectura ni de escritura en el archivo {archivo}")
    else:
        print(f"El archivo {archivo} no existe")

def ejecutar_comando(comando):
    if comando == "ayuda":
        mostrar_menu()

    elif comando == 'listar':
        listar_directorios_archivos()

    elif comando == 'info':
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
        escribir_en_archivo(str(input("Ingrese el nombre del archivo a crear: ")))

    elif comando == 'buscar':
        argumento = str(input())
        buscar_archivo(argumento)

    elif comando == 'cantidad':
        print(f"Cantidad de archivos en el directorio: {obtener_cantidad_archivos(os.getcwd())}")

    elif comando == 'cpu':
        info_cpu()

    elif comando == 'arquitectura':
        arquitectura_del_sistema()

    elif comando == 'python':
        version_de_python()

    elif comando == 'permisos':
        ver_permisos(str(input("Ingrese el nombre del archivo: ")))

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
        # La consola en español funciona solamente en la consola del sistema
        # operativo usando "python main.py" desde la ruta del proyecyo, pero
        # ya funciona el autocompletado

        # Anotación, hay algunas funciones que no se ejecutan correctamente si
        # la cmd no se ejecuta como admin. En windows es tan simple como ejecutar
        # el cmd como administrador y escribir el comando "python main.py"; en
        # linux se puede hacer con el comando "sudo python main.py" desde la ruta
        # del proyecto

        comando = prompt(f"{directorio}> ", completer=completer)
        if not ejecutar_comando(comando.lower()):
            break


# Este array sirve para el autocompletar
comandos = [
    "ayuda",
    "listar",
    "info",
    "ir",
    "mostrar",
    "copiar",
    "mover",
    "pid",
    "uso",
    "creard",
    "eliminar",
    "comprobar",
    "limpiar",
    "creart",
    "salir",
    "buscar",
    "cantidad",
    "cpu",
    "python",
    "arquitectura",
    "permisos"
]

comandos_mayusculas = [comando.upper() for comando in comandos]
comandos.extend(comandos_mayusculas)
completer = WordCompleter(comandos)

consola()
