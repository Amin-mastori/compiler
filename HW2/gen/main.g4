grammar main;
start:
    Id '=' expr EOF
    ;

expr:
    expr '+' term #rule_plus
    | expr '-' term  #rule_minus
    | term #rule3
    ;

term:
    term '*' fact
    | term '/' fact
    | fact
    ;

fact:
    Id
    | Number
    | '('expr')'
    ;

/* Lexical rules*/
Plus: '+';
MINUS: '-';
MUL: '*';
DIVIDE: '/';
ASSIGN: '=';


Id: IDENTIFIER;
Number: NUMBER;

fragment IDENTIFIER: [a-zA-Z][a-zA-Z]*;
fragment NUMBER: [0-9]+;

Newline: '\n' -> skip;
Whitespace: [ \t\r]+ -> channel(HIDDEN);