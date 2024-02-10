grammar palindrome;

start: PALINDROME* EOF;

palindrome: 'z' entry EOF;

entry: 'a' entry 'a'
     | 'b' entry 'b'
     | DIGIT entry DIGIT
     | 'a'
     | 'b'
     | DIGIT
     | ;

DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip;