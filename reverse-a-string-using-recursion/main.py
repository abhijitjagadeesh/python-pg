INPUT_STRING = "Hello I am abhijit"

def reverse(input_string):
    if input_string == "":
        return ""

    return reverse(input_string[1:]) + input_string[0]

print(reverse(INPUT_STRING))