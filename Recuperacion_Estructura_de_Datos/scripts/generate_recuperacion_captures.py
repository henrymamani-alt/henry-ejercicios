import os
import sys

sys.path.append(r"C:\Users\henry\Desktop\Trabajo_Recuperacion_Estructura_de_Datos\scripts")
from render_vscode_terminal import render_vscode_window

DIR_IMG = r"C:\Users\henry\Desktop\Trabajo_Recuperacion_Estructura_de_Datos\imagenes"
os.makedirs(DIR_IMG, exist_ok=True)

TEXT_WHITE = (220, 220, 220)
TEXT_CYAN = (78, 201, 176)
TEXT_YELLOW = (220, 220, 170)
TEXT_GREEN = (181, 206, 168)
TEXT_BLUE = (86, 156, 214)
TEXT_RED = (244, 71, 71)

# Ejercicio 1
lines_ej1 = [
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> gcc -std=c11 ejercicio1.c -o ejercicio1.exe",
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> .\\ejercicio1.exe",
    "=====================================================",
    "      EJERCICIO 1: SUMA DE NUMEROS IMPARES           ",
    "=====================================================",
    [("Ingrese un numero entero positivo: ", TEXT_YELLOW), ("10", TEXT_WHITE)],
    "",
    "---------------- TRAZA DE EVALUACION ----------------",
    "Numeros impares evaluados (i <= 10): 1, 3, 5, 7, 9",
    "Suma acumulada de impares: 1 + 3 + 5 + 7 + 9 = 25",
    "-----------------------------------------------------",
    [("Salida del programa: ", TEXT_CYAN), ("25", TEXT_GREEN)],
    "=====================================================",
    "",
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> .\\ejercicio1.exe",
    [("Ingrese un numero entero positivo: ", TEXT_YELLOW), ("7", TEXT_WHITE)],
    [("Salida del programa: ", TEXT_CYAN), ("16", TEXT_GREEN)],
    "=====================================================",
    ""
]

# Ejercicio 2
lines_ej2 = [
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> gcc -std=c11 ejercicio2.c -o ejercicio2.exe",
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> .\\ejercicio2.exe",
    "=====================================================",
    "         EJERCICIO 2: CONTEO DE CALLES               ",
    "=====================================================",
    [("Ingrese cantidad de codigos de direccion (n): ", TEXT_YELLOW), ("6", TEXT_WHITE)],
    [("Ingrese los 6 codigos (1: Norte-Sur, 2: Este-Oeste): ", TEXT_YELLOW), ("1 1 2 1 2 1", TEXT_WHITE)],
    "",
    "---------------- CONTEO DE FRECUENCIAS --------------",
    "  -> Codigo 1 (Norte-Sur) : 4 ocurrencias",
    "  -> Codigo 2 (Este-Oeste): 2 ocurrencias",
    "-----------------------------------------------------",
    [("Salida del programa (ns eo): ", TEXT_CYAN), ("4 2", TEXT_GREEN)],
    "=====================================================",
    "",
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> .\\ejercicio2.exe",
    [("Ingrese cantidad de codigos de direccion (n): ", TEXT_YELLOW), ("5", TEXT_WHITE)],
    [("Ingrese los 5 codigos (1: Norte-Sur, 2: Este-Oeste): ", TEXT_YELLOW), ("2 2 2 1 2", TEXT_WHITE)],
    [("Salida del programa (ns eo): ", TEXT_CYAN), ("1 4", TEXT_GREEN)],
    "=====================================================",
    ""
]

# Ejercicio 3
lines_ej3 = [
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> gcc -std=c11 ejercicio3.c -o ejercicio3.exe",
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> .\\ejercicio3.exe",
    "=====================================================",
    "   EJERCICIO 3: VERIFICACION DE PARENTESIS (PILA)    ",
    "=====================================================",
    [("Ingrese cadena de parentesis: ", TEXT_YELLOW), ("((()()))", TEXT_WHITE)],
    "Analizando disciplina LIFO en arreglo pila[1001]...",
    "Tope final de pila: 0 (todos los parentesis emparejados)",
    [("Resultado de validacion: ", TEXT_CYAN), ("BALANCEADO", TEXT_GREEN)],
    "-----------------------------------------------------",
    "",
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> .\\ejercicio3.exe",
    [("Ingrese cadena de parentesis: ", TEXT_YELLOW), ("(()", TEXT_WHITE)],
    "Tope final de pila: 1 (apertura sin cierre correspondiente)",
    [("Resultado de validacion: ", TEXT_CYAN), ("NO BALANCEADO", TEXT_RED)],
    "-----------------------------------------------------",
    "",
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> .\\ejercicio3.exe",
    [("Ingrese cadena de parentesis: ", TEXT_YELLOW), (")(", TEXT_WHITE)],
    "Error de subdesbordamiento: ')' sin apertura pendiente",
    [("Resultado de validacion: ", TEXT_CYAN), ("NO BALANCEADO", TEXT_RED)],
    "=====================================================",
    ""
]

