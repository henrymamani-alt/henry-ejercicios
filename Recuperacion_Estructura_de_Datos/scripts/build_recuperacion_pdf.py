import os
import subprocess
import base64
import shutil

DIR_BASE = r"C:\Users\henry\Desktop\Trabajo_Recuperacion_Estructura_de_Datos"
DIR_IMG = os.path.join(DIR_BASE, "imagenes")
DIR_COD = os.path.join(DIR_BASE, "codigo")

def img_to_b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

logo_unap_b64 = img_to_b64(os.path.join(DIR_IMG, "logo-una-puno.png"))
logo_finesi_b64 = img_to_b64(os.path.join(DIR_IMG, "logofinesi.png"))

imgs_b64 = {i: img_to_b64(os.path.join(DIR_IMG, f"captura_ejercicio{i}.png")) for i in range(1, 6)}

# Exercise data with statements, analysis, completions table, and highlighted code
exercises = [
    {
        "id": 1,
        "title": "Ejercicio 1: Suma de números impares",
        "enunciado": "Lea un entero positivo y muestre la suma de todos los números impares menores o iguales a él (ejemplo: <code>10 &rarr; 25</code>).",
        "analisis": "El problema modela una suma aritmética sobre la subsecuencia de enteros congruentes con <code>1 (mod 2)</code> en el intervalo discreto <code>[1, n]</code>. Para garantizar un comportamiento determinista, el bucle inicia en el primer número impar positivo (<code>i = 1</code>) y se incrementa paso a paso (<code>i = i + 1</code>). Dentro del cuerpo iterativo, la cláusula condicional <code>i % 2 != 0</code> evalúa el residuo de la división euclidiana por 2; al cumplirse la imparidad, el acumulador actualiza su estado mediante <code>suma = suma + i</code>. La complejidad temporal resultante es estrictamente lineal <i>O(n)</i> y el consumo de memoria es constante <i>O(1)</i>.",
        "completados": [
            ("Espacio 1: Inicialización del bucle", "1", "Inicializa la variable de control 'i' en 1 (primer entero impar positivo)."),
            ("Espacio 2: Paso de incremento", "i + 1", "Avanza la variable 'i' de unidad en unidad para recorrer exhaustivamente cada entero hasta 'n'."),
            ("Espacio 3: Condición de imparidad", "i % 2 != 0", "Verifica si el residuo de dividir 'i' entre 2 es distinto de cero (número impar)."),
            ("Espacio 4: Acumulador de suma", "suma + i", "Suma algebraicamente el impar actual a la variable acumuladora 'suma'.")
        ],
        "codigo_html": """<span class="kw">#include</span> <span class="str">&lt;stdio.h&gt;</span>

<span class="kw">int</span> <span class="fn">main</span>(<span class="kw">void</span>) {
    <span class="kw">int</span> n, i, suma = <span class="num">0</span>;
    <span class="fn">scanf</span>(<span class="str">"%d"</span>, &amp;n);
    <span class="kw">for</span> (i = <span class="hl">1</span>; i &lt;= n; i = <span class="hl">i + 1</span>) {
        <span class="kw">if</span> (<span class="hl">i % 2 != 0</span>) {
            suma = <span class="hl">suma + i</span>;
        }
    }
    <span class="fn">printf</span>(<span class="str">"%d\\n"</span>, suma);
    <span class="kw">return</span> <span class="num">0</span>;
}"""
    },
    {
        "id": 2,
        "title": "Ejercicio 2: Conteo de calles",
        "enunciado": "Lea n códigos de dirección: 1 representa Norte-Sur y 2 representa Este-Oeste. Imprima los totales respectivos (ejemplo: <code>1 1 2 1 2 1 &rarr; 4 2</code>).",
        "analisis": "Se requiere clasificar y contabilizar un flujo secuencial de <code>n</code> señales discretas binarias. Se emplea un bucle acotado indexado en cero (<code>for (i = 0; i &lt; n; i++)</code>) que invoca <code>scanf</code> en cada ciclo. Mediante bifurcación condicional se evalúa el código: si <code>x == 1</code>, se incrementa el contador de calles axiales Norte-Sur (<code>ns++</code>); en caso alternativo (<code>else if (x == 2)</code>), se incrementa el contador Este-Oeste (<code>eo++</code>). El algoritmo opera en tiempo lineal <i>O(n)</i> y espacio auxiliar <i>O(1)</i>.",
        "completados": [
            ("Espacio 1: Límite del for", "i < n", "Condición de permanencia que garantiza la lectura exacta de los 'n' registros."),
            ("Espacio 2: Condición Norte-Sur", "x == 1", "Discrimina el valor numérico 1 asociado al eje geográfico Norte-Sur."),
            ("Espacio 3: Incremento Norte-Sur", "ns++", "Incrementa en uno el acumulador de calles con orientación Norte-Sur."),
            ("Espacio 4: Incremento Este-Oeste", "eo++", "Incrementa en uno el acumulador de calles con orientación Este-Oeste.")
        ],
        "codigo_html": """<span class="kw">#include</span> <span class="str">&lt;stdio.h&gt;</span>

<span class="kw">int</span> <span class="fn">main</span>(<span class="kw">void</span>) {
    <span class="kw">int</span> n, x, i, ns = <span class="num">0</span>, eo = <span class="num">0</span>;
    <span class="fn">scanf</span>(<span class="str">"%d"</span>, &amp;n);
    <span class="kw">for</span> (i = <span class="num">0</span>; <span class="hl">i &lt; n</span>; i++) {
        <span class="fn">scanf</span>(<span class="str">"%d"</span>, &amp;x);
        <span class="kw">if</span> (<span class="hl">x == 1</span>) {
            <span class="hl">ns++</span>;
        } <span class="kw">else if</span> (x == <span class="num">2</span>) {
            <span class="hl">eo++</span>;
        }
    }
    <span class="fn">printf</span>(<span class="str">"%d %d\\n"</span>, ns, eo);
    <span class="kw">return</span> <span class="num">0</span>;
}"""
    },
    {
        "id": 3,
        "title": "Ejercicio 3: Verificación de paréntesis con una pila",
        "enunciado": "Lea una cadena compuesta solamente por <code>(</code> y <code>)</code>. Escriba <code>BALANCEADO</code> si sus paréntesis están correctamente emparejados; en caso contrario, <code>NO BALANCEADO</code>. Complete cuatro espacios.",
        "analisis": "El emparejamiento de símbolos anidados es el problema canónico de los autómata de pila (PDA). Al iterar sobre la cadena, cada apertura <code>(</code> se inserta en el tope del arreglo mediante postincremento (<code>pila[tope++] = '('</code>). Al encontrar un cierre <code>)</code>, se comprueba primero que la pila no esté vacía (<code>if (tope == 0)</code>); de estarlo, existe un cierre prematuro y se aborta (<code>valido = 0; break;</code>). Si hay elementos, se desapila con <code>tope--</code>. La invariante de balanceo exige que no existan aperturas pendientes al concluir (<code>valido && tope == 0</code>).",
        "completados": [
            ("Espacio 1: Apilar apertura (Push)", "tope++", "Guarda '(' en la posición actual de la pila y avanza el cursor 'tope'."),
            ("Espacio 2: Detección de underflow", "tope == 0", "Detecta un paréntesis de cierre sin apertura previa disponible."),
            ("Espacio 3: Desapilar (Pop)", "tope--", "Retira el paréntesis de apertura emparejado decrementando 'tope'."),
            ("Espacio 4: Validez final", "valido && tope == 0", "Verifica que el análisis no haya fallado y que la pila quede totalmente vacía.")
        ],
        "codigo_html": """<span class="kw">#include</span> <span class="str">&lt;stdio.h&gt;</span>
<span class="kw">#include</span> <span class="str">&lt;string.h&gt;</span>

<span class="kw">int</span> <span class="fn">main</span>(<span class="kw">void</span>) {
    <span class="kw">char</span> s[<span class="num">1001</span>], pila[<span class="num">1001</span>];
    <span class="kw">int</span> i, tope = <span class="num">0</span>, valido = <span class="num">1</span>;
    <span class="fn">scanf</span>(<span class="str">"%1000s"</span>, s);
    <span class="kw">for</span> (i = <span class="num">0</span>; s[i] != <span class="str">'\\0'</span>; i++) {
        <span class="kw">if</span> (s[i] == <span class="str">'('</span>) {
            pila[<span class="hl">tope++</span>] = <span class="str">'('</span>;
        } <span class="kw">else if</span> (s[i] == <span class="str">')'</span>) {
            <span class="kw">if</span> (<span class="hl">tope == 0</span>) {
                valido = <span class="num">0</span>;
                <span class="kw">break</span>;
            }
            <span class="hl">tope--</span>;
        }
    }
    <span class="kw">if</span> (<span class="hl">valido &amp;&amp; tope == 0</span>)
        <span class="fn">puts</span>(<span class="str">"BALANCEADO"</span>);
    <span class="kw">else</span>
        <span class="fn">puts</span>(<span class="str">"NO BALANCEADO"</span>);
    <span class="kw">return</span> <span class="num">0</span>;
}"""
    },
    {
        "id": 4,
        "title": "Ejercicio 4: Baúl con operaciones en ambos extremos",
        "enunciado": "Use un arreglo como doble cola (deque). Las operaciones permiten insertar y retirar elementos por ambos extremos. Considere hasta 100 operaciones y valores enteros.",
        "analisis": "La doble cola (deque) permite inserción y supresión en <i>O(1)</i> en ambos extremos. El arreglo <code>a[205]</code> se centra asignando <code>ini = 100</code> y <code>fin = 100</code>. El rango semiabierto <code>[ini, fin)</code> almacena los datos activos. La operación <code>PUSH_TOP</code> expande el deque hacia la izquierda mediante pre-decremento (<code>a[--ini] = x</code>); <code>PUSH_BOTTOM</code> expande hacia la derecha mediante post-incremento (<code>a[fin++] = x</code>). Análogamente, <code>POP_TOP</code> contrae la frontera izquierda (<code>ini++</code>) y <code>POP_BOTTOM</code> contrae la derecha (<code>fin--</code>).",
        "completados": [
            ("Espacio 1: Inserción en Tope / Frente", "--ini", "Decrementa 'ini' para asignar la nueva posición libre en el extremo izquierdo a[--ini]."),
            ("Espacio 2: Inserción en Fondo / Cola", "fin++", "Inserta en el índice actual 'fin' y lo incrementa a la siguiente posición a[fin++]."),
            ("Espacio 3: Retiro de Tope / Frente", "ini++", "Avanza el índice 'ini' eliminando lógicamente el elemento superior en tiempo O(1)."),
            ("Espacio 4: Retiro de Fondo / Cola", "fin--", "Retrocede el índice 'fin' eliminando lógicamente el elemento del fondo en tiempo O(1).")
        ],
        "codigo_html": """<span class="kw">#include</span> <span class="str">&lt;stdio.h&gt;</span>
<span class="kw">#include</span> <span class="str">&lt;string.h&gt;</span>

<span class="kw">int</span> <span class="fn">main</span>(<span class="kw">void</span>) {
    <span class="kw">int</span> a[<span class="num">205</span>], ini = <span class="num">100</span>, fin = <span class="num">100</span>, n, x, i, j;
    <span class="kw">char</span> op[<span class="num">20</span>];
    <span class="fn">scanf</span>(<span class="str">"%d"</span>, &amp;n);
    <span class="kw">for</span> (i = <span class="num">0</span>; i &lt; n; i++) {
        <span class="fn">scanf</span>(<span class="str">"%19s"</span>, op);
        <span class="kw">if</span> (<span class="fn">strcmp</span>(op, <span class="str">"PUSH_TOP"</span>) == <span class="num">0</span>) {
            <span class="fn">scanf</span>(<span class="str">"%d"</span>, &amp;x); a[<span class="hl">--ini</span>] = x;
        } <span class="kw">else if</span> (<span class="fn">strcmp</span>(op, <span class="str">"PUSH_BOTTOM"</span>) == <span class="num">0</span>) {
            <span class="fn">scanf</span>(<span class="str">"%d"</span>, &amp;x); a[<span class="hl">fin++</span>] = x;
        } <span class="kw">else if</span> (<span class="fn">strcmp</span>(op, <span class="str">"POP_TOP"</span>) == <span class="num">0</span>) {
            <span class="kw">if</span> (ini &lt; fin) <span class="hl">ini++</span>;
        } <span class="kw">else if</span> (<span class="fn">strcmp</span>(op, <span class="str">"POP_BOTTOM"</span>) == <span class="num">0</span>) {
            <span class="kw">if</span> (ini &lt; fin) <span class="hl">fin--</span>;
        }
    }
    <span class="kw">if</span> (ini == fin) <span class="fn">puts</span>(<span class="str">"BAUL VACIO"</span>);
    <span class="kw">else</span> {
        <span class="kw">for</span> (j = ini; j &lt; fin; j++) <span class="fn">printf</span>(<span class="str">"%d "</span>, a[j]);
        <span class="fn">printf</span>(<span class="str">"\\n"</span>);
    }
    <span class="kw">return</span> <span class="num">0</span>;
}"""
    },
    {
        "id": 5,
        "title": "Ejercicio 5: Personas vetadas y recorrido inverso",
        "enunciado": "Lea exactamente diez nombres, excluya Santiago, Pedro, Ariadna, Marco, Juan y Angel. Imprima la cantidad admitida y sus nombres desde el último hasta el primero, utilizando un arreglo como pila.",
        "analisis": "El problema exige un filtro de exclusión compuesto por conjunciones booleanas sobre cadenas (<code>strcmp(...) != 0</code>). Al detectar un nombre apto, se empareja mediante copia en memoria (<code>strcpy(pila[tope++], nombre[i])</code>). Posteriormente, se exhibe la cardinalidad del conjunto de aceptados (<code>printf(\"%d\\n\", tope)</code>). Finalmente, un bucle <code>while (tope &gt; 0)</code> extrae en orden reverso los nombres empleando el operador de pre-decremento <code>puts(pila[--tope])</code>, logrando la inversión cronológica propia de la política LIFO.",
        "completados": [
            ("Espacio 1: Sexto nombre vetado", "strcmp(nombre[i], \"Angel\") != 0", "Verifica que el nombre ingresado no sea 'Angel', completando la lista de exclusión."),
            ("Espacio 2: Apilado de admitido", "tope++", "Inserta la cadena admitida en el tope e incrementa el contador de elementos apilados."),
            ("Espacio 3: Total de admitidos", "tope", "Muestra por consola la cantidad final de personas que superaron los filtros de exclusión."),
            ("Espacio 4: Desapilado e impresión", "--tope", "Pre-decrementa el cursor para recuperar e imprimir los nombres desde el último al primero.")
        ],
        "codigo_html": """<span class="kw">#include</span> <span class="str">&lt;stdio.h&gt;</span>
<span class="kw">#include</span> <span class="str">&lt;string.h&gt;</span>

<span class="kw">int</span> <span class="fn">main</span>(<span class="kw">void</span>) {
    <span class="kw">char</span> nombre[<span class="num">10</span>][<span class="num">40</span>], pila[<span class="num">10</span>][<span class="num">40</span>];
    <span class="kw">int</span> i, tope = <span class="num">0</span>;
    <span class="kw">for</span> (i = <span class="num">0</span>; i &lt; <span class="num">10</span>; i++) {
        <span class="fn">scanf</span>(<span class="str">"%39s"</span>, nombre[i]);
        <span class="kw">if</span> (<span class="fn">strcmp</span>(nombre[i], <span class="str">"Santiago"</span>) != <span class="num">0</span> &amp;&amp;
            <span class="fn">strcmp</span>(nombre[i], <span class="str">"Pedro"</span>) != <span class="num">0</span> &amp;&amp;
            <span class="fn">strcmp</span>(nombre[i], <span class="str">"Ariadna"</span>) != <span class="num">0</span> &amp;&amp;
            <span class="fn">strcmp</span>(nombre[i], <span class="str">"Marco"</span>) != <span class="num">0</span> &amp;&amp;
            <span class="fn">strcmp</span>(nombre[i], <span class="str">"Juan"</span>) != <span class="num">0</span> &amp;&amp;
            <span class="hl">strcmp(nombre[i], "Angel") != 0</span>) {
            <span class="fn">strcpy</span>(pila[<span class="hl">tope++</span>], nombre[i]);
        }
    }
    <span class="fn">printf</span>(<span class="str">"%d\\n"</span>, <span class="hl">tope</span>);
    <span class="kw">while</span> (tope &gt; <span class="num">0</span>) {
        <span class="fn">puts</span>(pila[<span class="hl">--tope</span>]);
    }
    <span class="kw">return</span> <span class="num">0</span>;
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
    margin: 10mm 14mm 10mm 14mm;
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1e293b;
    background: #ffffff;
    margin: 0;
    padding: 0;
    font-size: 9pt;
    line-height: 1.35;
}}

.page {{
    page-break-after: always;
    height: 275mm;
    max-height: 275mm;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}}

.page:last-child {{
    page-break-after: avoid;
}}

.page-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #003366;
    padding-bottom: 3px;
    margin-bottom: 8px;
    font-size: 8pt;
    color: #475569;
}}
.page-header strong {{
    color: #003366;
}}

.page-footer {{
    margin-top: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #cbd5e1;
    padding-top: 3px;
    font-size: 7.5pt;
    color: #64748b;
}}

/* Caratula */
.cover-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}}
.cover-title {{
    text-align: center;
    flex: 1;
    margin: 0 12px;
}}
.cover-title h1 {{
    margin: 0 0 3px 0;
    font-size: 12.5pt;
    color: #003366;
    font-weight: 800;
}}
.cover-title h2 {{
    margin: 0 0 2px 0;
    font-size: 10pt;
    color: #1e293b;
    font-weight: 700;
}}
.cover-title h3 {{
    margin: 0;
    font-size: 8.5pt;
    color: #64748b;
    font-weight: 600;
}}

.banner-line {{
    height: 3px;
    background: #003366;
    margin: 8px 0 14px 0;
    border-radius: 2px;
}}

.meta-card {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 5px solid #003366;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 16px;
    font-size: 9pt;
    line-height: 1.55;
}}
.meta-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px 14px;
}}

.doc-main-title {{
    font-size: 15pt;
    font-weight: 800;
    color: #003366;
    text-align: center;
    margin: 16px 0 10px 0;
    letter-spacing: 0.5px;
}}

.doc-subtitle {{
    font-size: 11pt;
    font-weight: 700;
    color: #0284c7;
    text-align: center;
    margin-bottom: 16px;
}}

.intro-text {{
    text-align: justify;
    line-height: 1.55;
    font-size: 9.5pt;
    margin-bottom: 15px;
}}

.highlight-box {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 14px;
    font-size: 9pt;
    line-height: 1.5;
}}

/* Ejercicio: Titulo y Enunciado */
.ex-title-box {{
    background: #003366;
    color: #ffffff;
    font-size: 10.5pt;
    font-weight: 700;
    padding: 5px 10px;
    border-radius: 4px;
    margin-bottom: 5px;
}}

.enunciado-card {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #0284c7;
    border-radius: 4px;
    padding: 5px 9px;
    font-size: 8.5pt;
    margin-bottom: 4px;
    line-height: 1.35;
}}

.section-label {{
    font-weight: 700;
    color: #003366;
    font-size: 8.5pt;
    margin: 4px 0 2px 0;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}}

.analisis-box {{
    font-size: 8.2pt;
    text-align: justify;
    line-height: 1.32;
    margin-bottom: 4px;
    color: #334155;
}}

/* Tabla de Respuestas / Completados */
.completados-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 5px;
    font-size: 7.8pt;
}}
.completados-table th {{
    background: #e2e8f0;
    color: #0f172a;
    text-align: left;
    padding: 3px 6px;
    border: 1px solid #cbd5e1;
    font-weight: 700;
}}
.completados-table td {{
    padding: 3px 6px;
    border: 1px solid #cbd5e1;
    vertical-align: middle;
}}
.badge-code {{
    background: #dcfce7;
    color: #166534;
    font-family: Consolas, monospace;
    font-weight: 700;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #86efac;
}}

/* Bloque de Codigo con Resaltado */
.code-box {{
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 4px;
    padding: 6px 10px;
    font-family: Consolas, "JetBrains Mono", monospace;
    font-size: 7pt;
    line-height: 1.25;
    color: #e2e8f0;
    white-space: pre;
    overflow: hidden;
    margin-bottom: 4px;
}}
.kw {{ color: #f43f5e; font-weight: bold; }}
.fn {{ color: #38bdf8; }}
.str {{ color: #fde047; }}
.num {{ color: #a78bfa; }}
.hl {{
    background: #166534;
    color: #f0fdf4;
    font-weight: 800;
    padding: 1px 4px;
    border-radius: 3px;
    box-shadow: 0 0 4px rgba(74, 222, 128, 0.4);
}}

/* Evidencia de Consola */
.evidence-title-box {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 5px solid #0284c7;
    padding: 8px 14px;
    border-radius: 5px;
    font-size: 11pt;
    font-weight: 700;
    color: #003366;
    margin-bottom: 12px;
}}

.evidence-wrapper {{
    text-align: center;
    margin: 8px 0;
}}
.evidence-wrapper img {{
    width: 100%;
    max-width: 100%;
    border-radius: 6px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.14);
}}

.evidence-caption {{
    margin-top: 8px;
    font-size: 8.5pt;
    color: #64748b;
    font-style: italic;
}}
</style>
</head>
<body>
"""

# Page 1: Caratula
html_doc += f"""
<div class="page">
    <div class="cover-header">
        <img src="{logo_unap_b64}" style="height: 72px;" alt="UNA Puno">
        <div class="cover-title">
            <h1>UNIVERSIDAD NACIONAL DEL ALTIPLANO DE PUNO</h1>
            <h2>FACULTAD DE INGENIERÍA ESTADÍSTICA E INFORMÁTICA</h2>
            <h3>ESCUELA PROFESIONAL DE INGENIERÍA ESTADÍSTICA E INFORMÁTICA</h3>
        </div>
        <img src="{logo_finesi_b64}" style="height: 72px;" alt="FINESI">
    </div>

    <div class="banner-line"></div>

    <div class="meta-card">
        <div class="meta-grid">
            <div><strong>Asignatura:</strong> Estructura de Datos (2026)</div>
            <div><strong>Docente:</strong> Prof. Fred Torres Cruz</div>
            <div><strong>Estudiante:</strong> Henry Antonio Mamani Gutierrez</div>
            <div><strong>Semestre / Ciclo:</strong> III Semestre</div>
            <div><strong>Fecha de Evaluación:</strong> 30 de Octubre de 2026</div>
            <div><strong>Correo Institucional:</strong> henrymamani@est.unap.edu.pe</div>
            <div style="grid-column: span 2;"><strong>Modalidad:</strong> Evaluación Práctica Presencial &mdash; Trabajo de Recuperación</div>
        </div>
    </div>

    <div class="doc-main-title">
        RECUPERACIÓN DE ESTRUCTURAS DE DATOS
    </div>
    <div class="doc-subtitle">
        RESOLUCIÓN FORMAL Y COMPLETACIÓN DE ESPACIOS DE CÓDIGO
    </div>

    <div class="intro-text">
        <p><strong>Presentación del Trabajo de Recuperación:</strong></p>
        <p>El presente documento técnico e informe académico contiene el desarrollo exhaustivo y la resolución integral de los cinco (5) problemas planteados en la prueba práctica de <strong>Recuperación de Estructuras de Datos</strong> aplicada por la <strong>Facultad de Ingeniería Estadística e Informática (FINESI)</strong>.</p>
        <p>Cada ejercicio ha sido resuelto rigurosamente según las especificaciones del docente, completando los espacios en blanco requeridos en el lenguaje de programación C estándar (C11). Asimismo, se incluye la fundamentación matemática y algorítmica de cada instrucción, el análisis de complejidad temporal y espacial, y la evidencia gráfica en alta definición de la compilación y ejecución interactiva mediante <strong>Visual Studio Code en entorno Windows 11</strong>.</p>
    </div>

    <div class="highlight-box">
        <strong>Pautas de Presentación y Convención de Resaltado:</strong>
        <ul style="margin: 4px 0; padding-left: 18px;">
            <li><strong>Código completado resaltado:</strong> Cada fragmento que correspondía a un espacio en blanco (<code>_______</code>) en la evaluación práctica original se encuentra resaltado visualmente en <span class="badge-code">verde esmeralda brillante</span> tanto en la tabla de respuestas como en el código fuente para una rápida verificación docente.</li>
            <li><strong>Pruebas y trazabilidad:</strong> Se verificaron casos de prueba habituales y casos de borde (cadenas vacías, desbordes, números negativos y filtros de texto).</li>
        </ul>
    </div>

    <div style="margin-top: auto; text-align: center; color: #94a3b8; font-size: 8.5pt; padding-bottom: 6px;">
        Facultad de Ingeniería Estadística e Informática &mdash; UNA Puno<br>
        Puno, Perú &mdash; 2026
    </div>

    <div class="page-footer">
        <div>Henry Antonio Mamani Gutierrez</div>
        <div>Página 1 de 11</div>
        <div>henrymamani@est.unap.edu.pe</div>
    </div>
</div>
"""

# Pages 2 to 11 (5 exercises * 2 pages each)
page_num = 2
for ex in exercises:
    eid = ex["id"]
    
    # Rows for completions table
    rows_table = ""
    for num_esp, cod_val, justif in ex["completados"]:
        rows_table += f"""
        <tr>
            <td style="width: 25%; font-weight: 600;">{num_esp}</td>
            <td style="width: 28%; text-align: center;"><span class="badge-code">{cod_val}</span></td>
            <td style="width: 47%;">{justif}</td>
        </tr>
        """

    # Pagina A: Enunciado, Analisis, Tabla de Completado, Codigo con Resaltado
    html_doc += f"""
<div class="page">
    <div class="page-header">
        <div><strong>Recuperación de Estructura de Datos (2026)</strong> &mdash; FINESI / UNA PUNO</div>
        <div>Prof. Fred Torres Cruz</div>
    </div>

    <div class="ex-title-box">
        {ex["title"]}
    </div>

    <div class="enunciado-card">
        <strong>Enunciado Oficial:</strong> {ex["enunciado"]}
    </div>

    <div class="section-label">Análisis y Fundamentación Algorítmica:</div>
    <div class="analisis-box">
        {ex["analisis"]}
    </div>

    <div class="section-label">Tabla de Respuestas &mdash; Espacios Completados:</div>
    <table class="completados-table">
        <thead>
            <tr>
                <th>Espacio Evaluado</th>
                <th style="text-align: center;">Código Completado (Resaltado)</th>
                <th>Justificación Técnica / Algorítmica</th>
            </tr>
        </thead>
        <tbody>
            {rows_table}
        </tbody>
    </table>

    <div class="section-label">Código Fuente en C (<code>ejercicio{eid}.c</code>) con Espacios Resaltados:</div>
    <div class="code-box">{ex["codigo_html"]}</div>

    <div class="page-footer">
        <div>Henry Antonio Mamani Gutierrez</div>
        <div>Página {page_num} de 11</div>
        <div>henrymamani@est.unap.edu.pe</div>
    </div>
</div>
"""
    page_num += 1

    # Pagina B: Evidencia Grafica en Consola
    html_doc += f"""
<div class="page">
    <div class="page-header">
        <div><strong>Recuperación de Estructura de Datos (2026)</strong> &mdash; FINESI / UNA PUNO</div>
        <div>Prof. Fred Torres Cruz</div>
    </div>

    <div class="evidence-title-box">
        Evidencia de Compilación y Ejecución en Consola &mdash; {ex["title"]}
    </div>

    <div class="evidence-wrapper">
        <img src="{imgs_b64[eid]}" alt="Evidencia Ejercicio {eid}">
        <div class="evidence-caption">
            Terminal integrada de Visual Studio Code (PowerShell en Windows 11). Compilador GCC con estándar C11.
        </div>
    </div>

    <div class="page-footer">
        <div>Henry Antonio Mamani Gutierrez</div>
        <div>Página {page_num} de 11</div>
        <div>henrymamani@est.unap.edu.pe</div>
    </div>
</div>
"""
    page_num += 1

html_doc += """
</body>
</html>
"""

html_path = os.path.join(DIR_BASE, "informe_recuperacion.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_doc)
print(f"HTML generado en {html_path}")

# Compile PDF using Edge Headless
pdf_target = os.path.join(DIR_BASE, "Trabajo_Recuperacion_Estructuras_Datos_Henry_Mamani.pdf")
pdf_desktop = r"C:\Users\henry\Desktop\Trabajo_Recuperacion_Estructuras_Datos_Henry_Mamani.pdf"

cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_target}",
    html_path
]

print("Compilando PDF con Edge headless...")
res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_target) and os.path.getsize(pdf_target) > 10000:
    shutil.copy(pdf_target, pdf_desktop)
    print(f"PDF generado exitosamente en:\n1. {pdf_target}\n2. {pdf_desktop}")
    print("Tamanio del archivo:", os.path.getsize(pdf_desktop), "bytes")
else:
    print("Error generando PDF:", res.stderr)
