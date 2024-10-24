# Ćwiczenie 1: Operatory arytmetyczne
# Napisz program, który wykonuje podstawowe operacje arytmetyczne na dwóch liczbach.

a = 10
b = 5

# Dodawanie
result_addition = a + b
print("Addition:", result_addition)

# Odejmowanie
result_subtraction = a - b
print("Subtraction:", result_subtraction)

# Mnożenie
result_multiplication = a * b
print("Multiplication:", result_multiplication)

# Dzielenie
result_division = a / b
print("Division:", result_division)

# Reszta z dzielenia
result_modulo = a % b
print("Modulo:", result_modulo)

# Potęgowanie
result_exponentiation = a ** b
print("Exponentiation:", result_exponentiation)

# Ćwiczenie 2: Operatory porównania
# Napisz program, który sprawdza różne warunki porównujące dwie liczby.

a = 10
b = 5

# Równość
is_equal = a == b
print("Is equal:", is_equal)

# Różność
is_not_equal = a != b
print("Is not equal:", is_not_equal)

# Większość
is_greater = a > b
print("Is greater:", is_greater)

# Mniejszość
is_less = a < b
print("Is less:", is_less)

# Większe lub równe
is_greater_or_equal = a >= b
print("Is greater or equal:", is_greater_or_equal)

# Mniejsze lub równe
is_less_or_equal = a <= b
print("Is less or equal:", is_less_or_equal)

# Ćwiczenie 3: Operatory logiczne
# Napisz program, który sprawdza różne warunki logiczne na dwóch liczbach.

a = 10
b = -5

# Logiczne AND
are_both_greater_than_zero = (a > 0) and (b > 0)
print("Are both greater than zero:", are_both_greater_than_zero)

# Logiczne OR
is_one_greater_than_zero = (a > 0) or (b > 0)
print("Is at least one greater than zero:", is_one_greater_than_zero)

# Logiczne NOT
is_a_not_zero = not (a == 0)
print("Is a not zero:", is_a_not_zero)

# Ćwiczenie 4: Operatory przypisania
# Napisz program, który demonstruje użycie różnych operatorów przypisania.

a = 10

# Przypisanie wartości
print("Initial value of a:", a)

# Dodawanie i przypisanie
a += 5
print("After adding 5:", a)

# Odejmowanie i przypisanie
a -= 3
print("After subtracting 3:", a)

# Mnożenie i przypisanie
a *= 2
print("After multiplying by 2:", a)

# Dzielenie i przypisanie
a /= 4
print("After dividing by 4:", a)

# Reszta z dzielenia i przypisanie
a %= 6
print("After modulo 6:", a)

# Potęgowanie i przypisanie
a **= 3
print("After exponentiation to the power of 3:", a)

# Ćwiczenie 5: Operatory bitowe
# Napisz program, który wykonuje operacje bitowe na dwóch liczbach.

a = 10  # 1010 w systemie binarnym
b = 5   # 0101 w systemie binarnym

# Bitowe AND
result_and = a & b
print("Bitwise AND:", result_and)

# Bitowe OR
result_or = a | b
print("Bitwise OR:", result_or)

# Bitowe XOR
result_xor = a ^ b
print("Bitwise XOR:", result_xor)

# Przesunięcie bitowe w lewo
result_shift_left = a << 2
print("Bitwise left shift:", result_shift_left)

# Przesunięcie bitowe w prawo
result_shift_right = b >> 2
print("Bitwise right shift:", result_shift_right)
