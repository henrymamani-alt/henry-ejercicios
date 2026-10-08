#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    stack<char> pilaCaracteres;
    string palabra;
    string palabraInvertida = "";

    cout << "=====================================================" << endl;
    cout << "        EJERCICIO 2: INVERTIR UNA PALABRA            " << endl;
    cout << "=====================================================" << endl;

    cout << "Ingrese una palabra: ";
    cin >> palabra;

    // 1. Apilar cada caracter (push)
    cout << "\n[Paso 1] Apilando caracteres de '" << palabra << "':" << endl;
    for (size_t i = 0; i < palabra.length(); i++) {
        pilaCaracteres.push(palabra[i]);
        cout << "  Caracter '" << palabra[i] << "' apilado -> Tope: '" << pilaCaracteres.top() << "'" << endl;
    }

    // 2. Desapilar caracteres (pop) para construir la palabra invertida
    cout << "\n[Paso 2] Desapilando para invertir (LIFO):" << endl;
    while (!pilaCaracteres.empty()) {
        palabraInvertida += pilaCaracteres.top();
        pilaCaracteres.pop();
    }

    cout << "\n---------------- RESULTADO FINAL --------------------" << endl;
    cout << " Palabra original  : " << palabra << endl;
    cout << " Palabra invertida : " << palabraInvertida << endl;
    cout << "-----------------------------------------------------" << endl;
    cout << "Justificacion: Al seguir la disciplina LIFO (Last In, First Out),\n"
         << "el ultimo caracter ingresado es el primero en desapilarse,\n"
         << "lo que produce la inversion natural de la secuencia." << endl;
    cout << "=====================================================" << endl;

    return 0;
}
