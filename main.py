import sys
from stats import get_num_words, character_count, sorting
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    counter = get_num_words(text)
    var2 = character_count(text)
    sorted_chars = sorting(var2)

    print(f'============ BOOKBOT ============')
    print(f"Analyzing book found at {path_to_file}...")
    print(f"Found {counter} total words")
    print(f"--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['nums']}")


        


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


    

main()
    
    
    
