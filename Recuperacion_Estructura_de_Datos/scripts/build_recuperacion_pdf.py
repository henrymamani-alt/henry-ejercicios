import os
import subprocess
import base64
import shutil
import fitz

DIR_BASE = r"C:\Users\henry\Desktop\Trabajo_Recuperacion_Estructura_de_Datos"
DIR_IMG = os.path.join(DIR_BASE, "imagenes")
DIR_COD = os.path.join(DIR_BASE, "codigo")

def img_to_b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

imgs_b64 = {i: img_to_b64(os.path.join(DIR_IMG, f"captura_ejercicio{i}.png")) for i in range(1, 6)}

exercises = [
    {
        "id": 1,
        "title": "1. Suma de números impares.",
        "enunciado": "Lea un entero positivo y muestre la suma de todos los números impares menores o iguales a él (ejemplo: 10 &rarr; 25).",
        "respuestas": [
            ("Espacio 1", "1", "Inicia en el primer número impar positivo."),
            ("Espacio 2", "i + 1", "Paso de incremento secuencial de 1 en 1."),
            ("Espacio 3", "i % 2 != 0", "Condición para verificar si el número es impar."),
            ("Espacio 4", "suma + i", "Acumula el valor impar en la suma.")
        ],
        "codigo": """#include &lt;stdio.h&gt;

int main(void) {
    int n, i, suma = 0;
    scanf("%d", &amp;n);
    for (i = <span class="hl">1</span>; i &lt;= n; i = <span class="hl">i + 1</span>) {
        if (<span class="hl">i % 2 != 0</span>) {
            suma = <span class="hl">suma + i</span>;
        }
    }
    printf("%d\\n", suma);
    return 0;
}"""
    },
    {
        "id": 2,
        "title": "2. Conteo de calles.",
        "enunciado": "Lea n códigos de dirección: 1 representa Norte-Sur y 2 representa Este-Oeste. Imprima los totales respectivos (ejemplo: 1 1 2 1 2 1 &rarr; 4 2).",
        "respuestas": [
            ("Espacio 1", "i < n", "Condición del for para leer los n códigos."),
            ("Espacio 2", "x == 1", "Verifica si el código es 1 (Norte-Sur)."),
            ("Espacio 3", "ns++", "Incrementa el contador Norte-Sur."),
            ("Espacio 4", "eo++", "Incrementa el contador Este-Oeste.")
        ],
        "codigo": """#include &lt;stdio.h&gt;

int main(void) {
    int n, x, i, ns = 0, eo = 0;
    scanf("%d", &amp;n);
    for (i = 0; <span class="hl">i &lt; n</span>; i++) {
        scanf("%d", &amp;x);
        if (<span class="hl">x == 1</span>) {
            <span class="hl">ns++</span>;
        } else if (x == 2) {
            <span class="hl">eo++</span>;
        }
    }
    printf("%d %d\\n", ns, eo);
    return 0;
}"""
    },
    {
        "id": 3,
        "title": "3. Verificación de paréntesis con una pila.",
        "enunciado": "Lea una cadena compuesta solamente por ( y ). Escriba BALANCEADO si sus paréntesis están correctamente emparejados; en caso contrario, NO BALANCEADO. Complete cuatro espacios.",
        "respuestas": [
            ("Espacio 1", "tope++", "Apila '(' en la posición tope y avanza el cursor."),
            ("Espacio 2", "tope == 0", "Detecta si la pila está vacía al intentar cerrar (error)."),
            ("Espacio 3", "tope--", "Desapila el '(' emparejado decrementando el tope."),
            ("Espacio 4", "valido && tope == 0", "Verifica que no hubo error y que la pila quedó vacía.")
        ],
        "codigo": """#include &lt;stdio.h&gt;
#include &lt;string.h&gt;

int main(void) {
    char s[1001], pila[1001];
    int i, tope = 0, valido = 1;
    scanf("%1000s", s);
    for (i = 0; s[i] != '\\0'; i++) {
        if (s[i] == '(') {
            pila[<span class="hl">tope++</span>] = '(';
        } else if (s[i] == ')') {
            if (<span class="hl">tope == 0</span>) {
                valido = 0;
                break;
            }
            <span class="hl">tope--</span>;
        }
    }
    if (<span class="hl">valido &amp;&amp; tope == 0</span>)
        puts("BALANCEADO");
    else
        puts("NO BALANCEADO");
    return 0;
}"""
    },
    {
        "id": 4,
        "title": "4. Baúl con operaciones en ambos extremos.",
        "enunciado": "Use un arreglo como doble cola (deque). Las operaciones permiten insertar y retirar elementos por ambos extremos. Considere hasta 100 operaciones y valores enteros.",
        "respuestas": [
            ("Espacio 1", "--ini", "PUSH_TOP: decrementa ini e inserta en el extremo frontal."),
            ("Espacio 2", "fin++", "PUSH_BOTTOM: inserta en el extremo posterior e incrementa fin."),
            ("Espacio 3", "ini++", "POP_TOP: elimina del extremo frontal avanzando ini."),
            ("Espacio 4", "fin--", "POP_BOTTOM: elimina del extremo posterior retrocediendo fin.")
        ],
        "codigo": """#include &lt;stdio.h&gt;
#include &lt;string.h&gt;

int main(void) {
    int a[205], ini = 100, fin = 100, n, x, i, j;
    char op[20];
    scanf("%d", &amp;n);
    for (i = 0; i &lt; n; i++) {
        scanf("%19s", op);
        if (strcmp(op, "PUSH_TOP") == 0) {
            scanf("%d", &amp;x); a[<span class="hl">--ini</span>] = x;
        } else if (strcmp(op, "PUSH_BOTTOM") == 0) {
            scanf("%d", &amp;x); a[<span class="hl">fin++</span>] = x;
        } else if (strcmp(op, "POP_TOP") == 0) {
            if (ini &lt; fin) <span class="hl">ini++</span>;
        } else if (strcmp(op, "POP_BOTTOM") == 0) {
            if (ini &lt; fin) <span class="hl">fin--</span>;
        }
    }
    if (ini == fin) puts("BAUL VACIO");
    else {
        for (j = ini; j &lt; fin; j++) printf("%d ", a[j]);
        printf("\\n");
    }
    return 0;
}"""
    },
    {
        "id": 5,
        "title": "5. Personas vetadas y recorrido inverso.",
        "enunciado": "Lea exactamente diez nombres, excluya Santiago, Pedro, Ariadna, Marco, Juan y Angel. Imprima la cantidad admitida y sus nombres desde el último hasta el primero, utilizando un arreglo como pila.",
        "respuestas": [
            ("Espacio 1", "strcmp(nombre[i], \"Angel\") != 0", "Excluye al sexto nombre vetado ('Angel')."),
            ("Espacio 2", "tope++", "Apila la persona admitida e incrementa tope."),
            ("Espacio 3", "tope", "Imprime la cantidad de personas admitidas."),
            ("Espacio 4", "--tope", "Desapila e imprime en orden inverso (LIFO).")
        ],
        "codigo": """#include &lt;stdio.h&gt;
#include &lt;string.h&gt;

int main(void) {
    char nombre[10][40], pila[10][40];
    int i, tope = 0;
    for (i = 0; i &lt; 10; i++) {
        scanf("%39s", nombre[i]);
        if (strcmp(nombre[i], "Santiago") != 0 &amp;&amp;
            strcmp(nombre[i], "Pedro") != 0 &amp;&amp;
            strcmp(nombre[i], "Ariadna") != 0 &amp;&amp;
            strcmp(nombre[i], "Marco") != 0 &amp;&amp;
            strcmp(nombre[i], "Juan") != 0 &amp;&amp;
            <span class="hl">strcmp(nombre[i], "Angel") != 0</span>) {
            strcpy(pila[<span class="hl">tope++</span>], nombre[i]);
        }
    }
    printf("%d\\n", <span class="hl">tope</span>);
    while (tope &gt; 0) {
        puts(pila[<span class="hl">--tope</span>]);
    }
    return 0;
}"""
    }
]

