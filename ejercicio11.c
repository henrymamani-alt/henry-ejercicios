#include <stdio.h>
#include <stdbool.h>

int main() {
    const int CLAVE_CORRECTA = 2026;
    int clave_ingresada = 0;
    int intentos = 0;
    bool acceso_concedido = false;

    printf("=====================================================\n");
    printf("  SISTEMA DE AUTENTICACION PARA CARGA DE DATOS (C)   \n");
    printf("=====================================================\n");
    printf("(Clave de acceso predefinida: 2026)\n\n");

    // Ciclo while para solicitar repetidamente la clave
    while (!acceso_concedido) {
        intentos++;
        printf("Intento #%d - Ingrese la clave numerica de acceso: ", intentos);
        scanf("%d", &clave_ingresada);

        if (clave_ingresada == CLAVE_CORRECTA) {
            acceso_concedido = true;
            printf("\n[!] ACCESO CONCEDIDO.\n");
            printf("    Bienvenido al modulo de carga de datos.\n");
        } else {
            printf("[-] Clave incorrecta. Acceso denegado. Intente nuevamente.\n\n");
        }
    }

    printf("-----------------------------------------------------\n");
    printf(" Resumen de inicio de sesion:\n");
    printf(" Numero total de intentos realizados: %d\n", intentos);
    printf(" Estado final: Autenticacion exitosa.\n");
    printf("=====================================================\n");

    return 0;
}
