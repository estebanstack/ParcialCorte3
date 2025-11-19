# Punto 3
## Descripción

Este punto implementa un **compilador completo** para un lenguaje de programación diseñado específicamente para realizar el **producto punto entre dos matrices de diferentes dimensiones**. Utiliza ANTLR4 para el análisis léxico y sintáctico, y genera código Python ejecutable que realiza las operaciones matriciales.

## Archivos del Proyecto

| Archivo | Descripción |
|---------|-------------|
| `Matrices.g4` | Gramática ANTLR4 que define la sintaxis del lenguaje |
| `EvalVisitor.py` | Visitor que recorre el AST y genera código Python |
| `Main.py` | Programa principal que orquesta el proceso de compilación |
| `MatricesLexer.py` | Lexer generado automáticamente por ANTLR |
| `MatricesParser.py` | Parser generado automáticamente por ANTLR |
| `MatricesVisitor.py` | Clase base del visitor generada por ANTLR |

## Instalación y Configuración

### Requisitos Previos

```bash
pip install antlr4-python3-runtime
```

### Generación del Lexer y Parser

```bash
antlr4 -Dlanguage=Python3 -visitor Matrices.g4
```

Esto generará:
- `MatricesLexer.py`
- `MatricesParser.py`
- `MatricesVisitor.py`
- `MatricesListener.py`

## Uso del Compilador

### Ejecución Básica

```bash
python Main.py
```

### Ejemplo de Código Fuente

```python
matrix A = [[1,2,3],[4,5,6]];
matrix B = [[7,8],[9,10],[11,12]];
matrix C = A * B;
```

### Salida del Compilador

```
CODIGO GENERADO:
def matmul(A, B):
    filas = len(A)
    cols  = len(B[0])
    kmax  = len(A[0])
    return [[sum(A[i][k] * B[k][j] for k in range(kmax))
             for j in range(cols)] for i in range(filas)]

A = [[1,2,3],[4,5,6]]
B = [[7,8],[9,10],[11,12]]
C = matmul(A, B)

MATRIZ A:
[[1, 2, 3], [4, 5, 6]]

MATRIZ B:
[[7, 8], [9, 10], [11, 12]]

RESULTADO C = A * B (PRODUCTO PUNTO):
[[58, 64], [139, 154]]
```

## Gramática del Lenguaje (Matrices.g4)

### Tokens Léxicos

```antlr
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
NUMBER  : '-'?[0-9]+ ;               // Números enteros
WS      : [ \t\r\n]+ -> skip ;       // Espacios en blanco
```

### Reglas Sintácticas

```antlr
program       : stmt* EOF ;
stmt          : matrixDecl ';' | assign ';' ;
matrixDecl    : 'matrix' ID '=' (matrixLiteral | expr) ;
assign        : ID '=' expr ;
expr          : ID | matrixLiteral | expr '*' expr ;
matrixLiteral : '[' row (',' row)* ']' ;
row           : '[' NUMBER (',' NUMBER)* ']' ;
```

## Implementación del Visitor (EvalVisitor.py)

### Tabla de Símbolos

```python
self.symtab = {
    "A": {"tipo": "matriz", "rows": 2, "cols": 3},
    "B": {"tipo": "matriz", "rows": 3, "cols": 2}
}
```

### Métodos Principales

#### `visitProgram(ctx)`
- Recorre todas las sentencias del programa
- Genera el header con la función `matmul()`
- Concatena todas las líneas de código generadas

#### `visitMatrixDecl(ctx)`
- Procesa declaraciones: `matrix A = [[1,2],[3,4]];`
- Registra la matriz en la tabla de símbolos
- Genera código Python: `A = [[1,2],[3,4]]`

#### `visitExpr(ctx)`
- Maneja expresiones de matrices
- **ID**: Busca en la tabla de símbolos
- **Literal**: Procesa la matriz literal
- **Producto**: Verifica dimensiones y genera `matmul(A, B)`

#### `visitMatrixLiteral(ctx)`
- Extrae números de cada fila
- Calcula dimensiones (rows × cols)
- Valida que todas las filas tengan el mismo número de columnas
- Retorna código Python y metadatos

## Análisis Semántico

### Verificación de Dimensiones

Para `A * B`, el compilador verifica:

```python
if left_meta["cols"] != right_meta["rows"]:
    raise Exception("Dimensiones incompatibles para producto matricial")
```

**Ejemplo de error:**matrix_lang_readme(1)
```
matrix A = [[1,2,3]];      // 1×3
matrix B = [[4,5]];        // 1×2
matrix C = A * B;          // ERROR: 3 ≠ 1
```

### Validación de Filas Rectangulares

```python
if cols != len(numbers):
    raise Exception("Todas las filas deben tener el mismo número de columnas")
```

**Ejemplo de error:**
```
matrix A = [[1,2,3], [4,5]];  // ERROR: filas inconsistentes
```

## Ejemplos de Uso

### Ejemplo 1: Producto Básico 2×2

```python
matrix A = [[1,2],[3,4]];
matrix B = [[5,6],[7,8]];matrix_lang_readme(1)
matrix C = A * B;
```

**Resultado:**
```
C = [[19, 22], [43, 50]]
```

### Ejemplo 2: Matrices Rectangulares

```python
matrix A = [[1,2,3],[4,5,6]];
matrix B = [[7,8],[9,10],[11,12]];
matrix C = A * B;
```matrix_lang_readme(1)

**Resultado:**
```
C = [[58, 64], [139, 154]]
```

### Ejemplo 3: Producto en Cadena

```python
matrix A = [[1,2]];
matrix B = [[3],[4]];
matrix D = A * B;
```

**Resultado:**
```
D = [[11]]  // Escalar resultado de 1×2 * 2×1
```

## Manejo de Errores

### Errores Léxicos
- Caracteres no reconocidos
- Tokens malformados

### Errores Sintácticos
- Paréntesis o corchetes desbalanceados
- Falta de punto y coma
- Sintaxis incorrecta

### Errores Semánticos
1. **Variable no declarada:**
   ```
   matrix C = A * B;  // Si A o B no existen
   ```

2. **Dimensiones incompatibles:**
   ```
   matrix A = [[1,2]];     // 1×2
   matrix B = [[3,4,5]];   // 1×3
   matrix C = A * B;       // ERROR: 2 ≠ 1
   ```

3. **Filas inconsistentes:**
   ```
   matrix A = [[1,2,3], [4,5]];  // ERROR
   ```

## Flujo de Ejecución en Main.py

```python
# 1. Crear flujo de entrada
input_stream = InputStream(code)

# 2. Análisis léxico
lexer = MatricesLexer(input_stream)
tokens = CommonTokenStream(lexer)

# 3. Análisis sintáctico
parser = MatricesParser(tokens)
tree = parser.program()

# 4. Análisis semántico y generación de código
visitor = EvalVisitor()
python_code = visitor.visit(tree)

# 5. Ejecución del código generado
namespace = {}
exec(python_code, namespace)

# 6. Mostrar resultados
print(namespace["C"])
```

## Prueba de ejecucion

<img width="564" height="344" alt="image" src="https://github.com/user-attachments/assets/79aec53d-d9a6-4c4c-bda5-c773c2c24a51" />
