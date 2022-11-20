import math
START = 3
END = 100

def get_prime_numbers(start, end):
    result = []
    for num in range(start, end + 1):
        is_prime = True
        for divisor in range(2, math.ceil(num // 2) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
    return result 

print(get_prime_numbers(START, END))