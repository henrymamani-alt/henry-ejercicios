#include <stdio.h>
#include <string.h>

/*
 * UNIVERSIDAD NACIONAL DEL ALTIPLANO DE PUNO
 * FACULTAD DE INGENIERÍA ESTADÍSTICA E INFORMÁTICA
 * Curso: Estructura de Datos (2026) - Prof. Fred Torres Cruz
 * Estudiante: Henry Antonio Mamani Gutierrez
 * 
 * 3. Verificación de paréntesis con una pila.
 * Lea una cadena compuesta solamente por ( y ). Escriba BALANCEADO si sus
 * paréntesis están correctamente emparejados; en caso contrario, NO BALANCEADO.
 * Complete cuatro espacios.
 * 
 * ESPACIOS COMPLETADOS:
 * - Espacio 1: tope++                 (Apila '(' e incrementa el contador de tope)
 * - Espacio 2: tope == 0              (Verifica si la pila está vacía al cerrar ')')
 * - Espacio 3: tope--                 (Desapila el '(' correspondiente)
 * - Espacio 4: valido && tope == 0    (Condición final: balanceado si no hubo error y la pila quedó vacía)
 */

int main(void) {
    char s[1001], pila[1001];
    int i, tope = 0, valido = 1;

    if (scanf("%1000s", s) != 1) return 1;

    for (i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            pila[tope++] = '(';
        } else if (s[i] == ')') {
            if (tope == 0) {
                valido = 0;
                break;
            }
            tope--;
        }
    }

    if (valido && tope == 0)
        puts("BALANCEADO");
    else
        puts("NO BALANCEADO");

    return 0;
}
