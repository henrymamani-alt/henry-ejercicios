#include <iostream>
#include <stack>
#include <string>

using namespace std;

bool verificarBalanceo(const string& expresion, string& motivo) {
    stack<char> pila;

    for (size_t i = 0; i < expresion.length(); i++) {
        char c = expresion[i];
        if (c == '(') {
            pila.push(c);
        } else if (c == ')') {
            if (pila.empty()) {
                motivo = "Se encontro ')' en la posicion " + to_string(i + 1) + " sin parentesis de apertura pendiente.";
                return false;
            }
            pila.pop(); // Pareja de parentesis encontrada
        }
    }

    if (!pila.empty()) {
        motivo = "Existen " + to_string(pila.size()) + " parentesis de apertura '(' que nunca fueron cerrados.";
        return false;
    }

    motivo = "Todos los parentesis estan correctamente abiertos y cerrados (balanceados).";
    return true;
}

int main() {
    string expresion;

    cout << "=====================================================" << endl;
    cout << "   EJERCICIO 3: VERIFICAR PARENTESIS BALANCEADOS     " << endl;
    cout << "=====================================================" << endl;

    cout << "Ingrese la expresion a evaluar (ej. (a+b)*(c-d)): ";
    getline(cin >> ws, expresion);

    string motivo;
    bool balanceado = verificarBalanceo(expresion, motivo);

    cout << "\n---------------- EVALUACION DE SINTAXIS -------------" << endl;
    cout << " Expresion analizada : " << expresion << endl;
    cout << " Estado de balanceo   : " << (balanceado ? "CORRECTO (Balanceado)" : "INCORRECTO (Desbalanceado)") << endl;
    cout << " Detalle / Diagnostico: " << motivo << endl;
    cout << "-----------------------------------------------------" << endl;

    return 0;
}
