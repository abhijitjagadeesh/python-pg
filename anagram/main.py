WORDS = [ 'a', 'other', 'bat', 'cat', 'cta', 'tab']
anagrams_list = {}

def anagrams(word_list):
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_list.keys():
            anagrams_list[sorted_word].append(word)
        else:
            anagrams_list[sorted_word] = [word]

anagrams(WORDS)
for key, value in anagrams_list.items():
    if len(value) > 1:
        print(value)

