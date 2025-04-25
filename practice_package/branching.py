def is_weekend(day):
    return day == 6 or day == 7

def get_discount(amount):
    return amount * 0.1 if amount >= 5000 else amount * 0.05 if amount >= 1000 else 0

def describe_number(n):
    if n < 10:
        return f"нечетное однозначное число" if n % 2 != 0 else f"четное однозначное число"
    elif n < 100:
        return f"нечетное двузначное число" if n % 2 != 0 else f"четное двузначное число"
    else:
        return f"нечетное трехзначное число" if n % 2 != 0 else f"четное трехзначное число"

def convert_to_meters(unitNumber, lengthInUnits):
    units = {1: 0.1, 2: 1000, 3: 1, 4: 0.001, 5: 0.01}
    return lengthInUnits * units[unitNumber]

def describe_age(age):
    ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    tens = ['', '', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if 20 <= age < 30:
        return f"{tens[2]} {ones[age % 10]} лет"
    elif age % 10 == 1:
        return f"{ones[age // 10]} {ones[age % 10]} год"
    return f"{ones[age // 10]} {ones[age % 10]} лет"
