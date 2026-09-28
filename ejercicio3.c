#include <stdio.h>

int main() {
    double medicion_decimal;
    int medicion_entera;
    double valor_perdido;

    printf("=====================================================\n");
    printf("    CONVERSION EXPLICITA (CASTING) DE SENSOR         \n");
    printf("=====================================================\n");

    printf("Ingrese la medicion decimal del sensor (ej. 18.9): ");
    if (scanf("%lf", &medicion_decimal) != 1) {
        printf("Error: Entrada invalida.\n");
        return 1;
    }

    // Conversion explicita (casting) a entero
    medicion_entera = (int)medicion_decimal;

    // Calculo del valor decimal que se pierde
    valor_perdido = medicion_decimal - (double)medicion_entera;

    printf("\n---------------- RESULTADOS DE CONVERSION -----------\n");
    printf(" Valor original (decimal) : %.4f\n", medicion_decimal);
    printf(" Valor convertido (entero): %d\n", medicion_entera);
    printf(" Valor decimal perdido    : %.4f\n", valor_perdido);
    printf(" Porcentaje de perdida    : %.2f%%\n", (valor_perdido / medicion_decimal) * 100.0);
    printf("-----------------------------------------------------\n");

    return 0;
}
