from stats import word_count, return_characaters, sort_dict_list
import sys 

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main(s = sys.argv):
    if len(s) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = s[1]
    text = get_book_text(book_path)
    words_counted = word_count(text)
    new_dict = return_characaters(text)
    sorted_dict = sort_dict_list(new_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ...")
    print(f"----------- Word Count ----------\nFound {words_counted} total words")
    print(f"--------- Character Count -------\n{sorted_dict}")
    print("============= END ===============")
main()
