#include <stdio.h>

int main() {
    float temperatura;

    printf("=====================================================\n");
    printf("      CLASIFICACION DE TEMPERATURAS CLIMATICAS       \n");
    printf("=====================================================\n");

    printf("Ingrese la temperatura registrada por el sensor (en C): ");
    if (scanf("%f", &temperatura) != 1) {
        printf("Error: Registro de temperatura invalido.\n");
        return 1;
    }

    printf("\n---------------- RESULTADO DE EVALUACION -------------\n");
    printf(" Temperatura sensada: %.2f C\n", temperatura);
    printf(" Clasificacion      : ");

    if (temperatura < 0.0f) {
        printf("CONGELACION (< 0 C)\n");
        printf(" Observacion        : Condiciones bajo el punto de congelacion.\n");
    } else if (temperatura >= 0.0f && temperatura <= 20.0f) {
        printf("FRIO (0 C a 20 C)\n");
        printf(" Observacion        : Rango termico bajo, caracteristico de zonas andinas.\n");
    } else {
        printf("TEMPLADO (> 20 C)\n");
        printf(" Observacion        : Rango termico moderado y calido.\n");
    }
    printf("-----------------------------------------------------\n");

    return 0;
}
