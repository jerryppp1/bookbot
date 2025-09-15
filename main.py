from stats import word_counters, letter_counter, sorted_list
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()




    
def main():
    if(len(sys.argv)) == 2 :
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(book_path)
    counts = word_counters(book)
    letters = letter_counter(book)
    sorted_chars = sorted_list(letters)
    print(counts)
    for entry in sorted_chars:
        ch = entry["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {entry['num']}")
    print(len(sys.argv))

    
    


    
main()