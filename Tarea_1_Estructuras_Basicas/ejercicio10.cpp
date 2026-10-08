#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    const int N = 10;
    double mediciones[N];
    double suma = 0.0;
    double media = 0.0;
    int conteo_superiores = 0;

    cout << "=====================================================" << endl;
    cout << "  ANALISIS ESTADISTICO DE 10 MEDICIONES (C++)        " << endl;
    cout << "=====================================================" << endl;

    // Ciclo for para ingresar los valores
    for (int i = 0; i < N; i++) {
        cout << "Ingrese la medicion [" << (i + 1) << "/" << N << "]: ";
        cin >> mediciones[i];
        suma += mediciones[i];
    }

    // Calculo de la media aritmetica
    media = suma / N;

    // Determinar cuantas observaciones estan por encima de la media
    for (int i = 0; i < N; i++) {
        if (mediciones[i] > media) {
            conteo_superiores++;
        }
    }

    cout << fixed << setprecision(2);
    cout << "\n---------------- RESUMEN ESTADISTICO ----------------" << endl;
    cout << " Suma total acumulada            : " << suma << endl;
    cout << " Media aritmetica del grupo      : " << media << endl;
    cout << " Observaciones mayores a la media: " << conteo_superiores << " de " << N << endl;
    cout << "\nDetalle de observaciones y clasificacion respecto a la media:" << endl;
    for (int i = 0; i < N; i++) {
        cout << " Obs " << setw(2) << (i + 1) << ": " << setw(7) << mediciones[i];
        if (mediciones[i] > media) {
            cout << "  -> Por encima de la media (+)" << endl;
        } else if (mediciones[i] < media) {
            cout << "  -> Por debajo de la media (-)" << endl;
        } else {
            cout << "  -> Igual a la media" << endl;
        }
    }
    cout << "-----------------------------------------------------" << endl;

    return 0;
}
