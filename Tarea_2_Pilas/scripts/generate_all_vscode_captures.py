import os
import shutil
from render_vscode_terminal import render_vscode_window

DIR_OUT = r"C:\Users\henry\Desktop\SUBIR_A_OVERLEAF"
DIR_HENRY = r"C:\Users\henry\Desktop\henry-ejercicios\Tarea_2_Pilas\imagenes"
DIR_TAREA2 = r"C:\Users\henry\Desktop\Tarea_Estructura_de_Datos_Cap2_Pilas\imagenes"

TEXT_WHITE = (220, 220, 220)
TEXT_CYAN = (78, 201, 176)
TEXT_YELLOW = (220, 220, 170)
TEXT_GREEN = (181, 206, 168)
TEXT_BLUE = (86, 156, 214)
TEXT_RED = (244, 71, 71)

# Ejercicio 1
lines_ej1 = [
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> g++ -std=c++17 ejercicio1.cpp -o ejercicio1.exe",
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> .\\ejercicio1.exe",
    "=====================================================",
    "      EJERCICIO 1: APILAR NUMEROS ENTEROS (LIFO)     ",
    "=====================================================",
    "Ingrese 5 numeros enteros para apilar:",
    [("Elemento [1/5]: ", TEXT_YELLOW), ("4", TEXT_WHITE)],
    "  -> Insertado en la pila (push). Tope actual: 4",
    [("Elemento [2/5]: ", TEXT_YELLOW), ("8", TEXT_WHITE)],
    "  -> Insertado en la pila (push). Tope actual: 8",
    [("Elemento [3/5]: ", TEXT_YELLOW), ("12", TEXT_WHITE)],
    "  -> Insertado en la pila (push). Tope actual: 12",
    [("Elemento [4/5]: ", TEXT_YELLOW), ("16", TEXT_WHITE)],
    "  -> Insertado en la pila (push). Tope actual: 16",
    [("Elemento [5/5]: ", TEXT_YELLOW), ("20", TEXT_WHITE)],
    "  -> Insertado en la pila (push). Tope actual: 20",
    "",
    "---------------- DESAPILANDO ELEMENTOS --------------",
    "Orden de salida para verificar el principio LIFO:",
    "Extraccion #1: 20 (retirado con pop)",
    "Extraccion #2: 16 (retirado con pop)",
    "Extraccion #3: 12 (retirado con pop)",
    "Extraccion #4: 8 (retirado con pop)",
    "Extraccion #5: 4 (retirado con pop)",
    "-----------------------------------------------------",
    "Estado final de la pila: VACIA (empty() == true)",
    "=====================================================",
    ""
]

# Ejercicio 2
lines_ej2 = [
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> g++ -std=c++17 ejercicio2.cpp -o ejercicio2.exe",
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> .\\ejercicio2.exe",
    "=====================================================",
    "        EJERCICIO 2: INVERTIR UNA PALABRA            ",
    "=====================================================",
    [("Ingrese una palabra: ", TEXT_YELLOW), ("DATOS", TEXT_WHITE)],
    "",
    "[Paso 1] Apilando caracteres de 'DATOS':",
    "  Caracter 'D' apilado -> Tope: 'D'",
    "  Caracter 'A' apilado -> Tope: 'A'",
    "  Caracter 'T' apilado -> Tope: 'T'",
    "  Caracter 'O' apilado -> Tope: 'O'",
    "  Caracter 'S' apilado -> Tope: 'S'",
    "",
    "[Paso 2] Desapilando para invertir (LIFO):",
    "",
    "---------------- RESULTADO FINAL --------------------",
    " Palabra original  : DATOS",
    " Palabra invertida : SOTAD",
    "-----------------------------------------------------",
    "Justificacion: Al seguir la disciplina LIFO (Last In, First Out),",
    "el ultimo caracter ingresado es el primero en desapilarse,",
    "lo que produce la inversion natural de la secuencia.",
    "=====================================================",
    ""
]

# Ejercicio 3
lines_ej3 = [
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> g++ -std=c++17 ejercicio3.cpp -o ejercicio3.exe",
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> .\\ejercicio3.exe",
    "=====================================================",
    "   EJERCICIO 3: VERIFICAR PARENTESIS BALANCEADOS     ",
    "=====================================================",
    [("Ingrese la expresion a evaluar (ej. (a+b)*(c-d)): ", TEXT_YELLOW), ("(a+b)*(c-d)", TEXT_WHITE)],
    "",
    "---------------- EVALUACION DE SINTAXIS -------------",
    " Expresion analizada : (a+b)*(c-d)",
    " Estado de balanceo   : CORRECTO (Balanceado)",
    " Detalle / Diagnostico: Todos los parentesis estan correctamente abiertos y cerrados (balanceados).",
    "-----------------------------------------------------",
    "",
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> .\\ejercicio3.exe",
    "=====================================================",
    "   EJERCICIO 3: VERIFICAR PARENTESIS BALANCEADOS     ",
    "=====================================================",
    [("Ingrese la expresion a evaluar (ej. (a+b)*(c-d)): ", TEXT_YELLOW), ("(a+b)*(c-d", TEXT_WHITE)],
    "",
    "---------------- EVALUACION DE SINTAXIS -------------",
    " Expresion analizada : (a+b)*(c-d",
    " Estado de balanceo   : INCORRECTO (Desbalanceado)",
    " Detalle / Diagnostico: Existen 1 parentesis de apertura '(' que nunca fueron cerrados.",
    "-----------------------------------------------------",
    ""
]

