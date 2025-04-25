def count_char_occurrences(text, char):
    return text.count(char)

def merge_dicts(dict1, dict2):
    result = dict1.copy() 
    result.update(dict2)  
    return result

def get_keys_with_value(dct, value):
    return [key for key, val in dct.items() if val == value]

def is_subset(dict1, dict2):
    return all(item in dict2.items() for item in dict1.items())

def deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, dict):
            d[k] = deep_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d

def dict_to_table(d):
    return [[k, v] for k, v in d.items()]

def invert_dictionary(d):
    return {v: k for k, v in d.items()}
