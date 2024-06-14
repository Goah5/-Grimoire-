import random

def generate_numbers(query):
    query = query.replace(' ', '')
    
    if query.isdigit():
        # Case: X
        X = int(query)
        return [random.randint(1, X) for _ in range(X)]

    elif query[0] == 'd':
        # Case: dX
        X = int(query[1:])
        return [random.randint(1, X)]

    elif 'd' in query:
        # Cases: dX±C or NdX±C
        parts = query.split('d')
        N = int(parts[0]) if parts[0].isdigit() else 1
        remaining = parts[1]

        if '+' in remaining:
            X, C = map(int, remaining.split('+'))
            return [random.randint(1, X) + C for _ in range(N)]

        elif '-' in remaining:
            X, C = map(int, remaining.split('-'))
            return [random.randint(1, X) - C for _ in range(N)]

        else:
            X = int(remaining)
            return [random.randint(1, X) for _ in range(N)]

    else:
        return None

# Примеры использования
print(generate_numbers('10'))
print(generate_numbers('5'))
print(generate_numbers('d12'))
print(generate_numbers('7'))
print(generate_numbers('4d5+2'))
print(generate_numbers('3d4-1'))
print(generate_numbers('d7-2'))
print(generate_numbers('2d10'))
