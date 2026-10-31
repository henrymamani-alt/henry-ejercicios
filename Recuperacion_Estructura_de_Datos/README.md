# Recuperación de Estructuras de Datos (2026)
**Universidad Nacional del Altiplano de Puno (UNA PUNO)**  
**Facultad de Ingeniería Estadística e Informática (FINESI)**  
**Escuela Profesional de Ingeniería Estadística e Informática**

- **Estudiante:** Henry Antonio Mamani Gutierrez
- **Docente:** Prof. Fred Torres Cruz
- **Fecha de Evaluación:** 30 de Octubre de 2026
- **Asignatura:** Estructura de Datos (III Semestre)

---

## 📂 Estructura del Proyecto
```text
Trabajo_Recuperacion_Estructura_de_Datos/
├── codigo/
│   ├── ejercicio1.c
│   ├── ejercicio2.c
│   ├── ejercicio3.c
│   ├── ejercicio4.c
│   └── ejercicio5.c
├── compilados/
│   ├── ejercicio1.exe
│   ├── ejercicio2.exe
│   ├── ejercicio3.exe
│   ├── ejercicio4.exe
│   └── ejercicio5.exe
├── imagenes/
│   ├── logo-una-puno.png
│   ├── logofinesi.png
│   ├── captura_ejercicio1.png
│   ├── captura_ejercicio2.png
│   ├── captura_ejercicio3.png
│   ├── captura_ejercicio4.png
│   └── captura_ejercicio5.png
├── scripts/
│   ├── render_vscode_terminal.py
│   ├── generate_recuperacion_captures.py
│   └── build_recuperacion_pdf.py
├── main.tex
├── informe_recuperacion.html
├── Trabajo_Recuperacion_Estructuras_Datos_Henry_Mamani.pdf
└── README.md
```

---

## 📝 Resumen de Espacios Completados y Respuestas

### 1. Suma de números impares (`ejercicio1.c`)
- **Espacio 1:** `1` *(Inicialización en el primer impar positivo)*
- **Espacio 2:** `i + 1` *(Paso de incremento unitario)*
- **Espacio 3:** `i % 2 != 0` *(Condición de número impar)*
- **Espacio 4:** `suma + i` *(Acumulación en la suma)*
- **Resultado Ejemplo:** `10 -> 25`

### 2. Conteo de calles (`ejercicio2.c`)
- **Espacio 1:** `i < n` *(Condición de parada para n códigos)*
- **Espacio 2:** `x == 1` *(Identificación de Norte-Sur)*
- **Espacio 3:** `ns++` *(Contador Norte-Sur)*
- **Espacio 4:** `eo++` *(Contador Este-Oeste)*
- **Resultado Ejemplo:** `1 1 2 1 2 1 -> 4 2`

### 3. Verificación de paréntesis con una pila (`ejercicio3.c`)
- **Espacio 1:** `tope++` *(Apilar '(' en tope actual)*
- **Espacio 2:** `tope == 0` *(Detección de underflow por cierre huérfano)*
- **Espacio 3:** `tope--` *(Desapilar '(' emparejado)*
- **Espacio 4:** `valido && tope == 0` *(Condición de balanceo final)*
- **Resultado Ejemplo:** `((()())) -> BALANCEADO`, `(() -> NO BALANCEADO`

### 4. Baúl con operaciones en ambos extremos (`ejercicio4.c`)
- **Espacio 1:** `--ini` *(PUSH_TOP: inserción en el extremo frontal)*
- **Espacio 2:** `fin++` *(PUSH_BOTTOM: inserción en el extremo posterior)*
- **Espacio 3:** `ini++` *(POP_TOP: supresión del extremo frontal)*
- **Espacio 4:** `fin--` *(POP_BOTTOM: supresión del extremo posterior)*
- **Resultado Ejemplo:** `99 15 30`

### 5. Personas vetadas y recorrido inverso (`ejercicio5.c`)
- **Espacio 1:** `strcmp(nombre[i], "Angel") != 0` *(Exclusión del sexto vetado)*
- **Espacio 2:** `tope++` *(Apilar persona admitida)*
- **Espacio 3:** `tope` *(Total de admitidos)*
- **Espacio 4:** `--tope` *(Desapilado e impresión en orden inverso LIFO)*
- **Resultado Ejemplo:** `4 -> Elena, Luis, Maria, Carlos`

