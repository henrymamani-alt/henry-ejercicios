#include <stdio.h>

int main() {
    int total_registros;
    int num_nodos;

    printf("=====================================================\n");
    printf("    DISTRIBUCION DE CARGA ENTRE NODOS DE COMPUTO     \n");
    printf("=====================================================\n");

    printf("Ingrese el numero total de registros del dataset: ");
    scanf("%d", &total_registros);

    printf("Ingrese el numero de nodos de procesamiento: ");
    scanf("%d", &num_nodos);

    if (num_nodos <= 0 || total_registros < 0) {
        printf("Error: El numero de nodos debe ser mayor a 0 y los registros no negativos.\n");
        return 1;
    }

    int registros_por_nodo = total_registros / num_nodos;
    int registros_restantes = total_registros % num_nodos;

    printf("\n---------------- REPARTO DE CARGA DE TRABAJO --------\n");
    printf(" Total de registros recibidos      : %d\n", total_registros);
    printf(" Cantidad de nodos disponibles     : %d\n", num_nodos);
    printf(" Registros procesados por cada nodo: %d\n", registros_por_nodo);
    printf(" Registros sin distribuir uniforme : %d\n", registros_restantes);
    printf(" Verificacion (nodos*carga + resto): %d * %d + %d = %d\n",
           num_nodos, registros_por_nodo, registros_restantes,
           (num_nodos * registros_por_nodo + registros_restantes));
    printf("-----------------------------------------------------\n");

    return 0;
}
