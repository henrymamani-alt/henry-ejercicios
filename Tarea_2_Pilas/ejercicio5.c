#include <stdio.h>
#include <stdbool.h>

#define MAX_BITS 64

typedef struct {
    int datos[MAX_BITS];
    int tope;
} PilaInt;

void inicializar(PilaInt *p) { p->tope = -1; }
bool esta_vacia(PilaInt *p) { return p->tope == -1; }
void apilar(PilaInt *p, int val) { p->datos[++(p->tope)] = val; }
int desapilar(PilaInt *p) { return p->datos[(p->tope)--]; }

int main() {
    PilaInt p;
    inicializar(&p);
    int decimalOriginal;

    printf("=====================================================\n");
    printf("   EJERCICIO 5: DECIMAL A BINARIO EN C (LIFO)        \n");
    printf("=====================================================\n");
    printf("Ingrese un numero entero decimal positivo: ");
    if (scanf("%d", &decimalOriginal) != 1 || decimalOriginal < 0) {
        printf("Error: Entrada invalida.\n");
        return 1;
    }

    if (decimalOriginal == 0) {
        printf("El numero 0 en binario es: 0\n");
        return 0;
    }

    int n = decimalOriginal;
    printf("\nDividiendo entre 2 y apilando residuos:\n");
    while (n > 0) {
        int residuo = n % 2;
        int cociente = n / 2;
        apilar(&p, residuo);
        printf("  %d / 2 = %d | Residuo: %d apilado\n", n, cociente, residuo);
        n = cociente;
    }

    printf("\nNumero binario resultante (LIFO): ");
    while (!esta_vacia(&p)) {
        printf("%d", desapilar(&p));
    }
    printf("\n-----------------------------------------------------\n");

    return 0;
}
