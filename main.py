from stats import get_num_words
from stats import get_chars_dict
from stats import chars_dict_to_sorted_list
import sys

#Take the relative file path to the book and read the text from it into a string
def get_book_text(file_path):
    temp_book_text = ""
    with open(file_path) as f:
        temp_book_text = f.read()
    return temp_book_text

#Can print the text of the book OR find the total number of words and counts of the number of times each character is used
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        num_words = get_num_words(book_text)
        char_count = get_chars_dict(book_text)
        sort_counts = chars_dict_to_sorted_list(char_count)

        #Print the report
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print ("--------- Character Count -------")
        for item in sort_counts:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()