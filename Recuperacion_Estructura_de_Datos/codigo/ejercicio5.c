#include <stdio.h>
#include <string.h>

/*
 * UNIVERSIDAD NACIONAL DEL ALTIPLANO DE PUNO
 * FACULTAD DE INGENIERÍA ESTADÍSTICA E INFORMÁTICA
 * Curso: Estructura de Datos (2026) - Prof. Fred Torres Cruz
 * Estudiante: Henry Antonio Mamani Gutierrez
 * 
 * 5. Personas vetadas y recorrido inverso.
 * Lea exactamente diez nombres, excluya Santiago, Pedro, Ariadna, Marco,
 * Juan y Angel. Imprima la cantidad admitida y sus nombres desde el último
 * hasta el primero, utilizando un arreglo como pila.
 * 
 * ESPACIOS COMPLETADOS:
 * - Espacio 1: strcmp(nombre[i], "Angel") != 0  (Excluye al sexto nombre vetado: 'Angel')
 * - Espacio 2: tope++                           (Apila el nombre admitido e incrementa tope)
 * - Espacio 3: tope                             (Imprime la cantidad total de personas admitidas)
 * - Espacio 4: --tope                           (Desapila en orden LIFO desde el último admitido)
 */

int main(void) {
    char nombre[10][40], pila[10][40];
    int i, tope = 0;

    for (i = 0; i < 10; i++) {
        if (scanf("%39s", nombre[i]) != 1) return 1;
        if (strcmp(nombre[i], "Santiago") != 0 &&
            strcmp(nombre[i], "Pedro") != 0 &&
            strcmp(nombre[i], "Ariadna") != 0 &&
            strcmp(nombre[i], "Marco") != 0 &&
            strcmp(nombre[i], "Juan") != 0 &&
            strcmp(nombre[i], "Angel") != 0) {
            strcpy(pila[tope++], nombre[i]);
        }
    }

    printf("%d\n", tope);
    while (tope > 0) {
        puts(pila[--tope]);
    }

    return 0;
}
