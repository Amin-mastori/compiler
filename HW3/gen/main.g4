grammar main;

// Start rule
startrule: (National_number | Email | Postal_code | Decimal_number | Software_version | Website_address | DIGIT)+ EOF;

// Rule for national numbers (example: US phone number)
National_number : DIGIT+ ('-' DIGIT+)? ;

// Rule for email addresses
Email : [a-zA-Z0-9._%+-]+[@][a-zA-Z0-9.-]+[\].[a-zA-Z]{2,} ;

// Rule for postal codes (example: US postal code)
Postal_code : (DIGIT{5} | DIGIT{5} '-' DIGIT{4}) ;

// Rule for decimal numbers
Decimal_number : DIGIT+ ('.' DIGIT+)?;

// Rule for software versions (example: semantic versioning)
Software_version : DIGIT+ '.' DIGIT+ '.' DIGIT+ ;

// Rule for website addresses
Website_address : 'http://' [a-zA-Z0-9.-]+ | 'https://' [a-zA-Z0-9.-]+ ;

// Other rules
DIGIT : [0-9] ;
