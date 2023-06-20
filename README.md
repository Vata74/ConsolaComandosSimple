# Consola Interactiva para Gestión de Archivos

Este proyecto consiste en una consola interactiva para la gestión de archivos en un sistema operativo. Permite realizar diversas acciones como listar directorios y archivos, moverse entre directorios, mostrar el contenido de archivos de texto, copiar y mover archivos, entre otras funcionalidades.

## Instalación
Para utilizar este proyecto, siga los siguientes pasos:

1. Asegúrese de tener Python instalado en su sistema. Puede verificarlo ejecutando el siguiente comando:
```
python --version
```
2. Si no tiene Python instalado, puede descargarlo desde el sitio web oficial de Python o desde la Microsoft Store.

3. Descargue el código fuente del proyecto desde el repositorio en GitHub.

4. Abra una terminal con permisos de administrador y navegue hasta el directorio donde se encuentra el archivo main.py del proyecto.

5. Ejecute los siguientes comandos para instalar las dependencias necesarias.
```
pip install os
pip install platform
pip install shutil
pip install prompt_toolkit
```

6. Ejecute el siguiente comando para iniciar la consola interactiva:
```
python main.py
```

## Uso

Una vez que la consola interactiva esté en funcionamiento, podrá ingresar comandos para realizar diferentes acciones. A continuación, se muestra una lista de comandos disponibles:

- `ayuda`: Muestra información de ayuda y la lista de comandos disponibles.
- `listar`: Lista los directorios y archivos en el directorio actual.
- `info`: Lista los directorios y archivos en el directorio actual junto con información adicional.
- `ir`: Permite moverse a otro directorio.
- `mostrar`: Muestra el contenido de un archivo de texto.
- `copiar`: Copia un archivo a otra ubicación.
- `mover`: Mueve un archivo a otra ubicación.
- `pid`: Muestra el ID de proceso actual.
- `uso`: Muestra el uso de disco actual.
- `creard`: Crea un directorio en la ruta actual.
- `eliminar`: Elimina un archivo vacío en un directorio de forma segura.
- `comprobar`: Verifica la existencia de un directorio.
- `limpiar`: Limpia la pantalla de la consola.
- `creart`: Crea y escribe en un archivo de texto.
- `buscar`: Busca un archivo específico en el directorio seleccionado.
- `cantidad`: Enumera la cantidad de archivos en el directorio seleccionado.
- `cpu`: Muestra información sobre el CPU.
- `python`: Muestra la versión de Python.
- `arquitectura`: Muestra la arquitectura del sistema.
- `permisos`: Muestra los permisos de lectura/escritura de un archivo del directorio actual.
- `abrird`: Abre un directorio.
  

Siga las instrucciones proporcionadas por cada comando para realizar las acciones deseadas.

## Funcionamiento

La consola se encarga de hacer diversas llamadas al sistema, para ello hace uso de las librerías os, platform y shutil.

**Sobre OS:**
La librería nos proporciona funciones para interactuar con el sistema operativo en el que se ejecuta la consola. Permite realizar operaciones relacionadas con archivos, directorios, variables de entorno, procesos y mucho más. 



¡Gracias por utilizar esta consola interactiva para la gestión de archivos!
