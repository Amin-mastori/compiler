grammar Password;

start: check EOF;


check: STRING {
    if ($STRING.text.length() >= 8) {
        System.out.println("(True)");
    } else {
        System.out.println("(False)");
    }
};

STRING: '"' ~["]* '"';

WS: [ \t\r\n]+ -> skip;