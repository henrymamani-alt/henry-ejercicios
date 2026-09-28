#include <stdio.h>
#include <stdbool.h>

int main() {
    int edad;
    int estado_validacion; // 1 = Validado, 0 = No validado

    printf("=====================================================\n");
    printf("   FILTRO DE ADMISION DE OBSERVACIONES AL ESTUDIO    \n");
    printf("=====================================================\n");

    printf("Ingrese la edad del individuo: ");
    scanf("%d", &edad);

    printf("Ha sido validado el registro? (1 = Si / 0 = No): ");
    scanf("%d", &estado_validacion);

    bool es_mayor_edad = (edad >= 18);
    bool esta_validado = (estado_validacion == 1);

    // Operador logico AND (&&)
    bool puede_incorporarse = es_mayor_edad && esta_validado;

    printf("\n---------------- VERIFICACION DE CONDICIONES ---------\n");
    printf(" Condicion 1 (Edad >= 18)   : %d anios -> %s\n", edad, es_mayor_edad ? "VERDADERO" : "FALSO");
    printf(" Condicion 2 (Validado == 1): %d -> %s\n", estado_validacion, esta_validado ? "VERDADERO" : "FALSO");
    printf(" Expresion logica           : (edad >= 18) && (validado == 1)\n");
    printf(" Evaluacion                 : %s\n", puede_incorporarse ? "TRUE" : "FALSE");
    printf("-----------------------------------------------------\n");

    if (puede_incorporarse) {
        printf(" >> DICTAMEN: La observacion PUEDE incorporarse al conjunto de datos.\n");
    } else {
        printf(" >> DICTAMEN: La observacion NO PUEDE incorporarse al analisis.\n");
    }
    printf("=====================================================\n");

    return 0;
}
