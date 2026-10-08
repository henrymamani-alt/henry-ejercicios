#include <stdio.h>
#include <stdbool.h>

#define CAPACIDAD 10

typedef struct {
    int datos[CAPACIDAD];
    int tope;
} Pila;

void inicializar(Pila *p) { p->tope = -1; }
bool esta_vacia(Pila *p) { return p->tope == -1; }
void apilar(Pila *p, int val) { p->datos[++(p->tope)] = val; }
int desapilar(Pila *p) { return p->datos[(p->tope)--]; }
int consultar_tope(Pila *p) { return p->datos[p->tope]; }

int main() {
    Pila p;
    inicializar(&p);
    const int TOTAL = 5;

    printf("=====================================================\n");
    printf("   EJERCICIO 1: APILAR NUMEROS ENTEROS EN C (LIFO)   \n");
    printf("=====================================================\n");
    printf("Ingrese %d numeros enteros para apilar:\n", TOTAL);

    for (int i = 1; i <= TOTAL; i++) {
        int valor;
        printf("Elemento [%d/%d]: ", i, TOTAL);
        scanf("%d", &valor);
        apilar(&p, valor);
        printf("  -> Insertado en la pila (push). Tope actual: %d\n", consultar_tope(&p));
    }

    printf("\n---------------- DESAPILANDO ELEMENTOS --------------\n");
    printf("Orden de salida para verificar el principio LIFO:\n");

    int orden = 1;
    while (!esta_vacia(&p)) {
        printf("Extraccion #%d: %d (retirado con pop)\n", orden, desapilar(&p));
        orden++;
    }

    printf("-----------------------------------------------------\n");
    printf("Estado final de la pila: %s\n", esta_vacia(&p) ? "VACIA (empty() == true)" : "NO VACIA");
    printf("=====================================================\n");

    return 0;
}
