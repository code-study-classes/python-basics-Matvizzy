check_between_numbers = lambda A, B, C: (A < B < C) or (C < B < A)

check_odd_three = lambda number: 100 <= abs(number) <= 999 and abs(number) % 2 != 0

check_unique_digits = lambda number: len(set(str(abs(number)))) == len(str(abs(number))) if 100 <= abs(number) <= 999 else False

def check_palindrome_number(number):
    return str(abs(number)) == str(abs(number))[::-1]

check_ascending_digits = lambda number: 100 <= abs(number) <= 999 and list(str(abs(number))) == sorted(str(abs(number)))
