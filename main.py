from stats import word_count, letter_count, sort_chars_by_count, format_output
import sys

#creates string of text file found at filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    book_path = sys.argv[1]
    text = get_book_text(book_path)  #text file converted to string, text
    count = word_count(text) #gets word count of string, text
    letters = letter_count(text) #creates dictionary of characters and count found in string, text
    letters = sort_chars_by_count(letters) #list of dictionaries of characters and count, sorted in descending order by count
    format_output(book_path, count, letters) #formats output to print to the console

main()
