#include <stdio.h>

int main() {
    int n;
    long long contador_lineal = 0;
    long long contador_cuadratico = 0;

    printf("=====================================================\n");
    printf("    ANALISIS DE COMPLEJIDAD: O(n) vs O(n^2)          \n");
    printf("=====================================================\n");

    printf("Ingrese la cantidad de elementos n (ej. 10, 50, 100, 500): ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Error: Ingrese un valor entero positivo para n.\n");
        return 1;
    }

    // Procedimiento 1: Un solo recorrido de n elementos -> O(n)
    for (int i = 0; i < n; i++) {
        contador_lineal++;
    }

    // Procedimiento 2: Dos ciclos anidados de n iteraciones -> O(n^2)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            contador_cuadratico++;
        }
    }

    double ratio = (contador_lineal > 0) ? ((double)contador_cuadratico / (double)contador_lineal) : 0.0;

    printf("\n+------------------------------+--------------------+\n");
    printf("| Parametro / Procedimiento    | Valor              |\n");
    printf("+------------------------------+--------------------+\n");
    printf("| Tamanio de entrada (n)       | %-18d |\n", n);
    printf("| Operaciones Lineales O(n)    | %-18lld |\n", contador_lineal);
    printf("| Operaciones Cuadraticas O(n2)| %-18lld |\n", contador_cuadratico);
    printf("| Factor de escala (O(n2)/O(n))| %-18.2f |\n", ratio);
    printf("+------------------------------+--------------------+\n");

    printf("\nInterpretacion Teorico-Practica:\n");
    printf("1. En O(n), el crecimiento del tiempo es lineal: se realizaron exactamente n = %d ops.\n", n);
    printf("2. En O(n^2), el crecimiento es cuadratico: se realizaron exactamente n^2 = %lld ops.\n", contador_cuadratico);
    printf("3. Notese que el factor de escala es exactamente n = %.0f, lo que demuestra que al duplicar n,\n", ratio);
    printf("   el procedimiento O(n^2) incrementa su costo computacional en un factor cuadratico (x4).\n");
    printf("=====================================================\n");

    return 0;
}
