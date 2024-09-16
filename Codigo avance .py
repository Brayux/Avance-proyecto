import random

# LISTAS:

# Lista de letras posibles para rellenar la sopa de letras
letras_posibles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Diccionarios con diferentes niveles de dificultad, cada uno contiene palabras relacionadas con programación
dificil = {'PROGRAMACION':'PROGRAMACION','PYTHON':'PYTHON','WHILE':'WHILE','FOR':'FOR','IF':'IF','PRINT':'PRINT','INPUT':'INPUT','PIP':'PIP','TRUE':'TRUE','FALSE':'FALSE','RANGE':'RANGE','ELSE':'ELSE','FUNCIONES':'FUNCIONES','MATRIZ':'MATRIZ','STR':'STR','ELIF':'ELIF','LENGUAJES':'LENGUAJES','INTERPRETE':'INTERPRETE','COMPUTADOR':'COMPUTADOR'}
medio = {'PYTHON': 'PYTHON', 'WHILE': 'WHILE', 'RANGE': 'RANGE','MATRIZ': 'MATRIZ','LENGUAJES': 'LENGUAJES','FOR': 'FOR', 'IF': 'IF', 'TRUE': 'TRUE', 'FALSE': 'FALSE', 'ELSE': 'ELSE', 'PRINT': 'PRINT', 'INPUT': 'INPUT', 'STR': 'STR', 'ELIF': 'ELIF'}
facil = {'FOR': 'FOR', 'IF': 'IF', 'TRUE': 'TRUE', 'FALSE': 'FALSE', 'ELSE': 'ELSE', 'PRINT': 'PRINT', 'INPUT': 'INPUT', 'STR': 'STR', 'ELIF': 'ELIF'}

# Diccionarios para personalizar las palabras de la sopa
lista_palabras_usuario = {}
lista_palabras_personalizada = {'PROGRAMACION':'PROGRAMACION','PYTHON':'PYTHON','WHILE':'WHILE','FOR':'FOR','IF':'IF','PRINT':'PRINT','INPUT':'INPUT','PIP':'PIP','TRUE':'TRUE','FALSE':'FALSE','RANGE':'RANGE','ELSE':'ELSE','FUNCIONES':'FUNCIONES','MATRIZ':'MATRIZ','STR':'STR','ELIF':'ELIF','LENGUAJES':'LENGUAJES','INTERPRETE':'INTERPRETE','COMPUTADOR':'COMPUTADOR'}
lista_palabras = {}
palabras_buscar = []

# Diccionario para determinar de forma aleatoria las posibles rotaciones de las palabras en la sopa
rotaciones = {
    1 : (0,1),    # Horizontal (izquierda-derecha)
    2 : (0,-1),   # Horizontal (derecha-izquierda)
    3 : (1,0),    # Vertical (arriba-abajo)
    4 : (-1,0),   # Vertical (abajo-arriba)
    5 : (1,1),    # Diagonal descendente (de arriba a la izquierda hacia abajo a la derecha)
    6 : (-1, -1), # Diagonal ascendente (de abajo a la derecha hacia arriba a la izquierda)
    7 : (1, -1),  # Diagonal descendente (de arriba a la derecha hacia abajo a la izquierda)
    8 : (-1, 1)   # Diagonal ascendente (de abajo a la izquierda hacia arriba a la derecha)
}

rotaciones_posibles = []

# FUNCIONES:

# Función para generar la matriz inicial de la sopa de letras
def generar_sopa_de_letras(filas, columnas):
    sopa_de_letras = {}
    for fila in range(filas):
        for columna in range(columnas):
            sopa_de_letras[(fila, columna)] = '-'  # Inicialmente, todas las posiciones están vacías
    return sopa_de_letras

# Función para imprimir la sopa de letras
def imprimir_sopa_de_letras(sopa_de_letras, filas, columnas):
    for fila in range(filas):
        for columna in range(columnas):
            print(sopa_de_letras[(fila, columna)], end=' ')  # Imprimir cada letra seguida de un espacio
        print()

# Función para reemplazar letras en la sopa de letras en una posición específica
def reemplazar_letra(sopa_de_letras, fila, columna, nueva_letra):
    sopa_de_letras[(fila,columna)] = nueva_letra.lower()  # Reemplaza la letra en la posición dada

