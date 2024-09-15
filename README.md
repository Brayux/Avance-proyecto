# Avance Proyecto

| Nombre                       | Identificación |      Grupo      |      Carrera        |
|------------------------------|----------------|-----------------|---------------------|
| Brayan Andres Guerrero Cortés| 1011201494     |                 |                     |
| Daniel Santiago Barrera Rojas| 1031647812     |   ProGreening   | Ingeniería Agrícola |
| Pablo Mendoza Malagón        | 1072645448     |                 |                     |

[![Imagen-de-Whats-App-2024-04-18-a-las-13-37-14-41369a78.jpg](https://i.postimg.cc/MKtYzt5J/Imagen-de-Whats-App-2024-04-18-a-las-13-37-14-41369a78.jpg)](https://postimg.cc/CzB8NG9c)
<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>- ProGreening - </b></th>
  </tr>

 ## Proyecto Programacion de computadores:

## **Sopa de letras**

Construir una aplicación que emule una sopa de letras utilizando Python.
Condiciones:
- Código original
- Uso de herramientas vistas en el curso
- interacción y manejo a través de la consola
- Definido por el usuario:
Matriz del tamaño de la sopa de letras (Min: 10x10, Max: 30x30)
Ingreso de las palabras: Lista de coordenadas, Strings.
Nivel de dificultad: Asociado a cantidad de palabras, verticales, horizontales, diagonales.

## Features extra:
- Cuenta regresiva
- Sombreado o cambio visual de las palabras encontradas
- Interfaz gráfica con estructura

## Codigo hasta el momento:
````python


```
## Listas y Diccionarios:

letras_posibles: Lista con todas las letras del alfabeto en mayúscula. Se utiliza para rellenar la sopa de letras en posiciones vacías.

dificil, medio, facil: Diccionarios que contienen palabras de programación categorizadas por dificultad. Cada clave y valor es una palabra en mayúscula.

lista_palabras_usuario y lista_palabras_personalizada: Diccionarios para almacenar palabras personalizadas por el usuario.

lista_palabras: Diccionario que se utilizará para contener las palabras que realmente serán insertadas en la sopa.

palabras_buscar: Lista que almacena las palabras que el usuario debe buscar en la sopa.
rotaciones: Diccionario que contiene las direcciones posibles en las que las palabras pueden colocarse en la sopa. Cada clave corresponde a una dirección específica (horizontal, vertical, diagonal).

rotaciones_posibles: Lista que almacenará las rotaciones que se aplicarán para colocar las palabras en la sopa.

Este flujo permite al usuario interactuar con la sopa de letras, buscar palabras, y recibir retroalimentación sobre si las ha encontrado correctamente o no. La implementación de cada función y la estructura del programa permiten que el proceso de generación, personalización y resolución de la sopa de letras sea dinámico y flexible.

En el código, las orientaciones posibles están definidas en la variable rotaciones_posibles, que contiene cuatro tuplas que representan las direcciones en las que se puede colocar una palabra en la sopa de letras. Cada tupla está compuesta por dos valores:

El primer valor de la tupla indica el cambio en la fila (dirección vertical).

El segundo valor de la tupla indica el cambio en la columna (dirección horizontal).
Veamos cada orientación:
## **1. (0, 1) - Horizontal (de izquierda a derecha)**
Fila: No cambia (0), la palabra se coloca en la misma fila.
Columna: Aumenta en 1, lo que significa que la palabra se escribe hacia la derecha.
## **2. (0, -1) - Horizontal (de derecha a izquierda)**
Fila: No cambia (0), la palabra se coloca en la misma fila.
Columna: Disminuye en 1, lo que significa que la palabra se escribe hacia la izquierda.
## **3. (1, 0) - Vertical (de arriba hacia abajo)**
Fila: Aumenta en 1, lo que significa que la palabra se coloca hacia abajo.
Columna: No cambia (0), la palabra se coloca en la misma columna.
## **4. (-1, 0) - Vertical (de abajo hacia arriba)**
Fila: Disminuye en 1, lo que significa que la palabra se coloca hacia arriba.
Columna: No cambia (0), la palabra se coloca en la misma columna.
## **5. (1, 1) - Diagonal descendente (de arriba a la izquierda hacia abajo a la derecha)**
Fila: Aumenta en 1, lo que significa que la palabra se coloca hacia abajo.
Columna: Aumenta en 1, lo que significa que la palabra se coloca hacia la derecha.
## **6. (-1, -1) - Diagonal ascendente (de abajo a la derecha hacia arriba a la izquierda)**

Fila: Disminuye en 1, lo que significa que la palabra se coloca hacia arriba.

Columna: Disminuye en 1, lo que significa que la palabra se coloca hacia la izquierda.

## **7. (1, -1) - Diagonal descendente (de arriba a la derecha hacia abajo a la izquierda)**
Fila: Aumenta en 1, lo que significa que la palabra se coloca hacia abajo.

Columna: Disminuye en 1, lo que significa que la palabra se coloca hacia la izquierda.
## **8. (-1, 1) - Diagonal ascendente (de abajo a la izquierda hacia arriba a la derecha)**

Fila: Disminuye en 1, lo que significa que la palabra se coloca hacia arriba.

Columna: Aumenta en 1, lo que significa que la palabra se coloca hacia la derecha.

Resumen:
Estas ocho orientaciones permiten colocar palabras en una sopa de letras de forma horizontal, vertical y diagonal en ambas direcciones, lo que incrementa la dificultad y diversidad del juego.

Horizontal:

(0, 1) → Izquierda a derecha.

(0, -1) → Derecha a izquierda.

Vertical:

(1, 0) → Arriba hacia abajo.

(-1, 0) → Abajo hacia arriba.

Diagonal descendente:

(1, 1) → Arriba a la izquierda hacia abajo a la derecha.

(1, -1) → Arriba a la derecha hacia abajo a la izquierda.

Diagonal ascendente:

(-1, 1) → Abajo a la izquierda hacia arriba a la derecha.

(-1, -1) → Abajo a la derecha hacia arriba a la izquierda.


## Funciones
## **1. generar_sopa_de_letras(filas, columnas)**
Esta función genera una sopa de letras vacía con las dimensiones especificadas por los parámetros filas y columnas.

Entrada: Número de filas y columnas.

Salida: Un diccionario donde cada clave es una tupla (fila, columna) que representa la posición en la sopa de letras, y el valor es un '-', indicando que esa posición está vacía.
```python
def generar_sopa_de_letras(filas, columnas):
    sopa_de_letras = {}
    for fila in range(filas):
        for columna in range(columnas):
            sopa_de_letras[(fila, columna)] = '-'  # Inicialmente, todas las posiciones están vacías
    return sopa_de_letras
```
## **2. imprimir_sopa_de_letras(sopa_de_letras, filas, columnas)**
Esta función imprime la sopa de letras en la consola.

Entrada: La sopa de letras (un diccionario), el número de filas y columnas.

Salida: No tiene retorno, pero imprime la sopa de letras en formato de matriz.

```python
def imprimir_sopa_de_letras(sopa_de_letras, filas, columnas):
    for fila in range(filas):
        for columna in range(columnas):
            print(sopa_de_letras[(fila, columna)], end=' ')  # Imprimir cada letra seguida de un espacio
        print()
```
## **3. reemplazar_letra(sopa_de_letras, fila, columna, nueva_letra)**
Esta función reemplaza el valor de una posición específica en la sopa de letras.

Entrada: La sopa de letras, las coordenadas (fila, columna), y la nueva letra a colocar.

Salida: No retorna nada, pero actualiza el diccionario de la sopa de letras.
```python
def reemplazar_letra(sopa_de_letras, fila, columna, nueva_letra):
    sopa_de_letras[(fila, columna)] = nueva_letra.lower()  # Reemplaza la letra en la posición dada
```
## **4. escoger_separar_en_lista(letras_palabra)**
Esta función elige una palabra aleatoria de la lista de palabras, la separa en letras, y la elimina de la lista original para evitar duplicados.

Entrada: Una lista vacía (que luego se llenará con letras de la palabra).

Salida: La palabra seleccionada y la lista de letras que componen esa palabra.
```python
def escoger_separar_en_lista(letras_palabra):
    palabra = random.choice(list(lista_palabras.keys()))  # Elegir una palabra al azar
    palabras_buscar.append(palabra)  # Agregar la palabra a la lista de palabras a buscar
    letras_palabra = list(palabra)  # Separar la palabra en letras
    cantidad_palabras = len(letras_palabra)  # Contar el número de letras
    del lista_palabras[palabra]  # Eliminar la palabra del diccionario original
    return palabra, letras_palabra
```

## **5. priorizar_lista_usuario(lista_palabras, lista_palabras_usuario)**
Esta función añade las palabras personalizadas del usuario a la lista principal de palabras.
Entrada: La lista principal de palabras y la lista de palabras del usuario.
Salida: La lista de palabras actualizada, incluyendo las del usuario.
```python
def priorizar_lista_usuario(lista_palabras, lista_palabras_usuario):
    for palabra in lista_palabras_usuario:
        lista_palabras[palabra] = lista_palabras_usuario[palabra]  # Añadir las palabras del usuario a la lista principal
    return lista_palabras
```
## **6. colocar_en_sopa(sopa_de_letras, letras_palabra, filas, columnas, direccion_fila, direccion_columna)**
Esta función coloca una palabra en la sopa de letras en la dirección especificada.

Entrada: La sopa de letras, la lista de letras de la palabra, las dimensiones de la sopa, y la dirección (horizontal, vertical o diagonal).

Salida: No retorna nada, pero actualiza la sopa de letras con la palabra colocada.

```python
def colocar_en_sopa(sopa_de_letras, letras_palabra, filas, columnas, direccion_fila, direccion_columna):
    while True:
        # Escoger una posición inicial al azar
        inicio_fila = random.randint(0, filas - 1)
        inicio_columna = random.randint(0, columnas -1)
        # Validar si hay espacio para la palabra
        if validar_espacio(sopa_de_letras, letras_palabra, filas, columnas, inicio_fila, inicio_columna, direccion_fila, direccion_columna):
            contador = 0
            # Colocar las letras de la palabra en la sopa de letras
            for letra in letras_palabra:
                nueva_fila = inicio_fila + contador *direccion_fila
                nueva_columna = inicio_columna + contador *direccion_columna
                reemplazar_letra(sopa_de_letras, nueva_fila, nueva_columna, letra)
                contador += 1
            break

```
**Descripción:** Coloca una palabra en la sopa de letras en la dirección especificada.
**Parámetros:**

sopa_de_letras: La sopa de letras.

letras_palabra: Lista de letras de la palabra a colocar.

filas: Número de filas de la sopa.

columnas: Número de columnas de la sopa.

direccion_fila: Dirección en la que se moverá por las filas.

direccion_columna: Dirección en la que se moverá por las columnas.

Proceso:

Selecciona una posición de inicio aleatoria.

Verifica si hay suficiente espacio para colocar la palabra usando validar_espacio.
Coloca la palabra letra por letra en la dirección especificada.

Retorno:
La función no devuelve ningún valor. Solo modifica sopa_de_letras.

## **7. validar_espacio(sopa_de_letras, letras_palabra, filas, columnas, inicio_fila, inicio_columna, direccion_fila, direccion_columna)**
Esta función verifica si hay suficiente espacio en la dirección deseada para colocar una palabra sin que se salga de los límites o se superponga con otras palabras.

Entrada: La sopa de letras, la lista de letras de la palabra, las dimensiones de la sopa, la posición inicial y la dirección.

Salida: True si hay espacio suficiente, False si no lo hay.

## **8. configurar_dificultad(dificultad)**
Descripción: Configura la dificultad de la sopa de letras.

Parámetros:

dificultad: Nivel de dificultad (FACIL, MEDIO, DIFICIL).

Proceso:

Devuelve diferentes configuraciones (tamaño de la sopa, número de palabras, rotaciones posibles, lista de palabras) dependiendo del nivel de dificultad seleccionado.

Retorno:

Devuelve un conjunto de configuraciones: filas, columnas, cantidad_palabras_sopa, rotaciones_posibles, lista_palabras.

## **9. llenar_con_aleatorias(sopa_de_letras, filas, columnas)**
Esta función llena las posiciones vacías de la sopa de letras con letras aleatorias.

Entrada: La sopa de letras y sus dimensiones.

Salida: No retorna nada, pero actualiza la sopa de letras con caracteres aleatorios en las posiciones vacías.
Declaracion “main”:

## Inicio programa

## **1. Importación de Módulos**
```python
import random
from colorama import Fore, Style

random: Se usa para generar valores aleatorios, como seleccionar palabras o posiciones en la sopa de letras.
colorama: Se utiliza para manejar el color de la salida en la consola. Fore se usa para cambiar el color del texto, y Style para reiniciar el estilo al normal.
```
## **2. Inicio del Programa**

```python

print("Bienvenido a la sopa de letras")
print("Seleccione un nivel de dificultad: FACIL, MEDIO, DIFICIL")

El programa comienza dando la bienvenida al usuario e indicando que debe seleccionar un nivel de dificultad.
```
## **3. Selección de la Dificultad**
```python
dificultad = input("Ingrese la dificultad: ").upper()
filas, columnas, cantidad_palabras_sopa, rotaciones_posibles, lista_palabras = configurar_dificultad(dificultad)

dificultad: El usuario ingresa un nivel de dificultad (FACIL, MEDIO, DIFICIL).
configurar_dificultad(dificultad): Esta función, explicada anteriormente, devuelve las configuraciones correspondientes al nivel de dificultad seleccionado.
filas y columnas: Tamaño de la sopa de letras.
cantidad_palabras_sopa: Número de palabras que se colocarán en la sopa.
rotaciones_posibles: Direcciones posibles para colocar las palabras (horizontal, vertical, diagonal).
lista_palabras: Lista de palabras que se utilizarán.
```
## **4. Generación de la Sopa de Letras**
```python
sopa_de_letras = generar_sopa_de_letras(filas, columnas)

Se llama a la función generar_sopa_de_letras para crear una sopa de letras vacía con las dimensiones especificadas.
```
## **5. Ingreso de Palabras Personalizadas (Opcional)**
```python

personalizadas = input("¿Desea agregar palabras personalizadas? (SI/NO): ").upper()

if personalizadas == "SI":
    cantidad_palabras_usuario = int(input("¿Cuántas palabras desea agregar?: "))
    lista_palabras_usuario = [input("Ingrese la palabra: ").upper() for _ in range(cantidad_palabras_usuario)]
    lista_palabras = priorizar_lista_usuario(lista_palabras, lista_palabras_usuario)

El usuario tiene la opción de agregar palabras personalizadas.
personalizadas: Pregunta al usuario si quiere agregar palabras personalizadas.
priorizar_lista_usuario: Esta función combina las palabras personalizadas con la lista principal, dando prioridad a las personalizadas.
```
## **6. Colocación de Palabras en la Sopa de Letras**
```python
for _ in range(cantidad_palabras_sopa):
    palabra, letras_palabra = escoger_separar_en_lista([])
    colocada = False
    while not colocada:
        direccion_fila, direccion_columna = random.choice(rotaciones_posibles)
        inicio_fila = random.randint(0, filas - 1)
        inicio_columna = random.randint(0, columnas - 1)
        if validar_espacio(sopa_de_letras, letras_palabra, filas, columnas, inicio_fila, inicio_columna, direccion_fila, direccion_columna):
            colocar_en_sopa(sopa_de_letras, letras_palabra, filas, columnas, direccion_fila, direccion_columna)
            colocada = True
```
Este bloque se encarga de colocar las palabras en la sopa de letras.

escoger_separar_en_lista: Selecciona una palabra al azar de la lista y la separa en letras.
while not colocada: Intenta colocar la palabra en la sopa de letras hasta que encuentre un lugar adecuado.

random.choice(rotaciones_posibles): Selecciona una dirección al azar en la que se colocará la palabra.

random.randint: Selecciona una posición inicial al azar dentro de los límites de la sopa de letras.

validar_espacio: Verifica si hay suficiente espacio para colocar la palabra.

colocar_en_sopa: Coloca la palabra en la sopa de letras.

## **7. Llenado de Espacios Vacíos con Letras Aleatorias**
```python
llenar_con_aleatorias(sopa_de_letras, filas, columnas)

Llena todos los espacios vacíos en la sopa de letras (marcados con '-') con letras aleatorias para completar la sopa.
```
## **8. Impresión de la Sopa de Letras**
```python
imprimir_sopa_de_letras(sopa_de_letras, filas, columnas)

Imprime la sopa de letras en la consola para que el usuario la vea y comience a buscar las palabras.
```
## **9. Búsqueda de Palabras por Parte del Usuario**
```python
print("Ahora, busca las palabras en la sopa de letras!")
for _ in range(cantidad_palabras_sopa):
    palabra = input("Ingrese la palabra que encontró: ").upper()
    fila_ini = int(input("Ingrese la fila inicial: "))
    col_ini = int(input("Ingrese la columna inicial: "))
    fila_fin = int(input("Ingrese la fila final: "))
    col_fin = int(input("Ingrese la columna final: "))

    encontrada, letras_encontradas = verificar_palabra(sopa_de_letras, palabra, fila_ini, col_ini, fila_fin, col_fin)

    if encontrada:
        print("¡Correcto!")
        marcar_palabra(sopa_de_letras, letras_encontradas)
    else:
        print("Incorrecto, intente de nuevo.")

palabra: El usuario ingresa una palabra que cree haber encontrado en la sopa.
fila_ini, col_ini, fila_fin, col_fin: El usuario ingresa las coordenadas de inicio y fin de la palabra que ha encontrado.
verificar_palabra: Esta función verifica si la palabra y las coordenadas ingresadas por el usuario son correctas.
marcar_palabra: Si la palabra es correcta, se marca en la sopa de letras con un color verde.
````
## **10. Reimpresión de la Sopa de Letras**
```python
imprimir_sopa_de_letras(sopa_de_letras, filas, columnas)

Después de cada intento, la sopa de letras se vuelve a imprimir para que el usuario vea las palabras encontradas y continúe buscando.
```
