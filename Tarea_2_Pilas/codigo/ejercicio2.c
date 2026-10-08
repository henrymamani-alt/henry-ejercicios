#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX 100

typedef struct {
    char datos[MAX];
    int tope;
} PilaChar;

void inicializar(PilaChar *p) { p->tope = -1; }
bool esta_vacia(PilaChar *p) { return p->tope == -1; }
void apilar(PilaChar *p, char c) { p->datos[++(p->tope)] = c; }
char desapilar(PilaChar *p) { return p->datos[(p->tope)--]; }
char consultar_tope(PilaChar *p) { return p->datos[p->tope]; }

int main() {
    PilaChar p;
    inicializar(&p);
    char palabra[MAX];
    char palabraInvertida[MAX];
    int idx = 0;

    printf("=====================================================\n");
    printf("     EJERCICIO 2: INVERTIR UNA PALABRA EN C          \n");
    printf("=====================================================\n");
    printf("Ingrese una palabra: ");
    scanf("%s", palabra);

    printf("\n[Paso 1] Apilando caracteres de '%s':\n", palabra);
    int len = strlen(palabra);
    for (int i = 0; i < len; i++) {
        apilar(&p, palabra[i]);
        printf("  Caracter '%c' apilado -> Tope: '%c'\n", palabra[i], consultar_tope(&p));
    }

    printf("\n[Paso 2] Desapilando para invertir (LIFO):\n");
    while (!esta_vacia(&p)) {
        palabraInvertida[idx++] = desapilar(&p);
    }
    palabraInvertida[idx] = '\0';

    printf("\n---------------- RESULTADO FINAL --------------------\n");
    printf(" Palabra original  : %s\n", palabra);
    printf(" Palabra invertida : %s\n", palabraInvertida);
    printf("-----------------------------------------------------\n");

    return 0;
}
