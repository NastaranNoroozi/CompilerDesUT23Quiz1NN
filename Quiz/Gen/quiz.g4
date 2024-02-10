// Define a grammar called PalindromeNumbers
grammar quiz;
//grammar Palindrome;

start
    :   sequence EOF
    ;

sequence
    :   sequence element
    |   element
    ;

element
    :   PalindromeNumber
    |   NonPalindromeNumber
    ;

PalindromeNumber
    :   Digit Digit Digit Digit Digit
        {
            number = str(self.text)
            reverse_number = number[::-1]
            if number == reverse_number:
                print(f"Found palindrome: {number}")
        }
    ;

NonPalindromeNumber
    :   Digit+
    ;

Digit
    :   [0-9]
    ;

WS  :   [ \t\r\n]+ -> skip
    ;