html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Recuperación de Estructuras de Datos - Henry Antonio Mamani Gutierrez</title>
<style>
@page {{
    size: A4 portrait;
    margin: 8mm 14mm 8mm 14mm;
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #111827;
    background: #ffffff;
    margin: 0;
    padding: 0;
    font-size: 8.8pt;
    line-height: 1.32;
}}

.page {{
    page-break-after: always;
    height: 278mm;
    max-height: 278mm;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}}

.page:last-child {{
    page-break-after: avoid;
}}

/* Encabezado */
.exam-header-top {{
    display: flex;
    justify-content: space-between;
    font-size: 8.5pt;
    font-weight: 600;
    color: #374151;
    border-bottom: 1px solid #9ca3af;
    padding-bottom: 2px;
    margin-bottom: 4px;
}}

.exam-main-title {{
    font-size: 12.5pt;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-align: center;
    color: #111827;
    margin: 3px 0 6px 0;
}}

.student-meta-box {{
    background: #f9fafb;
    border: 1px solid #d1d5db;
    border-radius: 4px;
    padding: 6px 10px;
    margin-bottom: 8px;
    font-size: 8.5pt;
    line-height: 1.45;
}}
.student-meta-row {{
    display: flex;
    justify-content: space-between;
}}

.github-link-row {{
    margin-top: 5px;
    padding-top: 4px;
    border-top: 1px dashed #cbd5e1;
    font-size: 8.5pt;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}}
