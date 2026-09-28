#include <stdio.h>

int main() {
    float horas_trabajadas;
    float costo_por_hora;
    float costo_total;

    printf("=====================================================\n");
    printf("   CALCULO DE COSTOS DE PROCESAMIENTO DE DATOS      \n");
    printf("=====================================================\n");

    printf("Ingrese las horas dedicadas por el analista: ");
    if (scanf("%f", &horas_trabajadas) != 1 || horas_trabajadas < 0) {
        printf("Error: Entrada invalida para horas trabajadas.\n");
        return 1;
    }

    printf("Ingrese la tarifa (costo por hora en S/.): ");
    if (scanf("%f", &costo_por_hora) != 1 || costo_por_hora < 0) {
        printf("Error: Entrada invalida para costo por hora.\n");
        return 1;
    }

    costo_total = horas_trabajadas * costo_por_hora;

    printf("\n---------------- RESUMEN DE PROCESAMIENTO -----------\n");
    printf(" Horas trabajadas : %.2f hrs\n", horas_trabajadas);
    printf(" Tarifa aplicada  : S/. %.2f por hora\n", costo_por_hora);
    printf(" Costo total final: S/. %.2f\n", costo_total);
    printf("-----------------------------------------------------\n");

    return 0;
}
