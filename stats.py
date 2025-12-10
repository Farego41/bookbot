#Finds the total number of words in the text file
def get_num_words(book_text):
    list_of_words = book_text.split()
    number_of_words = len(list_of_words)
    return number_of_words

#Counts the number of times each character is used in the story
def get_chars_dict(book_text):
    character_count = {}
    for i in range(0,len(book_text)):
        if book_text[i].lower() =="\ufeff":
            continue
        if book_text[i].lower() not in character_count:
            character_count[book_text[i].lower()] = 1
        else:
            character_count[book_text[i].lower()] += 1
    return character_count

def sort_on(items):
    return items["num"]

#Sorts your character counts biggest to smallest by creating a new list of dictionaries.
def chars_dict_to_sorted_list(char_count):
    list_of_dicts = []
    for char in char_count:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = char_count[char]
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts