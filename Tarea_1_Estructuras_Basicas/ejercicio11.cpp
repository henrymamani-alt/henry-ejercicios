#include <iostream>

using namespace std;

int main() {
    const int CLAVE_CORRECTA = 2026;
    int clave_ingresada = 0;
    int intentos = 0;
    bool acceso_concedido = false;

    cout << "=====================================================" << endl;
    cout << "  SISTEMA DE AUTENTICACION PARA CARGA DE DATOS (C++) " << endl;
    cout << "=====================================================" << endl;
    cout << "(Clave de acceso predefinida: 2026)" << endl << endl;

    // Ciclo while para solicitar repetidamente la clave
    while (!acceso_concedido) {
        intentos++;
        cout << "Intento #" << intentos << " - Ingrese la clave numerica de acceso: ";
        cin >> clave_ingresada;

        if (clave_ingresada == CLAVE_CORRECTA) {
            acceso_concedido = true;
            cout << "\n[!] ACCESO CONCEDIDO." << endl;
            cout << "    Bienvenido al modulo de carga de datos." << endl;
        } else {
            cout << "[-] Clave incorrecta. Acceso denegado. Intente nuevamente.\n" << endl;
        }
    }

    cout << "-----------------------------------------------------" << endl;
    cout << " Resumen de inicio de sesion:" << endl;
    cout << " Numero total de intentos realizados: " << intentos << endl;
    cout << " Estado final: Autenticacion exitosa." << endl;
    cout << "=====================================================" << endl;

    return 0;
}
