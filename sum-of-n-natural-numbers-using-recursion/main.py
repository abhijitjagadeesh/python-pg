N = 10

def sum_of_n_natural_numbers(numbers):
    if numbers == 0:
        return 0
    return sum_of_n_natural_numbers(numbers - 1) + numbers


print(sum_of_n_natural_numbers(N))