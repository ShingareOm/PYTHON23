class PrintIntegerCharacter:
    def print_int_char(self, n, c):
        print("Integer:", n)
        print("Character:", c)

    def print_char_int(self, c, n):
        print("Character:", c)
        print("Integer:", n)

# Example usage:
printer = PrintIntegerCharacter()

# Method with parameters (int, char)
printer.print_int_char(5, 'A')

# Method with parameters (char, int)
printer.print_char_int('B', 10)
