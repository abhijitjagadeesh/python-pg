NUMBER = 10
cache = {}

def fib(number):

    result = ""
    if number == 0 or number == 1:
        return number
    if number in cache:
        return cache[number]
    else:
        result = fib(number - 2) + fib(number - 1)
        cache[number] = result
    return result


for num in range(NUMBER):
    print(fib(num))