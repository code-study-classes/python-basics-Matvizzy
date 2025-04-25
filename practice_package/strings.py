def check_brackets(text):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in text:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    
    return not stack

def count_vowel_groups(text):
    vowels = "aeiouAEIOU"
    count = 0
    in_group = False
    for char in text:
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count

def reverse_words(text):
    return ' '.join(reversed(text.split()))

def to_uppercase(text):
    return text.upper()

def encrypt_sentence(sentence, shift):
    result = ""
    for char in sentence:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(parts[::-1])

