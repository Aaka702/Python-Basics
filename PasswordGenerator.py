class PasswordGenerator:
    @staticmethod
    def generate_password(decimal_number, person_name):
        try:
            scientific_notation = format(float(decimal_number), ".1e")
            coefficient, exponent = map(str, scientific_notation.split('e'))
            coefficient_digit = str(sum(map(int, coefficient.replace('.', ''))) % 9)
            exponent_digit = str(sum(map(int, exponent)) % 9)
            s1 = ''.join(digit_words[int(digit)][:3] for digit in coefficient_digit + exponent_digit)
            s2 = ''.join(char for i, char in enumerate(person_name) if (i + 1) % 2 == int(exponent_digit) % 2)
            password = f"{s1}@{s2}"
            print(password)
        except ValueError:
            print("Invalid input")


num_test_cases = int(input().strip())
for _ in range(num_test_cases):
    number, name = input().strip().split()
    PasswordGenerator.gener
