import re
import random

def generate_numbers(query):
    match = re.match(r'(\d+)?d(\d+)([+\-]\d+)?', query)
    
    if not match:
        print("Неверный формат запроса.")
        return
    
    N = int(match.group(1)) if match.group(1) else 1
    X = int(match.group(2))
    C = int(match.group(3)) if match.group(3) else 0
    
    result = [random.randint(1, X) + C for _ in range(N)]
    print(result)

# Примеры использования:
generate_numbers("d12")
generate_numbers("7")
generate_numbers("4d5+2")
generate_numbers("d7-2")
generate_numbers("2d10")
