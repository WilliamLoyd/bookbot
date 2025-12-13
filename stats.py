def get_num_words(text):
    words = text.split()
    counter = len(words)
    return counter

def character_count(text):
    characters = text.lower()
    character_dict = {}
    for i in characters:
        if i in character_dict:
            character_dict[i] += 1
        else:
            character_dict[i] = 1
    return character_dict

