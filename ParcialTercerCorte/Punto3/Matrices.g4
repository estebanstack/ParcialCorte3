
grammar Matrices;

// Programa: secuencia de sentencias
program
    : stmt* EOF
    ;

// Sentencias: declaracion o asignacion
stmt
    : matrixDecl ';'
    | assign     ';'
    ;

// Declaracion de matrices
matrixDecl
    : 'matrix' ID '=' matrixLiteral
    | 'matrix' ID '=' expr
    ;

// Asignacion general:  id = expr
assign
    : ID '=' expr
    ;

// Expresiones: id, literal, o producto
expr
    : ID
    | matrixLiteral
    | expr '*' expr
    ;

// Literal de matriz: filas separadas por coma
matrixLiteral
    : '[' row (',' row)* ']'
    ;

row
    : '[' NUMBER (',' NUMBER)* ']'
    ;

ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER  : '-'?[0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
