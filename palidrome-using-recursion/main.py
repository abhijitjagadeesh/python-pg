INPUT_STRING = "1"

def palindrome(input_string):
    if len(input_string) == 0:
        return False
    if len(input_string) == 1:
        return True
    if input_string[0] != input_string[len(input_string) - 1]:
        return False
    return palindrome(input_string[1:len(input_string) - 1])


print(palindrome(INPUT_STRING))