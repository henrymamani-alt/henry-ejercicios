#include <iostream>
#include <stack>

using namespace std;

int main() {
    stack<int> pila;
    const int TOTAL = 5;

    cout << "=====================================================" << endl;
    cout << "      EJERCICIO 1: APILAR NUMEROS ENTEROS (LIFO)     " << endl;
    cout << "=====================================================" << endl;
    cout << "Ingrese " << TOTAL << " numeros enteros para apilar:" << endl;

    for (int i = 1; i <= TOTAL; i++) {
        int valor;
        cout << "Elemento [" << i << "/" << TOTAL << "]: ";
        cin >> valor;
        pila.push(valor);
        cout << "  -> Insertado en la pila (push). Tope actual: " << pila.top() << endl;
    }

    cout << "\n---------------- DESAPILANDO ELEMENTOS --------------" << endl;
    cout << "Orden de salida para verificar el principio LIFO:" << endl;

    int orden = 1;
    while (!pila.empty()) {
        cout << "Extraccion #" << orden << ": " << pila.top() << " (retirado con pop)" << endl;
        pila.pop();
        orden++;
    }

    cout << "-----------------------------------------------------" << endl;
    cout << "Estado final de la pila: " << (pila.empty() ? "VACIA (empty() == true)" : "NO VACIA") << endl;
    cout << "=====================================================" << endl;

    return 0;
}