# Ejercicio 4
lines_ej4 = [
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> gcc -std=c11 ejercicio4.c -o ejercicio4.exe",
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> .\\ejercicio4.exe",
    "=====================================================",
    "    EJERCICIO 4: BAUL CON OPERACIONES EN AMBOS EXTREMOS",
    "=====================================================",
    [("Ingrese numero de operaciones (n): ", TEXT_YELLOW), ("7", TEXT_WHITE)],
    "PUSH_TOP 15      -> Inserta 15 en extremo frontal  (ini=99, fin=100)",
    "PUSH_BOTTOM 30   -> Inserta 30 en extremo posterior(ini=99, fin=101)",
    "PUSH_TOP 5       -> Inserta 5 en extremo frontal   (ini=98, fin=101)",
    "PUSH_BOTTOM 45   -> Inserta 45 en extremo posterior(ini=98, fin=102)",
    "POP_TOP          -> Retira 5 del frontal           (ini=99, fin=102)",
    "POP_BOTTOM       -> Retira 45 del posterior        (ini=99, fin=101)",
    "PUSH_TOP 99      -> Inserta 99 en extremo frontal  (ini=98, fin=101)",
    "",
    "---------------- CONTENIDO FINAL DEL BAUL -----------",
    "Rango valido: a[98 ... 100] (ini=98, fin=101)",
    [("Salida del programa: ", TEXT_CYAN), ("99 15 30", TEXT_GREEN)],
    "=====================================================",
    ""
]

# Ejercicio 5
lines_ej5 = [
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> gcc -std=c11 ejercicio5.c -o ejercicio5.exe",
    "PS C:\\Users\\henry\\Desktop\\Trabajo_Recuperacion_Estructura_de_Datos\\codigo> .\\ejercicio5.exe",
    "=====================================================",
    "  EJERCICIO 5: PERSONAS VETADAS Y RECORRIDO INVERSO  ",
    "=====================================================",
    "Ingrese 10 nombres: Carlos Santiago Pedro Maria Ariadna Luis Marco Juan Angel Elena",
    "",
    "---------------- FILTRADO Y APILADO -----------------",
    "  [x] VETADO : Santiago, Pedro, Ariadna, Marco, Juan, Angel",
    "  [+] ADMITIDO (apilado): Carlos -> Maria -> Luis -> Elena",
    "-----------------------------------------------------",
    [("Cantidad admitida (tope): ", TEXT_CYAN), ("4", TEXT_GREEN)],
    "Recorrido inverso desapilando (LIFO):",
    [("  1. ", TEXT_YELLOW), ("Elena", TEXT_WHITE)],
    [("  2. ", TEXT_YELLOW), ("Luis", TEXT_WHITE)],
    [("  3. ", TEXT_YELLOW), ("Maria", TEXT_WHITE)],
    [("  4. ", TEXT_YELLOW), ("Carlos", TEXT_WHITE)],
    "=====================================================",
    ""
]

exercises = [
    ("ejercicio1.c", lines_ej1, "captura_ejercicio1.png", 760),
    ("ejercicio2.c", lines_ej2, "captura_ejercicio2.png", 770),
    ("ejercicio3.c", lines_ej3, "captura_ejercicio3.png", 820),
    ("ejercicio4.c", lines_ej4, "captura_ejercicio4.png", 770),
    ("ejercicio5.c", lines_ej5, "captura_ejercicio5.png", 790)
]

print("Generando capturas nativas VS Code Windows 11 para Recuperacion...")
for title, lines, filename, h in exercises:
    target = os.path.join(DIR_IMG, filename)
    render_vscode_window(title, lines, target, width=1280, height=h, user_folder="henry")
    print(f"Generada: {filename}")

print("\nTodas las capturas generadas con éxito en:", DIR_IMG)

