#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    int decimalOriginal;
    stack<int> pilaResiduos;

    cout << "=====================================================" << endl;
    cout << "     EJERCICIO 5: CONVERSION DE DECIMAL A BINARIO    " << endl;
    cout << "=====================================================" << endl;

    cout << "Ingrese un numero entero decimal positivo: ";
    if (!(cin >> decimalOriginal) || decimalOriginal < 0) {
        cout << "Error: Debe ingresar un entero no negativo." << endl;
        return 1;
    }

    if (decimalOriginal == 0) {
        cout << "\n---------------- PROCESO DE CONVERSION --------------" << endl;
        cout << "El numero 0 en binario es: 0" << endl;
        cout << "=====================================================" << endl;
        return 0;
    }

    int n = decimalOriginal;
    cout << "\n---------------- DIVISIONES SUCESIVAS (/ 2) ----------" << endl;
    cout << "Dividiendo entre 2 y apilando residuos:" << endl;

    while (n > 0) {
        int residuo = n % 2;
        int cociente = n / 2;
        pilaResiduos.push(residuo);
        cout << "  " << n << " / 2 = " << cociente << " | Residuo: " << residuo
             << " -> Apilado (push). Tope: " << pilaResiduos.top() << endl;
        n = cociente;
    }

    cout << "\n---------------- DESAPILANDO RESIDUOS (LIFO) --------" << endl;
    string binario = "";
    while (!pilaResiduos.empty()) {
        binario += to_string(pilaResiduos.top());
        pilaResiduos.pop();
    }

    cout << " Numero decimal original : " << decimalOriginal << endl;
    cout << " Representacion binaria  : " << binario << endl;
    cout << "-----------------------------------------------------" << endl;
    cout << "Explicacion: Los residuos se generan del bit menos significativo (LSB)\n"
         << "al mas significativo (MSB). La pila invierte el orden de salida,\n"
         << "entregando el numero binario correctamente leido de MSB a LSB." << endl;
    cout << "=====================================================" << endl;

    return 0;
}
