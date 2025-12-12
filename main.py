from stats import get_num_words, character_count
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file).split()
    counter = get_num_words(text)
    print(f"Found {counter} total words")
        
        


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


    

main()
    
    
    
