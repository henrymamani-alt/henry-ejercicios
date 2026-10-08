#include <stdio.h>

#define N 10

int main() {
    double mediciones[N];
    double suma = 0.0;
    double media = 0.0;
    int conteo_superiores = 0;

    printf("=====================================================\n");
    printf("  ANALISIS ESTADISTICO DE 10 MEDICIONES (C)          \n");
    printf("=====================================================\n");

    // Ciclo for para ingresar los valores y acumular suma
    for (int i = 0; i < N; i++) {
        printf("Ingrese la medicion [%d/%d]: ", i + 1, N);
        scanf("%lf", &mediciones[i]);
        suma += mediciones[i];
    }

    // Calculo de la media aritmetica
    media = suma / N;

    // Determinar cuantas observaciones estan por encima de la media
    for (int i = 0; i < N; i++) {
        if (mediciones[i] > media) {
            conteo_superiores++;
        }
    }

    printf("\n---------------- RESUMEN ESTADISTICO ----------------\n");
    printf(" Suma total acumulada            : %.2f\n", suma);
    printf(" Media aritmetica del grupo      : %.2f\n", media);
    printf(" Observaciones mayores a la media: %d de %d\n", conteo_superiores, N);
    printf("\nDetalle de observaciones y clasificacion respecto a la media:\n");
    for (int i = 0; i < N; i++) {
        printf(" Obs %2d: %7.2f", i + 1, mediciones[i]);
        if (mediciones[i] > media) {
            printf("  -> Por encima de la media (+)\n");
        } else if (mediciones[i] < media) {
            printf("  -> Por debajo de la media (-)\n");
        } else {
            printf("  -> Igual a la media\n");
        }
    }
    printf("-----------------------------------------------------\n");

    return 0;
}
