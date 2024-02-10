grammar quiz2;

startRule: number*;

number: POSITIVE_INT {
    if isPalindromeNumber($POSITIVE_INT.text):
        print("Palindrome Number:", $POSITIVE_INT.text)
    };

// Lexer rules
POSITIVE_INT: [1-9] [0-9]*;

// Helper method to check if a number is a palindrome
@members {
    def isPalindromeNumber(self, number):
        reversed_num = number[::-1]
        return number == reversed_num
}