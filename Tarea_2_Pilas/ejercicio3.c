#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX 200

typedef struct {
    char datos[MAX];
    int tope;
} PilaChar;

void inicializar(PilaChar *p) { p->tope = -1; }
bool esta_vacia(PilaChar *p) { return p->tope == -1; }
void apilar(PilaChar *p, char c) { p->datos[++(p->tope)] = c; }
char desapilar(PilaChar *p) { return p->datos[(p->tope)--]; }

int main() {
    PilaChar p;
    inicializar(&p);
    char expresion[MAX];

    printf("=====================================================\n");
    printf("   EJERCICIO 3: VERIFICAR PARENTESIS EN C            \n");
    printf("=====================================================\n");
    printf("Ingrese la expresion a evaluar: ");
    fgets(expresion, MAX, stdin);
    expresion[strcspn(expresion, "\n")] = 0;

    bool balanceado = true;
    char motivo[MAX] = "Expresion correctamente balanceada.";

    int len = strlen(expresion);
    for (int i = 0; i < len; i++) {
        if (expresion[i] == '(') {
            apilar(&p, '(');
        } else if (expresion[i] == ')') {
            if (esta_vacia(&p)) {
                balanceado = false;
                snprintf(motivo, MAX, "Se encontro ')' en la posicion %d sin apertura pendiente.", i + 1);
                break;
            }
            desapilar(&p);
        }
    }

    if (balanceado && !esta_vacia(&p)) {
        balanceado = false;
        snprintf(motivo, MAX, "Existen parentesis de apertura '(' sin cerrar.");
    }

    printf("\n---------------- EVALUACION DE SINTAXIS -------------\n");
    printf(" Expresion analizada : %s\n", expresion);
    printf(" Estado de balanceo   : %s\n", balanceado ? "CORRECTO (Balanceado)" : "INCORRECTO (Desbalanceado)");
    printf(" Detalle / Diagnostico: %s\n", motivo);
    printf("-----------------------------------------------------\n");

    return 0;
}
