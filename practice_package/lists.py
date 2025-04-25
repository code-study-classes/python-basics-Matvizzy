def find_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

def find_largest_element(lst):
    return max(lst) if lst else None

def count_even_numbers(lst):
    return len([x for x in lst if x % 2 == 0])

def remove_duplicates(lst):
    return list(set(lst))

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

def filter_palindromes(lst):
    return [s for s in lst if s == s[::-1]]

def normalize_names(names):
    return [name.strip().title() for name in names]

