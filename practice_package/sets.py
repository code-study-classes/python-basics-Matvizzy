def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

def find_common_elements(set1, set2):
    return set1 & set2

def find_shared_items(*sets):
    return set.intersection(*sets)

def is_superset(set_a, set_b):
    return set_a >= set_b

def remove_duplicates(items):
    return list(set(items))