# Función para elegir una palabra al azar y separarla en letras individuales
def escoger_separar_en_lista(letras_palabra):
    palabra = random.choice(list(lista_palabras.keys()))  # Elegir una palabra al azar
    palabras_buscar.append(palabra)  # Agregar la palabra a la lista de palabras a buscar
    letras_palabra = list(palabra)  # Separar la palabra en letras
    cantidad_palabras = len(letras_palabra)  # Contar el número de letras
    del lista_palabras[palabra]  # Eliminar la palabra del diccionario original
    return palabra, letras_palabra

# Función para priorizar las palabras del usuario en la sopa de letras
def priorizar_lista_usuario(lista_palabras, lista_palabras_usuario):
    for palabra in lista_palabras_usuario:
        lista_palabras[palabra] = lista_palabras_usuario[palabra]  # Añadir las palabras del usuario a la lista principal
    return lista_palabras

# Función para colocar las palabras en la sopa de letras en una dirección específica
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

# Función para validar si hay suficiente espacio para una palabra en la dirección deseada
def validar_espacio(sopa_de_letras, letras_palabra, filas, columnas, inicio_fila, inicio_columna, direccion_fila, direccion_columna):
    contador = 0
    for letra in letras_palabra:
        nueva_fila = inicio_fila + contador * direccion_fila
        nueva_columna = inicio_columna + contador * direccion_columna
        # Verificar si la posición está dentro de los límites y no está ocupada
        if nueva_fila < 0 or nueva_fila >= filas or nueva_columna < 0 or nueva_columna >= columnas:
            return False
        if sopa_de_letras[(nueva_fila, nueva_columna)] != '-' and sopa_de_letras[(nueva_fila, nueva_columna)] != letra:
            return False
        contador += 1
    return True

# Función para configurar la dificultad de la sopa de letras
def configurar_dificultad(dificultad):
    if dificultad == 'FACIL':
        return 10, 10, 5, [(0,1), (1,0)], facil
    if dificultad == 'MEDIO':
        return 15, 15, 10, [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1)], medio
    if dificultad == 'DIFICIL':
        return 30, 30, 15, [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)], dificil
    return 

# Función para llenar la sopa de letras con letras aleatorias en las posiciones vacías
def llenar_con_aleatorias(sopa_de_letras,filas, columnas):
    letras_posibles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for fila in range(filas):
        for columna in range(columnas):
            if sopa_de_letras[(fila, columna)] == '-':  # Si la posición está vacía
                sopa_de_letras[(fila, columna)] = random.choice(letras_posibles)  # Rellenar con una letra al azar

