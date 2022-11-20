

test_list = [3, 5, -4, 8, 11, 1, -1, 6 ]
target_sum = -3


def find_two_numbers(test_list):
    entries = {}
    for number in test_list:
        potential_match = target_sum - number
        if number in entries:
            return [potential_match, number]
        entries[potential_match] = True
    return []

print(find_two_numbers(test_list))

# Find 2 numbers from test_list whose sum is equal to target_sum in any order
# If not found return []

# O(n^2) time O(1) space
# def two_number_sum():
#   for number_one in range(len(test_list) - 1):
#     for number_two in range(1, len(test_list)):
#       if test_list[number_one] + test_list[number_two] == target_sum:
#         return [test_list[number_one], test_list[number_two]]
#   return []

# O(n) time O(n) space
# def two_number_sum():
#   entries = {}
#   for number in test_list:
#     potential_match = target_sum - number
#     if number in entries:
#       return [number, potential_match]
#     entries[potential_match] = True
#   return []

#O(nlong(n)) Time O(1) space