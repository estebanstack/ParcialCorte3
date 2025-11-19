from antlr4 import *
from MatricesLexer import MatricesLexer
from MatricesParser import MatricesParser
from EvalVisitor import EvalVisitor

code = """
matrix A = [[1,2,3],[4,5,6]];
matrix B = [[7,8],[9,10],[11,12]];
matrix C = A * B;
"""

input_stream = InputStream(code)
lexer = MatricesLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = MatricesParser(tokens)
tree = parser.program()


visitor = EvalVisitor()
python_code = visitor.visit(tree)

print("CODIGO GENERADO:")
print(python_code)

namespace = {}
exec(python_code, namespace)   

print("MATRIZ A:")
print(namespace["A"])
print("\nMATRIZ B:")
print(namespace["B"])
print("\nRESULTADO C = A * B (PRODUCTO PUNTO):")
print(namespace["C"])
