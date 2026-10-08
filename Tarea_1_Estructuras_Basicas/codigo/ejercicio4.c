#include <stdio.h>

int main() {
    int reg_algoritmo1;
    int reg_algoritmo2;

    printf("=====================================================\n");
    printf("   COMPARATIVA Y ARITMETICA DE REGISTROS (ALGORITMOS)\n");
    printf("=====================================================\n");

    printf("Ingrese registros procesados por Algoritmo 1: ");
    scanf("%d", &reg_algoritmo1);

    printf("Ingrese registros procesados por Algoritmo 2: ");
    scanf("%d", &reg_algoritmo2);

    int suma = reg_algoritmo1 + reg_algoritmo2;
    int diferencia = reg_algoritmo1 - reg_algoritmo2;
    long long producto = (long long)reg_algoritmo1 * reg_algoritmo2;

    printf("\n+--------------------+-----------------------------+\n");
    printf("| Operacion          | Resultado                   |\n");
    printf("+--------------------+-----------------------------+\n");
    printf("| Suma (+)           | %-27d |\n", suma);
    printf("| Diferencia (-)     | %-27d |\n", diferencia);
    printf("| Producto (*)       | %-27lld |\n", producto);

    if (reg_algoritmo2 != 0) {
        int division_entera = reg_algoritmo1 / reg_algoritmo2;
        int residuo = reg_algoritmo1 % reg_algoritmo2;
        printf("| Division Entera (/)| %-27d |\n", division_entera);
        printf("| Residuo / Modulo(%%)| %-27d |\n", residuo);
    } else {
        printf("| Division Entera (/)| Indefinida (division por 0) |\n");
        printf("| Residuo / Modulo(%%)| Indefinido (modulo por 0)   |\n");
    }
    printf("+--------------------+-----------------------------+\n");

    return 0;
}