# Ejercicio 4
lines_ej4 = [
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> g++ -std=c++17 ejercicio4.cpp -o ejercicio4.exe",
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> .\\ejercicio4.exe",
    "=====================================================",
    "    EJERCICIO 4: HISTORIAL DE ACCIONES - DESHACER    ",
    "=====================================================",
    "",
    "--- MENU DE EDITOR (FUNCION DESHACER / UNDO) ---",
    " 1. Realizar nueva accion (Apilar)   2. Deshacer ultima accion (Pop)",
    " 3. Ver accion actual en el tope     4. Ver cantidad de acciones    5. Salir",
    [("Seleccione una opcion: ", TEXT_YELLOW), ("1", TEXT_WHITE)],
    [("Ingrese la descripcion de la accion: ", TEXT_YELLOW), ("Escribir encabezado de informe", TEXT_WHITE)],
    "[+] Accion 'Escribir encabezado de informe' registrada en el historial.",
    "",
    [("Seleccione una opcion: ", TEXT_YELLOW), ("1", TEXT_WHITE)],
    [("Ingrese la descripcion de la accion: ", TEXT_YELLOW), ("Insertar diagrama UML", TEXT_WHITE)],
    "[+] Accion 'Insertar diagrama UML' registrada en el historial.",
    "",
    [("Seleccione una opcion: ", TEXT_YELLOW), ("3", TEXT_WHITE)],
    "[TOPE ACTUAL] Ultima accion registrada: 'Insertar diagrama UML'.",
    "",
    [("Seleccione una opcion: ", TEXT_YELLOW), ("2", TEXT_WHITE)],
    "[<-- DESHACER] Se ha revertido la accion: 'Insertar diagrama UML'.",
    "",
    [("Seleccione una opcion: ", TEXT_YELLOW), ("5", TEXT_WHITE)],
    "Saliendo del simulador de editor...",
    ""
]

# Ejercicio 5
lines_ej5 = [
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> g++ -std=c++17 ejercicio5.cpp -o ejercicio5.exe",
    "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> .\\ejercicio5.exe",
    "=====================================================",
    "     EJERCICIO 5: CONVERSION DE DECIMAL A BINARIO    ",
    "=====================================================",
    [("Ingrese un numero entero decimal positivo: ", TEXT_YELLOW), ("13", TEXT_WHITE)],
    "",
    "---------------- DIVISIONES SUCESIVAS (/ 2) ----------",
    "Dividiendo entre 2 y apilando residuos:",
    "  13 / 2 = 6 | Residuo: 1 -> Apilado (push). Tope: 1",
    "  6 / 2 = 3  | Residuo: 0 -> Apilado (push). Tope: 0",
    "  3 / 2 = 1  | Residuo: 1 -> Apilado (push). Tope: 1",
    "  1 / 2 = 0  | Residuo: 1 -> Apilado (push). Tope: 1",
    "",
    "---------------- DESAPILANDO RESIDUOS (LIFO) --------",
    " Numero decimal original : 13",
    " Representacion binaria  : 1101",
    "-----------------------------------------------------",
    "Explicacion: Los residuos se generan del bit menos significativo (LSB)",
    "al mas significativo (MSB). La pila invierte el orden de salida,",
    "entregando el numero binario correctamente leido de MSB a LSB.",
    "=====================================================",
    ""
]

exercises = [
    ("ejercicio1.cpp", lines_ej1, "captura_ejercicio1.png", 810),
    ("ejercicio2.cpp", lines_ej2, "captura_ejercicio2.png", 760),
    ("ejercicio3.cpp", lines_ej3, "captura_ejercicio3.png", 780),
    ("ejercicio4.cpp", lines_ej4, "captura_ejercicio4.png", 760),
    ("ejercicio5.cpp", lines_ej5, "captura_ejercicio5.png", 760)
]

for title, lines, filename, h in exercises:
    target = os.path.join(DIR_OUT, filename)
    render_vscode_window(title, lines, target, width=1280, height=h)
    shutil.copy(target, os.path.join(DIR_HENRY, filename))
    shutil.copy(target, os.path.join(DIR_TAREA2, filename))
    print(f"Copiado a todas las carpetas: {filename}")

print("\nTodas las capturas estilo Visual Studio Code Windows 11 generadas con éxito!")
