# Lenguaje de Multiplicación de Matrices

## Descripción

Este proyecto implementa un compilador para un lenguaje de programación diseñado específicamente para realizar el **producto punto entre dos matrices de diferentes dimensiones**. El lenguaje permite declarar matrices literales y calcular automáticamente su multiplicación, generando código Python equivalente.

## Características Principales

- **Declaración de matrices literales**: Sintaxis intuitiva con corchetes anidados
- **Producto matricial**: Operador `*` para multiplicar matrices
- **Verificación de dimensiones**: Comprobación automática de compatibilidad (columnas de A = filas de B)
- **Generación de código Python**: Traduce el código fuente a Python ejecutable
- **Tabla de símbolos**: Rastrea variables con sus dimensiones

## Gramática Traducida Dirigida por la Sintaxis

La gramática utiliza **atributos sintetizados** para:
- Calcular dimensiones de matrices (`filas`, `cols`)
- Generar código Python (`trad`)
- Verificar compatibilidad de dimensiones en operaciones

### Estructura de la Gramática

```
P → ST                    (Programa principal)
ST → D ST | ε            (Secuencia de declaraciones)
D → matrix id = M ;      (Declaración con literal)
D → matrix id = E ;      (Declaración con expresión)
E → id | M | E * E       (Expresiones: variables, literales, productos)
M → [ RLS ]              (Matriz literal)
R → [ NL ]               (Fila de la matriz)
```

## Sintaxis del Lenguaje

### Declaración de Matrices

```
matrix A = [[1,2,3], [4,5,6]];
matrix B = [[7,8], [9,10], [11,12]];
```

### Producto Matricial

```
matrix C = A * B;
```

## Ejemplo Completo

### Código de Entrada

```
matrix A = [[1,2], [3,4]];
matrix B = [[5,6], [7,8]];
matrix C = A * B;
```

### Código Python Generado

```python
def matmul(A,B):
    filas = len(A)
    cols  = len(B[0])
    kmax  = len(A[0])
    return [[sum(A[i][k]*B[k][j] for k in range(kmax))
             for j in range(cols)] for i in range(filas)]

A = [[1,2], [3,4]]
B = [[5,6], [7,8]]
C = matmul(A, B)
```

### Resultado de la Ejecución

```
C = [[19, 22], [43, 50]]
```

## Reglas Semánticas

### Verificación de Dimensiones

Para el producto `A * B`:
- ✅ **Válido**: `cols(A) == filas(B)`
- ❌ **Error**: Si las dimensiones son incompatibles

Ejemplo:
```
matrix A = [[1,2,3]];      // 1×3
matrix B = [[4], [5]];     // 2×1
matrix C = A * B;          // ERROR: 3 ≠ 2
```

### Cálculo de Dimensiones Resultantes

Cuando `A` es de dimensión `m×n` y `B` es de dimensión `n×p`:
- La matriz resultado `C = A * B` tendrá dimensión `m×p`

## Atributos de la Gramática

| No Terminal | Atributos | Descripción |
|-------------|-----------|-------------|
| **P** | `trad` | Código Python completo generado |
| **E** | `tipo`, `filas`, `cols`, `trad` | Expresión de matriz con sus dimensiones |
| **M** | `tipo`, `filas`, `cols`, `trad` | Literal de matriz |
| **RLS** | `filas`, `cols`, `trad` | Lista de filas de una matriz |
| **R** | `filas`, `cols`, `trad` | Una fila individual |
| **NL** | `count`, `trad` | Lista de números en una fila |

## Funciones Auxiliares

```python
nuevoSimbolo(nombre, tipo, filas, cols)  # Añade símbolo a la tabla
existe(nombre)                            # Verifica si existe un símbolo
getFilas(nombre)                          # Obtiene filas de una matriz
getCols(nombre)                           # Obtiene columnas de una matriz
error(mensaje)                            # Reporta error semántico
```

## Características Técnicas

### Traducción Dirigida por la Sintaxis
- **Header automático**: Incluye la función `matmul()` en todo programa
- **Concatenación de strings**: Usa el operador `||` para construir código
- **Propagación de atributos**: De hojas hacia la raíz del árbol sintáctico

### Manejo de Errores
1. **Matriz no declarada**: Uso de variable no definida
2. **Dimensiones incompatibles**: Violación de la regla del producto matricial
3. **Sintaxis incorrecta**: Errores de parsing

## Limitaciones

- Solo soporta el operador de multiplicación (`*`)
- No permite suma, resta u otras operaciones matriciales
- Las matrices deben ser rectangulares (todas las filas con igual número de columnas)
- Solo genera código Python (no ejecuta directamente)

## Extensiones Futuras

- [ ] Suma y resta de matrices
- [ ] Transposición de matrices
- [ ] Producto elemento a elemento (Hadamard)
- [ ] Matrices identidad y cero predefinidas
- [ ] Indexación de elementos individuales
- [ ] Operaciones con escalares

## Autor

Implementación de una gramática traducida para el curso de Compiladores.

---

**Nota**: Este lenguaje es una demostración académica de traducción dirigida por la sintaxis y generación de código para operaciones matriciales.