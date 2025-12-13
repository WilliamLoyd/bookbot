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

def sort_on(character_dict):
    return character_dict["nums"]

def sorting(character_dict):
    sorted_characters = []
    for i in character_dict:
        if i.isalpha():
            temp_dict = {"char": i, "nums": character_dict[i]}
            sorted_characters.append(temp_dict)
    sorted_characters.sort(reverse=True, key=sort_on)

    return sorted_characters


