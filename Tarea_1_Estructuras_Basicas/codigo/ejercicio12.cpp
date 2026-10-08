#include <iostream>
#include <vector>

using namespace std;

int main() {
    const int MAX_MEDICIONES = 10;
    int validos = 0;
    double valor;
    vector<double> lista_validos;

    cout << "=====================================================" << endl;
    cout << "  PROCESAMIENTO DE MEDICIONES CON CONTINUE Y BREAK   " << endl;
    cout << "=====================================================" << endl;
    cout << "Instrucciones: Se esperan hasta 10 mediciones.\n"
         << "- Valores negativos: Se omiten con continue.\n"
         << "- Valor 999        : Finaliza la captura con break.\n" << endl;

    for (int i = 1; i <= MAX_MEDICIONES; i++) {
        cout << "Entrada " << i << " de " << MAX_MEDICIONES << " - Ingrese medicion: ";
        cin >> valor;

        // Finalizacion inmediata si se introduce 999 mediante break
        if (valor == 999) {
            cout << ">> [BREAK] Se introdujo el codigo de parada 999. Finalizando proceso..." << endl;
            break;
        }

        // Omitir valores negativos considerandolos invalidos mediante continue
        if (valor < 0) {
            cout << ">> [CONTINUE] Medicion negativa (" << valor << ") invalida. Se omite." << endl;
            continue;
        }

        // Si es valido, se contabiliza y almacena
        validos++;
        lista_validos.push_back(valor);
        cout << "   -> Medicion " << valor << " registrada correctamente como valida." << endl;
    }

    cout << "\n---------------- RESUMEN FINAL DEL PROCESAMIENTO ----" << endl;
    cout << " Total de valores validos procesados: " << validos << endl;
    cout << " Valores validos registrados: ";
    if (validos == 0) {
        cout << "Ninguno";
    } else {
        for (size_t j = 0; j < lista_validos.size(); j++) {
            cout << lista_validos[j] << (j + 1 < lista_validos.size() ? ", " : "");
        }
    }
    cout << "\n-----------------------------------------------------" << endl;

    return 0;
}
