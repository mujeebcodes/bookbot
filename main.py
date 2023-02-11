
def main():
    text = get_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    letter_count = count_letters(text)
    print_book_report(letter_count, word_count)

def get_text(path):
    with open("books/frankenstein.txt") as book:
        return book.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter.isalpha():
            if letter not in letter_count_dict:
                letter_count_dict[letter] = 1
            else:
                letter_count_dict[letter] += 1
    return letter_count_dict

def print_book_report(letter_count, word_count):
    converted= list(zip(letter_count.keys(), letter_count.values()))
    report_list = sorted(converted)
    print("--- Begin report of frankenstein.txt ---")
    print("{} words found in the document \n".format(word_count))
    for char in report_list:
        print(f"The {char[0]} character was found {char[1]} times")

    print("\n--- End report ---")

main()