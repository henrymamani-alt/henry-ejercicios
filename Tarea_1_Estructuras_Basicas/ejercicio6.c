#include <stdio.h>

int main() {
    int registros_acumulados;

    printf("=====================================================\n");
    printf("   SEGUIMIENTO DE ESTADO DE VARIABLE ACUMULADA       \n");
    printf("=====================================================\n");

    // 1. Inicializacion en 4
    registros_acumulados = 4;
    printf("[Paso 1] Inicializacion:\n");
    printf("         registros_acumulados = %d\n\n", registros_acumulados);

    // 2. Incremento en 3
    registros_acumulados += 3;
    printf("[Paso 2] Incremento en 3 (operador += 3):\n");
    printf("         registros_acumulados = %d\n\n", registros_acumulados);

    // 3. Duplicacion del resultado
    registros_acumulados *= 2;
    printf("[Paso 3] Duplicar resultado (operador *= 2):\n");
    printf("         registros_acumulados = %d\n\n", registros_acumulados);

    printf("=====================================================\n");
    printf(" Estado final del acumulador de registros: %d\n", registros_acumulados);
    printf("=====================================================\n");

    return 0;
}
