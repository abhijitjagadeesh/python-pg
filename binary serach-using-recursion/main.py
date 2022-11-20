INPUT_ARRAY = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TARGET = 0

def search(input_array, target, start, end):

    if start > end:
        return False

    mid_index = (start + end) // 2 

    if input_array[mid_index] == target:
        return True
    elif input_array[mid_index] > target:
        return search(input_array, target, 0, mid_index - 1)
    else:
        return search(input_array, target, mid_index + 1, end)
    

print(search(INPUT_ARRAY, TARGET, 0, len(INPUT_ARRAY) - 1))