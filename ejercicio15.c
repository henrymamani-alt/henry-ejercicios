#include <stdio.h>

// Funcion 1: Recibe 3 mediciones y calcula su media aritmetica
double calcular_promedio(double m1, double m2, double m3) {
    return (m1 + m2 + m3) / 3.0;
}

// Funcion 2: Determina cuantas mediciones estan por encima del promedio
int contar_superiores_promedio(double m1, double m2, double m3, double promedio) {
    int contador = 0;
    if (m1 > promedio) contador++;
    if (m2 > promedio) contador++;
    if (m3 > promedio) contador++;
    return contador;
}

int main() {
    double m1, m2, m3;

    printf("=====================================================\n");
    printf("   MODULARIDAD: PROMEDIO Y COMPARACION DE 3 MUESTRAS \n");
    printf("=====================================================\n");

    printf("Ingrese la medicion 1: ");
    scanf("%lf", &m1);

    printf("Ingrese la medicion 2: ");
    scanf("%lf", &m2);

    printf("Ingrese la medicion 3: ");
    scanf("%lf", &m3);

    // Invocacion de la funcion calcular_promedio
    double promedio = calcular_promedio(m1, m2, m3);

    // Invocacion de la funcion contar_superiores_promedio
    int mayores = contar_superiores_promedio(m1, m2, m3, promedio);

    printf("\n---------------- RESUMEN DE RESULTADOS --------------\n");
    printf(" Mediciones ingresadas : [%.2f, %.2f, %.2f]\n", m1, m2, m3);
    printf(" Promedio calculado    : %.4f\n", promedio);
    printf(" Mediciones > promedio : %d de 3\n", mayores);

    printf("\nDetalle individual:\n");
    printf(" - Medicion 1 (%.2f): %s\n", m1, (m1 > promedio) ? "SUPERIOR al promedio" : "Menor o igual al promedio");
    printf(" - Medicion 2 (%.2f): %s\n", m2, (m2 > promedio) ? "SUPERIOR al promedio" : "Menor o igual al promedio");
    printf(" - Medicion 3 (%.2f): %s\n", m3, (m3 > promedio) ? "SUPERIOR al promedio" : "Menor o igual al promedio");
    printf("-----------------------------------------------------\n");

    return 0;
}
