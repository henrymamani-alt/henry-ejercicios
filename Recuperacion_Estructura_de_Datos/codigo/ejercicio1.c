#include <stdio.h>

/*
 * UNIVERSIDAD NACIONAL DEL ALTIPLANO DE PUNO
 * FACULTAD DE INGENIERÍA ESTADÍSTICA E INFORMÁTICA
 * Curso: Estructura de Datos (2026) - Prof. Fred Torres Cruz
 * Estudiante: Henry Antonio Mamani Gutierrez
 * 
 * 1. Suma de números impares.
 * Lea un entero positivo y muestre la suma de todos los números impares
 * menores o iguales a él (ejemplo: 10 -> 25).
 * 
 * ESPACIOS COMPLETADOS:
 * - Espacio 1: 1          (Inicialización del índice en el primer impar)
 * - Espacio 2: i + 1      (Incremento secuencial de la variable de control)
 * - Espacio 3: i % 2 != 0 (Condición de número impar, equivalente a i % 2 == 1)
 * - Espacio 4: suma + i   (Acumulación del valor impar en la suma)
 */

int main(void) {
    int n, i, suma = 0;
    if (scanf("%d", &n) != 1) return 1;

    for (i = 1; i <= n; i = i + 1) {
        if (i % 2 != 0) {
            suma = suma + i;
        }
    }

    printf("%d\n", suma);
    return 0;
}
