from MatricesVisitor import MatricesVisitor
from MatricesParser import MatricesParser

class EvalVisitor(MatricesVisitor):

    def __init__(self):
        # Tabla de símbolos: id → { filas, cols, tipo }
        self.symtab = {}
        self.lines = []

    def visitProgram(self, ctx):
        for stmt in ctx.stmt():
            self.visit(stmt)

        # Encabezado: implementacion de matmul
        HEADER = """def matmul(A, B):
    filas = len(A)
    cols  = len(B[0])
    kmax  = len(A[0])
    return [[sum(A[i][k] * B[k][j] for k in range(kmax))
             for j in range(cols)] for i in range(filas)]

"""
        return HEADER + "\n".join(self.lines)

    def visitMatrixDecl(self, ctx):
        name = ctx.ID().getText()

        # Caso 1: matrix A = literal
        if ctx.matrixLiteral():
            code, meta = self.visit(ctx.matrixLiteral())
            self.symtab[name] = {
                "tipo": "matriz",
                "rows": meta["rows"],
                "cols": meta["cols"]
            }
            self.lines.append(f"{name} = {code}")
            return None

        # Caso 2: matrix A = expresion
        if ctx.expr():
            code, meta = self.visit(ctx.expr())
            self.symtab[name] = {
                "tipo": "matriz",
                "rows": meta["rows"],
                "cols": meta["cols"]
            }
            self.lines.append(f"{name} = {code}")
            return None

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        expr_code, meta = self.visit(ctx.expr())
        self.lines.append(f"{name} = {expr_code}")
        return None

    def visitExpr(self, ctx):
        # ID simple
        if ctx.ID():
            name = ctx.ID().getText()
            if name not in self.symtab:
                raise Exception(f"Matriz no declarada: {name}")
            return name, {
                "rows": self.symtab[name]["rows"],
                "cols": self.symtab[name]["cols"]
            }

        # Literal
        if ctx.matrixLiteral():
            return self.visit(ctx.matrixLiteral())

        # Producto E1 * E2
        if len(ctx.expr()) == 2:
            left_code, left_meta = self.visit(ctx.expr(0))
            right_code, right_meta = self.visit(ctx.expr(1))

            # Verificacion de dimensiones
            if left_meta["cols"] != right_meta["rows"]:
                raise Exception("Dimensiones incompatibles para producto matricial")

            # Dimensiones del resultado
            filas = left_meta["rows"]
            cols  = right_meta["cols"]

            # Traduccion a matmul
            return f"matmul({left_code}, {right_code})", {
                "rows": filas,
                "cols": cols
            }

    # LITERALES DE MATRIZ
    def visitMatrixLiteral(self, ctx):
        rows = []
        cols = None

        for r in ctx.row():
            numbers = [n.getText() for n in r.NUMBER()]
            if cols is None:
                cols = len(numbers)
            elif cols != len(numbers):
                raise Exception("Todas las filas deben tener el mismo número de columnas")

            rows.append("[" + ",".join(numbers) + "]")

        code = "[" + ",".join(rows) + "]"
        return code, {
            "rows": len(rows),
            "cols": cols
        }
