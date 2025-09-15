def word_counters(word):
    split = word.split()
    i = len(split)
    return (f"Found {i} total words")

def letter_counter(word):
    lowercase_word = str.lower(word)
    char_dict = {}
    for i in lowercase_word:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1

    return char_dict

def sorted_list(word):
    new_list = []
    for (char, count) in word.items():
        new_list.append({"char": char, "num": count})
    new_list.sort(reverse=True, key=lambda item: item["num"])
    return new_list
    