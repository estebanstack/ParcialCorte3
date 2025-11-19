# Punto 1

Este documento describe y explica la función solicitada en el punto 1, cuyo propósito es modelar y generar formalmente la gramática CRUD de acuerdo con la teoría de lenguajes formales

Su único objetivo es construir la gramática formal G = (N, T, P, S₀)
y retornarla como una estructura de datos.

## Descripción general

La función:

generarGramaticaCRUD()

construye y retorna una gramática para un lenguaje que permite describir sentencias CRUD:

CREATE

READ

UPDATE

DELETE

Cada componente de la gramática está definido explícitamente:

N: Conjunto de No Terminales

T: Conjunto de Terminales

P: Conjunto de Producciones

S₀: Símbolo inicial

## Función completa
funcion generarGramaticaCRUD() retorna Gramatica:
```bash
    // 1. Conjunto de NO TERMINALES
    N = {
        "P",     // programa
        "S",     // sentencia
        "C",     // create
        "R",     // read
        "U",     // update
        "D",     // delete
        "CL",    // lista de columnas
        "RCL",   // resto de columnas
        "VL",    // lista de valores
        "RVL",   // resto de valores
        "FL",    // lista select para READ
        "ASG",   // lista de asignaciones
        "RASG",  // resto de asignaciones
        "W"      // sección opcional WHERE
    }


    // 2. Conjunto de TERMINALES
    T = {
        "create", "read", "update", "delete",
        "fields", "values", "set", "where",
        "(", ")", ",", "=", ";",
        "id", "value"
    }


    // 3. Conjunto de PRODUCCIONES
    P = {

        // Programa
        "P → S P | ε",

        // Sentencias CRUD
        "S → C",
        "S → R",
        "S → U",
        "S → D",

        // CREATE
        'C → create id "(" CL ")" values "(" VL ")" ";"',

        // READ
        'R → read id fields "(" FL ")" W ";"',

        // UPDATE
        'U → update id set ASG W ";"',

        // DELETE
        'D → delete id W ";"',

        // WHERE opcional
        'W → where id "=" value',
        'W → ε',

        // Listas de columnas
        "CL → id RCL",
        "RCL → , id RCL | ε",

        // Listas de valores
        "VL → value RVL",
        "RVL → , value RVL | ε",

        // Campos para SELECT
        "FL → CL",

        // Asignaciones de UPDATE
        'ASG → id "=" value RASG',
        'RASG → , id "=" value RASG | ε'
    }


    // 4. Símbolo inicial
    S0 = "P"


    // 5. Retornar la gramática completa
    retornar {
        "NoTerminales": N,
        "Terminales": T,
        "Producciones": P,
        "Inicial": S0
    }

fin funcion
```

### La funcion:
Construye formalmente la gramática de un lenguaje CRUD
No la ejecuta, simplemente la modela matemáticamente y la retorna

Porque así se define una gramática en la teoría de Lenguajes Formales:

𝐺 = (𝑁, 𝑇, 𝑃, 𝑆0)	​

La función devuelve exactamente estos elementos.

Permite:

Describir correctamente la sintaxis CRUD

Generar analizadores sintácticos

Construir intérpretes o traductores



## Conclusión

Esta función formaliza completamente la gramática de un lenguaje CRUD y la retorna como estructura de datos, es la base para análisis sintáctico, generación de código o construcción de lenguajes más complejos.
