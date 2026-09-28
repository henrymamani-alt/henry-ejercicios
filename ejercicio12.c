#include <stdio.h>

#define MAX_MEDICIONES 10

int main() {
    int validos = 0;
    double valor;
    double lista_validos[MAX_MEDICIONES];

    printf("=====================================================\n");
    printf("  PROCESAMIENTO DE MEDICIONES CON CONTINUE Y BREAK(C)\n");
    printf("=====================================================\n");
    printf("Instrucciones: Se esperan hasta 10 mediciones.\n");
    printf("- Valores negativos: Se omiten con continue.\n");
    printf("- Valor 999        : Finaliza la captura con break.\n\n");

    for (int i = 1; i <= MAX_MEDICIONES; i++) {
        printf("Entrada %d de %d - Ingrese medicion: ", i, MAX_MEDICIONES);
        scanf("%lf", &valor);

        // Finalizacion inmediata si se introduce 999 mediante break
        if (valor == 999.0) {
            printf(">> [BREAK] Se introdujo el codigo de parada 999. Finalizando proceso...\n");
            break;
        }

        // Omitir valores negativos considerandolos invalidos mediante continue
        if (valor < 0.0) {
            printf(">> [CONTINUE] Medicion negativa (%.2f) invalida. Se omite.\n", valor);
            continue;
        }

        // Si es valido, se contabiliza y almacena en el arreglo
        lista_validos[validos] = valor;
        validos++;
        printf("   -> Medicion %.2f registrada correctamente como valida.\n", valor);
    }

    printf("\n---------------- RESUMEN FINAL DEL PROCESAMIENTO ----\n");
    printf(" Total de valores validos procesados: %d\n", validos);
    printf(" Valores validos registrados: ");
    if (validos == 0) {
        printf("Ninguno\n");
    } else {
        for (int j = 0; j < validos; j++) {
            printf("%.2f%s", lista_validos[j], (j + 1 < validos) ? ", " : "\n");
        }
    }
    printf("-----------------------------------------------------\n");

    return 0;
}
