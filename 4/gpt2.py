import random

def generate_numbers(query):
    parts = query.split('d')
    
    n = 1
    x = 6  # По умолчанию, если не указан X, то считаем, что он равен 6
    c = 0
    
    if len(parts) > 1:
        if '+' in parts[1]:
            x, c = map(int, parts[1].split('+'))
        elif '-' in parts[1]:
            x, c = map(int, parts[1].split('-'))
            c = -c
        else:
            x = int(parts[1])

    if len(parts[0]) > 0:
        n = int(parts[0])

    result = [random.randint(1, x) + c for _ in range(n)]
    return result

# Примеры использования
print(generate_numbers("12"))          # Пример 1
print(generate_numbers("d12"))         # Пример 2
print(generate_numbers("4d5+2"))       # Пример 3
print(generate_numbers("d7-2"))        # Пример 4
print(generate_numbers("2d10"))        # Пример 5
