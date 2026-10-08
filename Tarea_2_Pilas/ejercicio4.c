#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_HISTORIAL 50
#define MAX_TEXTO 100

typedef struct {
    char acciones[MAX_HISTORIAL][MAX_TEXTO];
    int tope;
} PilaAcciones;

void inicializar(PilaAcciones *p) { p->tope = -1; }
bool esta_vacia(PilaAcciones *p) { return p->tope == -1; }
void apilar(PilaAcciones *p, const char *accion) {
    if (p->tope < MAX_HISTORIAL - 1) {
        strcpy(p->acciones[++(p->tope)], accion);
    }
}
void desapilar(PilaAcciones *p, char *salida) {
    if (!esta_vacia(p)) {
        strcpy(salida, p->acciones[(p->tope)--]);
    }
}
const char* consultar_tope(PilaAcciones *p) {
    return esta_vacia(p) ? "" : p->acciones[p->tope];
}

int main() {
    PilaAcciones historial;
    inicializar(&historial);
    int opcion;

    printf("=====================================================\n");
    printf("     EJERCICIO 4: HISTORIAL DESHACER EN C            \n");
    printf("=====================================================\n");

    do {
        printf("\n1. Registrar accion | 2. Deshacer | 3. Ver tope | 4. Salir\nOpcion: ");
        if (scanf("%d", &opcion) != 1) break;
        getchar(); // limpiar salto

        if (opcion == 1) {
            char accion[MAX_TEXTO];
            printf("Descripcion de la accion: ");
            fgets(accion, MAX_TEXTO, stdin);
            accion[strcspn(accion, "\n")] = 0;
            apilar(&historial, accion);
            printf("[+] Registrado: '%s'\n", accion);
        } else if (opcion == 2) {
            if (esta_vacia(&historial)) {
                printf("[-] Historial vacio.\n");
            } else {
                char rev[MAX_TEXTO];
                desapilar(&historial, rev);
                printf("[<-- DESHACER] Revertida accion: '%s'\n", rev);
            }
        } else if (opcion == 3) {
            if (esta_vacia(&historial)) {
                printf("[i] Tope vacio.\n");
            } else {
                printf("[TOPE ACTUAL] '%s'\n", consultar_tope(&historial));
            }
        }
    } while (opcion != 4);

    return 0;
}
