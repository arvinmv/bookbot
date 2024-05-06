import string

def get_book_content():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def get_word_count(file_contents):
    words = file_contents.split()
    word_count = len(words) 
    print(word_count)

def count_letters(file_contents):
    words = file_contents.split()
    letter_int_dict = {}
    for letter in string.ascii_lowercase:
        letter_int_dict[letter] = 0
    for word in words:
        for letter in word.lower():
            if letter.isalpha():
                letter_int_dict[letter] += 1
    for letter in letter_int_dict:
        for letter, count in letter_int_dict.items():
            print(f'The {letter} character was found {count} times')

def main():
    file_contents = get_book_content()
    get_word_count(file_contents)
    count_letters(file_contents)

main()
