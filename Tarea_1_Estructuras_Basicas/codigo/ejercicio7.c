#include <stdio.h>
#include <stdbool.h>

int main() {
    int observaciones_validas;
    double porcentaje_completos;

    printf("=====================================================\n");
    printf("     CONTROL DE CALIDAD DE CONJUNTO DE DATOS         \n");
    printf("=====================================================\n");

    printf("Ingrese la cantidad de observaciones validas: ");
    scanf("%d", &observaciones_validas);

    printf("Ingrese el porcentaje de datos completos (0 - 100 %%): ");
    scanf("%lf", &porcentaje_completos);

    // Criterios minimos: obs >= 100 y pct >= 70.0%
    bool cumple_obs = (observaciones_validas >= 100);
    bool cumple_pct = (porcentaje_completos >= 70.0);
    bool aceptado = cumple_obs && cumple_pct;

    printf("\n---------------- EVALUACION DE CRITERIOS ------------\n");
    printf(" 1. Observaciones validas (>= 100): %d [%s]\n",
           observaciones_validas, cumple_obs ? "CUMPLE" : "NO CUMPLE");
    printf(" 2. Datos completos (>= 70.00%%)   : %.2f%% [%s]\n",
           porcentaje_completos, cumple_pct ? "CUMPLE" : "NO CUMPLE");
    printf("-----------------------------------------------------\n");

    if (aceptado) {
        printf(" >> RESULTADO: CONJUNTO DE DATOS ACEPTADO PARA ANALISIS.\n");
    } else {
        printf(" >> RESULTADO: CONJUNTO DE DATOS RECHAZADO.\n");
        printf("    Motivo(s): ");
        if (!cumple_obs) printf("[Faltan observaciones minimas] ");
        if (!cumple_pct) printf("[Porcentaje de completitud insuficiente] ");
        printf("\n");
    }
    printf("-----------------------------------------------------\n");

    return 0;
}