.github-link-row strong {{
    color: #0f172a;
}}
.github-link-row a {{
    color: #0284c7;
    text-decoration: underline;
    font-weight: 700;
    font-family: Consolas, monospace;
    white-space: nowrap;
}}

/* Mini encabezado en paginas siguientes */
.sub-page-header {{
    display: flex;
    justify-content: space-between;
    font-size: 8pt;
    color: #6b7280;
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 2px;
    margin-bottom: 6px;
}}
.sub-page-header strong {{
    color: #111827;
}}
.sub-page-header a {{
    color: #0284c7;
    text-decoration: none;
    font-weight: 600;
}}

/* Secciones de Ejercicio */
.ex-title {{
    font-size: 9.5pt;
    font-weight: 700;
    color: #111827;
    margin: 0 0 2px 0;
}}

.ex-enunciado {{
    font-size: 8.2pt;
    color: #374151;
    margin-bottom: 5px;
    line-height: 1.3;
}}

/* Codigo con espacios completados resaltados */
.code-container {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 3px solid #0284c7;
    border-radius: 4px;
    padding: 5px 8px;
    font-family: Consolas, "Courier New", monospace;
    font-size: 7pt;
    line-height: 1.22;
    color: #0f172a;
    white-space: pre;
    margin-bottom: 5px;
}}

/* Resaltado del texto completado */
.hl {{
    background-color: #dcfce7;
    color: #15803d;
    font-weight: 800;
    border-bottom: 2px solid #22c55e;
    padding: 0 3px;
    border-radius: 2px;
}}

/* Respuestas breves */
.answers-box {{
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 4px;
    padding: 4px 8px;
    margin-bottom: 5px;
    font-size: 7.5pt;
    line-height: 1.25;
}}
.answers-box strong {{
    color: #166534;
}}
.ans-badge {{
    background: #ffffff;
    border: 1px solid #86efac;
    color: #15803d;
    font-family: Consolas, monospace;
    font-weight: 700;
    padding: 0 3px;
    border-radius: 2px;
}}

/* Captura de pantalla */
.screenshot-box {{
    text-align: center;
    margin-top: auto;
    margin-bottom: 2px;
}}
.screenshot-box img {{
    width: 100%;
    max-height: 112mm;
    object-fit: contain;
    border-radius: 5px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12);
}}

