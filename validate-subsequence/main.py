test_list = [5, 1, 22, 25, 6, -1, 8, 10]
sub_sequence = [1, 22, 25, 6, 9, 90, 11]


# return true or false is a sub_sequence is a part of array
# O(n) Time O(n) Space
def validate_sub_sequence():
    if len(sub_sequence) == 0:
        return False
    sub_seq_index = 0
    for number in test_list:
        if number == sub_sequence[sub_seq_index]:
            sub_seq_index += 1
    return len(sub_sequence) == sub_seq_index


#   seq_idx = 0
#   for number in test_list:
#     if seq_idx == len(sub_sequence):
#       break
#     if number == sub_sequence[seq_idx]:
#       seq_idx += 1
#   return seq_idx == len(sub_sequence)

print(validate_sub_sequence())