grammar main;

palindrome
    : 'z' entry EOF ;
entry
    : '1' entry '1'
    | '2' entry '2'
    | '3' entry '3'
    | '4' entry '4'
    | '5' entry '5'
    | '6' entry '6'
    | '7' entry '7'
    | '8' entry '8'
    | '9' entry '9'
    | '0' entry '0'
    | '1'
    | '2'
    | '3'
    | '4'
    | '5'
    | '6'
    | '7'
    | '8'
    | '9'
    | '0'
    |
    ;

WS : [ \t\r\n]+ -> skip ;