.page-footer {{
    margin-top: auto;
    display: flex;
    justify-content: space-between;
    font-size: 7.2pt;
    color: #6b7280;
    border-top: 1px solid #e5e7eb;
    padding-top: 2px;
}}
.page-footer a {{
    color: #0284c7;
    text-decoration: underline;
    font-family: Consolas, monospace;
    white-space: nowrap;
}}
</style>
</head>
<body>
"""

for idx, ex in enumerate(exercises):
    page_num = idx + 1
    
    html_doc += f'<div class="page">\n'
    
    if page_num == 1:
        # Encabezado con link en fila propia de ancho completo y nowrap
        html_doc += f"""
    <div class="exam-header-top">
        <div>FINESI &ndash; Estructuras de Datos</div>
        <div>Evaluación práctica (Recuperación)</div>
    </div>

    <div class="exam-main-title">
        RECUPERACIÓN DE ESTRUCTURAS DE DATOS
    </div>

    <div class="student-meta-box">
        <div class="student-meta-row">
            <div><strong>Apellidos y nombres:</strong> Mamani Gutierrez Henry Antonio</div>
            <div><strong>Fecha:</strong> 30/10/26</div>
        </div>
        <div class="student-meta-row" style="margin-top: 2px;">
            <div><strong>Asignatura:</strong> Estructura de Datos (2026) &mdash; Prof. Fred Torres Cruz</div>
            <div><strong>Modalidad:</strong> Trabajo de Recuperación</div>
        </div>
        <div class="github-link-row">
            <strong>Repositorio en GitHub:</strong> <a href="https://github.com/henrymamani-alt/henry-ejercicios" target="_blank">https://github.com/henrymamani-alt/henry-ejercicios</a>
        </div>
    </div>
"""
    else:
        html_doc += f"""
    <div class="sub-page-header">
        <div><strong>FINESI &ndash; Estructuras de Datos (Recuperación)</strong> | Prof. Fred Torres Cruz</div>
        <div>Mamani Gutierrez Henry Antonio | <a href="https://github.com/henrymamani-alt/henry-ejercicios" target="_blank">GitHub</a></div>
    </div>
"""

    # Titulo y enunciado
    html_doc += f"""
    <div class="ex-title">{ex["title"]}</div>
    <div class="ex-enunciado">{ex["enunciado"]}</div>

    <div class="code-container">{ex["codigo"]}</div>

    <div class="answers-box">
        <strong>Espacios completados en el código:</strong><br>
"""
    for n_esp, val_esp, desc_esp in ex["respuestas"]:
        html_doc += f'        &bull; <strong>{n_esp}:</strong> <span class="ans-badge">{val_esp}</span> &mdash; <em>{desc_esp}</em><br>\n'
    
    html_doc += f"""
    </div>

    <div class="screenshot-box">
        <img src="{imgs_b64[ex['id']]}" alt="Evidencia de ejecucion Ejercicio {ex['id']}">
    </div>

    <div class="page-footer">
        <div>Mamani Gutierrez Henry Antonio &mdash; Estructura de Datos</div>
        <div>Página {page_num} de 5</div>
        <div><a href="https://github.com/henrymamani-alt/henry-ejercicios" target="_blank">https://github.com/henrymamani-alt/henry-ejercicios</a></div>
    </div>
</div>
"""

html_doc += """
</body>
</html>
"""

html_path = os.path.join(DIR_BASE, "informe_recuperacion.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_doc)

# Compile PDF using Edge Headless
pdf_target1 = os.path.join(DIR_BASE, "Trabajo_Recuperacion_Estructuras_Datos_Henry_Mamani.pdf")
pdf_target2 = r"C:\Users\henry\Desktop\henry-ejercicios\Recuperacion_Estructura_de_Datos\Trabajo_Recuperacion_Estructuras_Datos_Henry_Mamani.pdf"
pdf_desktop = r"C:\Users\henry\Desktop\Trabajo_Recuperacion_Estructuras_Datos_Henry_Mamani.pdf"

cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_target1}",
    html_path
]

print("Compilando PDF con link corregido...")
subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(pdf_target1):
    shutil.copy(pdf_target1, pdf_target2)
    shutil.copy(pdf_target1, pdf_desktop)
    print("PDF actualizado y copiado exitosamente.")
    
    # Verify links with fitz
    doc = fitz.open(pdf_target1)
    print("Total paginas:", len(doc))
    for p_num, p in enumerate(doc):
        links = p.get_links()
        print(f"Pagina {p_num+1} links:", links)
