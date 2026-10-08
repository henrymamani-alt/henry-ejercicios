#include <iostream>
#include <stack>
#include <string>

using namespace std;

void mostrarMenu() {
    cout << "\n--- MENU DE EDITOR (FUNCION DESHACER / UNDO) ---" << endl;
    cout << " 1. Realizar nueva accion (Apilar)" << endl;
    cout << " 2. Deshacer ultima accion (Pop)" << endl;
    cout << " 3. Ver accion actual en el tope (Top)" << endl;
    cout << " 4. Ver cantidad de acciones registradas" << endl;
    cout << " 5. Salir del editor" << endl;
    cout << "Seleccione una opcion: ";
}

int main() {
    stack<string> historial;
    int opcion;

    cout << "=====================================================" << endl;
    cout << "    EJERCICIO 4: HISTORIAL DE ACCIONES - DESHACER    " << endl;
    cout << "=====================================================" << endl;

    do {
        mostrarMenu();
        if (!(cin >> opcion)) break;

        switch (opcion) {
            case 1: {
                string accion;
                cout << "Ingrese la descripcion de la accion realizada: ";
                getline(cin >> ws, accion);
                historial.push(accion);
                cout << "[+] Accion '" << accion << "' registrada en el historial." << endl;
                break;
            }
            case 2: {
                if (historial.empty()) {
                    cout << "[-] No hay acciones para deshacer. El historial esta vacio." << endl;
                } else {
                    string accionDeshecha = historial.top();
                    historial.pop();
                    cout << "[<-- DESHACER] Se ha revertido la accion: '" << accionDeshecha << "'." << endl;
                }
                break;
            }
            case 3: {
                if (historial.empty()) {
                    cout << "[i] No hay acciones en el tope. Historial vacio." << endl;
                } else {
                    cout << "[TOPE ACTUAL] Ultima accion registrada: '" << historial.top() << "'." << endl;
                }
                break;
            }
            case 4: {
                cout << "[TOTAL] Acciones actualmente en historial: " << historial.size() << endl;
                break;
            }
            case 5: {
                cout << "Saliendo del simulador de editor..." << endl;
                break;
            }
            default:
                cout << "Opcion no valida. Intente de nuevo." << endl;
        }
    } while (opcion != 5);

    return 0;
}
