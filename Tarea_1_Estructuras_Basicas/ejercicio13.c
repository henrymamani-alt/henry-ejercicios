#include <stdio.h>

#define N 10

int main() {
    int edades[N];
    int min_edad, max_edad;
    double suma = 0.0, media = 0.0;
    int sobre_media = 0;

    printf("=====================================================\n");
    printf("   ESTUDIO DEMOGRAFICO: ANALISIS DE 10 EDADES        \n");
    printf("=====================================================\n");

    for (int i = 0; i < N; i++) {
        printf("Ingrese la edad del participante [%d/%d]: ", i + 1, N);
        scanf("%d", &edades[i]);
        suma += edades[i];
    }

    // Inicializar min y max con el primer elemento
    min_edad = edades[0];
    max_edad = edades[0];

    for (int i = 1; i < N; i++) {
        if (edades[i] < min_edad) min_edad = edades[i];
        if (edades[i] > max_edad) max_edad = edades[i];
    }

    media = suma / N;

    for (int i = 0; i < N; i++) {
        if (edades[i] > media) {
            sobre_media++;
        }
    }

    printf("\n---------------- RESULTADOS ESTADISTICOS ------------\n");
    printf(" Lista de edades ingresadas: ");
    for (int i = 0; i < N; i++) {
        printf("%d%s", edades[i], (i < N - 1) ? ", " : "\n");
    }
    printf(" Edad minima en el grupo    : %d anios\n", min_edad);
    printf(" Edad maxima en el grupo    : %d anios\n", max_edad);
    printf(" Edad media del grupo       : %.2f anios\n", media);
    printf(" Participantes con edad > media: %d participantes\n", sobre_media);
    printf("-----------------------------------------------------\n");

    return 0;
}
