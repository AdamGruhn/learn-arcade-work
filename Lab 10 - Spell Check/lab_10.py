import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    # Open the dictionary file for reading, store in dictionary file
    dictionary_file = open("dictionary.txt")

    # Makes list to store dictionary words
    dictionary_list = []

    # Loop through each line of the dictionary
    for line in dictionary_file:
        # Remove line feed, returns, or spaces at end
        line = line.strip()

        dictionary_list.append(line)

    dictionary_file.close()

    print("--- Linear Search ---")

    wonderland_file = open("AliceInWonderLand200.txt")
    
    line_number = 0
    for line in wonderland_file:
        line_number += 1
        linear_word_list = split_line(line)
        for word in linear_word_list:
            list_position = 0
            while list_position < len(dictionary_list) and word.upper() != dictionary_list[list_position]:
                list_position += 1
            if list_position < len(dictionary_list):
                pass
            else:
                print(f"Line {line_number} possible misspelled word: {word}")
    wonderland_file.close()

    print("--- Binary Search ---")

    wonderland_file = open("AliceInWonderLand200.txt")
    line_number = 0
    for line in wonderland_file:
        line_number += 1
        binary_word_list = split_line(line)
        for word in binary_word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_position = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_position] < key:
                    lower_bound = middle_position + 1
                elif dictionary_list[middle_position] > key:
                    upper_bound = middle_position - 1
                else:
                    found = True

            if found:
                pass
            else:
                print(f"Line {line_number} possible misspelled word: {word}")

    wonderland_file.close()


main()
