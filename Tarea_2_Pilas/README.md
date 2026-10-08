# Tarea 2: Pilas / Stack (Capítulo II)

**Universidad Nacional del Altiplano de Puno**  
**Facultad de Ingeniería Estadística e Informática**  
**Escuela Profesional de Ingeniería Estadística e Informática**  

- **Curso:** Estructura de Datos (2026)  
- **Docente:** Prof. Fred Torres Cruz  
- **Estudiante:** Henry Antonio Mamani Gutierrez  
- **Documento Oficial:** [📄 `informe_pilas.pdf`](informe_pilas.pdf)  
- **Plantilla LaTeX:** [📝 `main.tex`](main.tex)  

---

## 📋 Lista de Ejercicios Desarrollados

| N° | Ejercicio | Código C++ | Código C | Evidencia | Lógica y Justificación LIFO |
|:--:|:---|:---:|:---:|:---------:|:---|
| 01 | **Apilar números enteros** | [`ejercicio1.cpp`](codigo/ejercicio1.cpp) | [`ejercicio1.c`](codigo/ejercicio1.c) | [Captura](imagenes/captura_ejercicio1.png) | Inserción de 5 enteros con `push()` y extracción secuencial con `top()`, `pop()` y `empty()`, saliendo en orden inverso: `20, 16, 12, 8, 4`. |
| 02 | **Invertir una palabra** | [`ejercicio2.cpp`](codigo/ejercicio2.cpp) | [`ejercicio2.c`](codigo/ejercicio2.c) | [Captura](imagenes/captura_ejercicio2.png) | Apilado de caracteres de una palabra (ej. `DATOS`) y desapilado natural en orden LIFO construyendo `SOTAD`. |
| 03 | **Paréntesis balanceados** | [`ejercicio3.cpp`](codigo/ejercicio3.cpp) | [`ejercicio3.c`](codigo/ejercicio3.c) | [Captura](imagenes/captura_ejercicio3.png) | Autómata de pila: apila `(` ante apertura y desapila ante `)`. Detecta cierres inválidos o aperturas pendientes. |
| 04 | **Historial Deshacer (Undo)** | [`ejercicio4.cpp`](codigo/ejercicio4.cpp) | [`ejercicio4.c`](codigo/ejercicio4.c) | [Captura](imagenes/captura_ejercicio4.png) | Menú interactivo de editor para apilar acciones, desapilar (revertir la última acción) y consultar el tope actual con `top()`. |
| 05 | **Decimal a binario** | [`ejercicio5.cpp`](codigo/ejercicio5.cpp) | [`ejercicio5.c`](codigo/ejercicio5.c) | [Captura](imagenes/captura_ejercicio5.png) | Divisiones sucesivas entre 2 apilando residuos (de LSB a MSB). La pila invierte la salida entregando el binario correcto (ej. `13` $\rightarrow$ `1101`). |

---

## 🧠 Pregunta de Cierre
**¿Qué característica común tienen los cinco problemas que hace apropiado utilizar una pila?**  
La característica común es la **reversibilidad temporal y la precedencia del último elemento ingresado (LIFO)**. En todos los problemas, el elemento más recientemente registrado o calculado es el que debe procesarse, verificarse o extraerse primero.
