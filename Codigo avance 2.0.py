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

        cantidad_rotaciones = 7

        # Solicitar si desea añadir más rotaciones
        rotaciones_siguientes = input("¿Quiere jugar únicamente con esa rotación o quiere añadir más? Responda con 'SI' o 'NO': ").upper()

        if rotaciones_siguientes == 'NO':
            while cantidad_rotaciones > 0:
                rotaciones_sig = int(input("¿Qué otra rotación quiere usar?: "))

                for clave, valor in rotaciones.items():
                    if clave == rotaciones_sig:
                        rotaciones_posibles.append(valor)
                    
                print()

                seguir = input("¿Quiere seguir agregando más rotaciones? Responda 'SI' o 'NO': ").upper()
                
                if seguir == 'NO':
                    print("Se jugará con las rotaciones elegidas.")
                    print(rotaciones_posibles)
                    break



            if cantidad_rotaciones == 0:
                print("No hay más rotaciones posibles, se usarán todas las rotaciones posibles.")
        else:
            if rotaciones_siguientes == "SI":
                print("Se usará esa única rotación.")

        # Mostrar las palabras disponibles
        palabras_disponibles = list(lista_palabras_personalizada.keys())
        print("Palabras disponibles: " + str(palabras_disponibles))

        # Solicitar si desea jugar con palabras aleatorias o elegidas
        palabras = input('¿Quiere jugar con palabras aleatorias o prefiere jugar con palabras elegidas por sí mismo? Escriba "aleatorio" o "elegir" según lo que prefiera: ')

        # Solicitar añadir palabras personalizadas
        adicionar_elementos = input("¿Quiere añadir palabras personalizadas a la sopa? (responda con 'SI' o 'NO'), La sopa de letras iniciará con las palabras que el programa ya tiene definidas. Las palabras que añada se añadirán junto con las palabras definidas por el programa, siempre y cuando la cantidad de palabras añadidas sea suficiente para completar la sopa de letras. La cantidad de letras de las palabras añadidas no puede ser superior a las dimensiones de la sopa de letras: ")

        if adicionar_elementos == "SI":
            cantidad_elementos_añadir = int(input("¿Cuántas palabras quiere añadir a la sopa de letras? "))

            while cantidad_elementos_añadir > 0:
                añadir_palabra = input("¿Qué palabra quiere añadir?: ").upper()
                cantidad_letras_palabra = len(añadir_palabra)
                nueva_cantidad = cantidad_letras_palabra

                if cantidad_letras_palabra > filas or cantidad_letras_palabra > columnas:
                    while nueva_cantidad > filas or nueva_cantidad > columnas:
                        volver_añadir_palabra = input("Añada otra palabra que tenga una cantidad de letras menor a las dimensiones de la sopa de letras: ").upper()
                        nueva_cantidad = len(volver_añadir_palabra)
                    
                    lista_palabras_usuario[volver_añadir_palabra] = list(volver_añadir_palabra)
                    cantidad_elementos_añadir -= 1
                    cantidad -= 1
                    cantidad_palabras_sopa += 1
                    print(cantidad_palabras_sopa)  # Prueba

                else:
                    lista_palabras_usuario[añadir_palabra] = list(añadir_palabra)
                    cantidad_elementos_añadir -= 1

        # Añadir palabras aleatorias si el usuario elige "aleatorio"
        if palabras == "aleatorio":
            while cantidad > 0:
                palabra_azar, palabra_al = random.choice(list(lista_palabras_personalizada.items()))
                lista_palabras[palabra_azar] = palabra_al
                
                if palabra_azar in lista_palabras:
                    del lista_palabras_personalizada[palabra_azar]  # Eliminar palabra para evitar duplicados
                cantidad -= 1
                cantidad_palabras_sopa += 1
    
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