if __name__ == "__main__":

    # Solicitar al usuario si desea una sopa de letras predefinida o personalizada
    personalizacion = input("¿Quiere jugar en una dificultad predefinida o desearía que la sopa de letras fuera personalizada bajo ciertos criterios? Responda con 'predefinida' o 'personalizada' según sea su caso: ").lower()

    if personalizacion == 'predefinida':
        # Mostrar las opciones de dificultad disponibles
        print("Las dificultades disponibles son las siguientes: \n FACIL: \n - Sopa de letras de 10 X 10 \n - Solo orientaciones vertical y horizontal \n - Solo 5 palabras \n - Palabras cortas \n MEDIO: \n - Sopa de letras de 15 X 15 \n - Orientaciones verticales, horizontales y diagonales en una dirección \n - 10 palabras \n - Palabras de longitud moderada \n DIFICIL: \n - Sopa de letras 30 X 30 \n - Todas las orientaciones posibles \n - 15 palabras \n - Todo tipo de palabras")
        
        # Solicitar la dificultad al usuario
        dificultad = input("Seleccione la dificultad bajo la cual le gustaría establecer la sopa de letras: ").upper()
        # Configurar la dificultad y obtener los parámetros correspondientes
        filas, columnas, cantidad_palabras_sopa, rotaciones_posibles, lista_palabras = configurar_dificultad(dificultad)

    elif personalizacion == 'personalizada':
        cantidad_palabras_sopa = 0
        # Solicitar las dimensiones de la sopa de letras
        print("Ingrese el tamaño de la sopa de letras, debe ser mínimo de dimensiones 10 X 10 y máximo 30 X 30")
        filas = int(input("Ingrese el número de filas: "))
        while not (10 <= filas <= 30):
            print("El número de filas debe estar entre 10 y 30.")
            filas = int(input("Ingrese de nuevo el número de filas: "))

        columnas = int(input("Ingrese el número de columnas: "))
        while not (10 <= columnas <= 30):
            print("El número de columnas debe estar entre 10 y 30.")
            columnas = int(input("Ingrese de nuevo el número de columnas: "))

        cantidad = int(input("¿Cuántas palabras quiere en la sopa? "))

        # Condiciones especiales para eliminar palabras según el tamaño de la sopa
        if (columnas == 11 and filas == 11) or (columnas == 10 and filas == 10):
            if 'PROGRAMACION' in lista_palabras:
                del lista_palabras['PROGRAMACION']
                del lista_palabras_personalizada['PROGRAMACION']
        else:
            if columnas == 10 and filas == 10:
                if 'PROGRAMACION' in lista_palabras or 'COMPUTADOR' in lista_palabras or 'INTERPRETE' in lista_palabras:
                    del lista_palabras['PROGRAMACION']
                    del lista_palabras['COMPUTADOR']
                    del lista_palabras['INTERPRETE']
                    del lista_palabras_personalizada['PROGRAMACION']
                    del lista_palabras_personalizada['COMPUTADOR']
                    del lista_palabras_personalizada['INTERPRETE']

        # Solicitar las rotaciones que el usuario desea utilizar
        print("¿Con cuáles rotaciones quiere jugar en la sopa? Las rotaciones posibles son: \n 1. Horizontal (izquierda-derecha) \n 2. Horizontal (derecha-izquierda) \n 3. Vertical (arriba-abajo) \n 4. Vertical (abajo-arriba) \n 5. Diagonal descendente (de arriba a la izquierda hacia abajo a la derecha) \n 6. Diagonal ascendente (de abajo a la derecha hacia arriba a la izquierda) \n 7. Diagonal descendente (de arriba a la derecha hacia abajo a la izquierda) \n 8. Diagonal ascendente (de abajo a la izquierda hacia arriba a la derecha) \n Ponga un numero entre 1 y 8, apartir del numero que acompaña a las orientaciones que se ven arriba:")

        primera_rotacion_elegida = int(input("Número de la rotación: "))

        # Añadir la rotación elegida a la lista de rotaciones posibles
        for clave, valor in rotaciones.items():
            if clave == primera_rotacion_elegida:
                rotaciones_posibles.append(valor)

        del rotaciones[primera_rotacion_elegida]
        cantidad_rotaciones = 7

        # Solicitar si desea añadir más rotaciones
        while True:
            rotaciones_siguientes = input("¿Quiere quiere añadir más rotaciones? Responda con 'SI' o 'NO': ").upper()

            if rotaciones_siguientes == 'NO':
                print("Se jugará con las rotaciones elegidas.")
                print(rotaciones_posibles)
                break  # Finaliza el bucle si el usuario no quiere más rotaciones

            elif rotaciones_siguientes == "SI":
                cantidad_rotaciones -= 1
                if cantidad_rotaciones > 0:
                    while True:
                        rotaciones_sig = input("¿Qué otra rotación quiere usar? (ingrese un número): ")

                        # Verificar manualmente si el valor ingresado es un número
                        es_numero = True
                        for caracter in rotaciones_sig:
                            if caracter < '0' or caracter > '9':  # Verificar si el carácter no es un dígito
                                es_numero = False
                                break
                        
                        if es_numero:
                            rotaciones_sig = int(rotaciones_sig)

                            # Verificar si la rotación ingresada está en el diccionario
                            if rotaciones_sig in rotaciones:
                                rotaciones_posibles.append(rotaciones[rotaciones_sig])

                                # Eliminar la rotación seleccionada para evitar duplicados
                                del rotaciones[rotaciones_sig]
                                print("Rotaciones seleccionadas:", rotaciones_posibles)
                                break  # Salir del bucle si se selecciona una rotación válida
                            else:
                                print("Por favor, ingrese un número de rotación válido que esté disponible.")
                        else:
                            print("Entrada inválida. Por favor, ingrese un número válido.")
                
                else:
                    print("No hay más rotaciones posibles.")
                    break  # Finaliza el bucle si ya no hay más rotaciones posibles

            else:
                print("Por favor, responda 'SI' o 'NO'.")

        # Mostrar las palabras disponibles
        palabras_disponibles = list(lista_palabras_personalizada.keys())
        print("Palabras disponibles: " + str(palabras_disponibles))

        # Solicitar si desea jugar con palabras aleatorias o elegidas
        while True:
            palabras = input('¿Quiere jugar con palabras aleatorias o prefiere jugar con palabras elegidas por sí mismo? Escriba "ALEATORIO" o "ELEGIR" según lo que prefiera: ').upper()

            if palabras == "ALEATORIO":
                while cantidad > 0:
                    palabra_azar, palabra_al = random.choice(list(lista_palabras_personalizada.items()))
                    lista_palabras[palabra_azar] = palabra_al
                    
                    if palabra_azar in lista_palabras:
                        del lista_palabras_personalizada[palabra_azar]  # Eliminar palabra para evitar duplicados
                    cantidad -= 1
                    cantidad_palabras_sopa += 1
                print("Se jugará con palabras aleatorias.")
                break  # Salir del bucle después de añadir palabras aleatorias

            elif palabras == "ELEGIR":
                while True:
                    añadir_palabra = input("¿Qué palabra quiere añadir? ").upper()
                    if añadir_palabra in lista_palabras_personalizada:
                        lista_palabras[añadir_palabra] = lista_palabras_personalizada[añadir_palabra]
                        cantidad_palabras_sopa += 1
                        del lista_palabras_personalizada[añadir_palabra]  # Eliminar palabra para evitar duplicados
                        cantidad -= 1
                        if cantidad <= 0:
                            break  # Salir del bucle si se ha añadido el número requerido de palabras
                    else:
                        print("La palabra no está en la lista de palabras personalizadas o ya ha sido añadida.")
                
                print("Se jugará con palabras elegidas.")
                break  # Salir del bucle después de añadir las palabras elegidas

            else:
                print("Entrada inválida. Por favor, responda con 'ALEATORIO' o 'ELEGIR'.")

        # Solicitar añadir palabras personalizadas
        adicionar_elementos = input("¿Quiere añadir palabras personalizadas a la sopa? (responda con 'SI' o 'NO'). La sopa de letras iniciará con las palabras que el programa ya tiene definidas. Las palabras que añada se añadirán junto con las palabras definidas por el programa, siempre y cuando la cantidad de palabras añadidas sea suficiente para completar la sopa de letras. La cantidad de letras de las palabras añadidas no puede ser superior a las dimensiones de la sopa de letras: ").upper()

        if adicionar_elementos == "SI":
            cantidad_elementos_añadir = int(input("¿Cuántas palabras quiere añadir a la sopa de letras? "))

            while cantidad_elementos_añadir > 0:
                añadir_palabra = input("¿Qué palabra quiere añadir?: ").upper()
                cantidad_letras_palabra = len(añadir_palabra)

                if cantidad_letras_palabra > filas or cantidad_letras_palabra > columnas:
                    print("La palabra es demasiado larga para las dimensiones de la sopa de letras.")
                    continue  # Volver a solicitar una nueva palabra si la longitud es incorrecta

                # Añadir palabra al diccionario de palabras del usuario
                lista_palabras_usuario[añadir_palabra] = list(añadir_palabra)
                cantidad_elementos_añadir -= 1
                cantidad -= 1
                cantidad_palabras_sopa += 1

                print("Palabras personalizadas añadidas:")
                print(lista_palabras_usuario)
                print("Cantidad de palabras restantes por añadir:"+str(cantidad_elementos_añadir))

        elif adicionar_elementos == "NO":
            print("No se añadirán palabras personalizadas.")

        else:
            print("Entrada inválida. Por favor, responda con 'SI' o 'NO'.")
   
        print(lista_palabras_usuario)

    # Priorizar palabras del usuario
    lista_palabras = priorizar_lista_usuario(lista_palabras, lista_palabras_usuario)
    # Generar la sopa de letras inicial
    sopa_de_letras = generar_sopa_de_letras(filas, columnas)
    
    # Colocar palabras en la sopa
    for _ in range(cantidad_palabras_sopa):
        palabra, letras_palabra = escoger_separar_en_lista(lista_palabras)
        random.shuffle(rotaciones_posibles)  # Mezclar las rotaciones posibles
        for direccion_fila, direccion_columna in rotaciones_posibles:
            if validar_espacio(sopa_de_letras, letras_palabra, filas, columnas, 0, 0, direccion_fila, direccion_columna):
                colocar_en_sopa(sopa_de_letras, letras_palabra, filas, columnas, direccion_fila, direccion_columna)
                break

    # Llenar la sopa de letras con letras aleatorias en las posiciones vacías
    llenar_con_aleatorias(sopa_de_letras, filas, columnas)

    # Imprimir la sopa de letras generada y las palabras a encontrar
    print("Sopa de letras generada:")

    imprimir_sopa_de_letras(sopa_de_letras, filas, columnas)
    
    print("Palabras a encontrar: " + str(palabras_buscar))