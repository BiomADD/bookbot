def word_count(text):
    list_of_words = text.split()
    return len(list_of_words)
    
def return_characaters(text):
    dict_characters = {}
    new_text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  
    for character in new_text:
        if character in alphabet and character in dict_characters:
            dict_characters[character] += 1
        elif character in alphabet:
            dict_characters[character] = 1
    return dict_characters

def sort_dict_list(dict_characters):
    sorted_dict = sorted(dict_characters.items(), key=lambda x: x[1], reverse=True)
    return "\n".join(f"{key}: {value}" for key, value in sorted_dict)

