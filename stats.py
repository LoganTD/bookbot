def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letter_dict = {}
    for letter in text:
        letter = letter.lower() #skips duplicate letters based on case
        if letter in letter_dict:
            letter_dict[letter] += 1 #increases count of found character
        else:
            letter_dict[letter] = 1  #creates dictionary entry if first time character is found
    return letter_dict 

#key to sort list by count
def sort_on(dict_item):
    return dict_item["count"]

def sort_chars_by_count(char_counts):
    chars_list = [] #list to hold dictionary of chars and their counts
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})
    #sort in descending order based on count from sort_on method
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def format_output(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    #for loop to print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        #if statment that skips non-alphabetical characters
        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")

    print("============= END ===============")