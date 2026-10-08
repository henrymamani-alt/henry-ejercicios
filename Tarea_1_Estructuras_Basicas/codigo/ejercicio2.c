#include <stdio.h>
#include <stdbool.h>

int main() {
    int id;                      // Identificador unico (entero)
    int edad;                    // Edad de la observacion (entero)
    double valor_promedio;       // Valor promedio de una variable continua (flotante doble precision)
    char categoria;              // Categoria representada por una letra (caracter)
    bool es_valido;              // Estado de validez del registro (booleano)
    int entrada_validez;

    printf("=====================================================\n");
    printf("        REGISTRO DE OBSERVACION DE DATOS             \n");
    printf("=====================================================\n");

    printf("Ingrese ID del registro (ej. 101): ");
    scanf("%d", &id);

    printf("Ingrese la edad del individuo: ");
    scanf("%d", &edad);

    printf("Ingrese el valor promedio de la variable (ej. 84.75): ");
    scanf("%lf", &valor_promedio);

    printf("Ingrese la categoria (letra A, B, C, etc.): ");
    scanf(" %c", &categoria);

    printf("Estado de validez (1 = Valido, 0 = Invalido): ");
    scanf("%d", &entrada_validez);
    es_valido = (entrada_validez != 0);

    printf("\n================ RESUMEN DE OBSERVACION =============\n");
    printf(" [1] Identificador (int)        : %d\n", id);
    printf(" [2] Edad (int)                 : %d anios\n", edad);
    printf(" [3] Valor Promedio (double)    : %.4f\n", valor_promedio);
    printf(" [4] Categoria (char)           : %c\n", categoria);
    printf(" [5] Estado de Validez (bool)   : %s\n", es_valido ? "VALIDO (true)" : "INVALIDO (false)");
    printf("=====================================================\n");

    return 0;
}
