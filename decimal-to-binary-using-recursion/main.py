INPUT_DECIMAL = 233

def get_binary(decimal, result):
    if decimal == 0:
        return result
    result = str(decimal % 2) + result
    return get_binary(decimal // 2, result)


result = ""
print(get_binary(INPUT_DECIMAL, result))