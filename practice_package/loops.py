def sum_even_digits(number):
    return sum(int(digit) for digit in str(abs(number)) if int(digit) % 2 == 0)

def count_vowel_triplets(text):
    vowels = 'aeiouy'
    text = text.lower()
    count = 0
    for i in range(len(text) - 2):
        if text[i] in vowels and text[i+1] in vowels and text[i+2] in vowels:
            count += 1
    return count

def find_fibonacci_index(number):
    a, b = 1, 1
    index = 2
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1

def remove_duplicates(string):
    result = []
    for char in string:
        if not result or result[-1] != char:
            result.append(char)
    return ''.join(result)
