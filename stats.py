def count_words(text):
    word_count = 0
    for word in text.split():
        word_count += 1
    return word_count

def count_characters(text):
    characters_dict = {}
    for character in text.lower():
        if character not in characters_dict:
            characters_dict[character] = 1
        elif character in characters_dict:
            characters_dict[character] += 1
    return characters_dict

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
