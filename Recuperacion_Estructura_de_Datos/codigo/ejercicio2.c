#include <stdio.h>

/*
 * UNIVERSIDAD NACIONAL DEL ALTIPLANO DE PUNO
 * FACULTAD DE INGENIERÍA ESTADÍSTICA E INFORMÁTICA
 * Curso: Estructura de Datos (2026) - Prof. Fred Torres Cruz
 * Estudiante: Henry Antonio Mamani Gutierrez
 * 
 * 2. Conteo de calles.
 * Lea n códigos de dirección: 1 representa Norte-Sur y 2 representa Este-Oeste.
 * Imprima los totales respectivos (ejemplo: 1 1 2 1 2 1 -> 4 2).
 * 
 * ESPACIOS COMPLETADOS:
 * - Espacio 1: i < n      (Condición de parada para leer exactamente n códigos)
 * - Espacio 2: x == 1     (Verificación para la dirección Norte-Sur)
 * - Espacio 3: ns++       (Incremento del contador de calles Norte-Sur)
 * - Espacio 4: eo++       (Incremento del contador de calles Este-Oeste)
 */

int main(void) {
    int n, x, i, ns = 0, eo = 0;
    if (scanf("%d", &n) != 1) return 1;

    for (i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x == 1) {
            ns++;
        } else if (x == 2) {
            eo++;
        }
    }

    printf("%d %d\n", ns, eo);
    return 0;
}

