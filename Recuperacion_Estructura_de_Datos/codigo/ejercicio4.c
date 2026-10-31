#include <stdio.h>
#include <string.h>

/*
 * UNIVERSIDAD NACIONAL DEL ALTIPLANO DE PUNO
 * FACULTAD DE INGENIERÍA ESTADÍSTICA E INFORMÁTICA
 * Curso: Estructura de Datos (2026) - Prof. Fred Torres Cruz
 * Estudiante: Henry Antonio Mamani Gutierrez
 * 
 * 4. Baúl con operaciones en ambos extremos.
 * Use un arreglo como doble cola (deque). Las operaciones permiten insertar
 * y retirar elementos por ambos extremos. Considere hasta 100 operaciones
 * y valores enteros.
 * 
 * ESPACIOS COMPLETADOS:
 * - Espacio 1: --ini    (PUSH_TOP: decrementa el índice inicial e inserta en el extremo frontal)
 * - Espacio 2: fin++    (PUSH_BOTTOM: inserta en el extremo posterior e incrementa fin)
 * - Espacio 3: ini++    (POP_TOP: elimina del extremo frontal avanzando ini)
 * - Espacio 4: fin--    (POP_BOTTOM: elimina del extremo posterior retrocediendo fin)
 * 
 * Nota Técnica: Se inicializa ini = 100 y fin = 100 en un arreglo de tamaño 205.
 * El rango de elementos válidos en el baúl es a[ini ... fin - 1].
 */

int main(void) {
    int a[205], ini = 100, fin = 100, n, x, i, j;
    char op[20];

    if (scanf("%d", &n) != 1) return 1;

    for (i = 0; i < n; i++) {
        scanf("%19s", op);
        if (strcmp(op, "PUSH_TOP") == 0) {
            scanf("%d", &x); a[--ini] = x;
        } else if (strcmp(op, "PUSH_BOTTOM") == 0) {
            scanf("%d", &x); a[fin++] = x;
        } else if (strcmp(op, "POP_TOP") == 0) {
            if (ini < fin) ini++;
        } else if (strcmp(op, "POP_BOTTOM") == 0) {
            if (ini < fin) fin--;
        }
    }

    if (ini == fin) puts("BAUL VACIO");
    else {
        for (j = ini; j < fin; j++) printf("%d ", a[j]);
        printf("\n");
    }

    return 0;
}

