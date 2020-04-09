"""
Author: Robby Stohel
File: word_count.py

This program shows the raw and cleaned word counts of the AliceInWonderland.txt
file as both counts fail to match those displayed in the unittest and project
instructions. The clean_file function was copied directly from the instructions
to show a discrepancy in the function as well. Additionally, the file itself
must be encoded to utf-8 when it is read in, otherwise we receive decoding errors.
"""

def clean_line(raw_line):
    '''removes all punctuation from input string and
    returns a list of all words which have a length greater than one '''
    if not isinstance(raw_line, str):
        raise ValueError("Input must be a string")
    line = raw_line.strip().lower()
    line = list(line)
    for index in range(len(line)):  # pylint: disable=C0200
        if line[index] < 'a' or line[index] > 'z':
            line[index] = ' '
    cleaned = "".join(line)
    words = [word for word in cleaned.split() if len(word) > 1]
    return words

def main():
    """ Main driver to run count tests and display results """
    words = ["the", "and", "to", "of", "it", "she", "you", "said", "in", "alice", "was", "that", "as", "her", "with"]
    expected_count = [1818, 940, 809, 631, 610, 553, 481, 462, 431, 403, 358, 330, 274, 248, 228]
    raw_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cleaned_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    # This loop counts the raw words
    for value in range(0, 15):
        text_file = open("AliceInWonderland.txt", "r", encoding="utf8")
        for line in text_file:
            if words[value] in clean_line(line):
                raw_count[value] += 1
        text_file.close()

    # This loop counts the cleaned lines
    for value in range(0, 15):
        text_file = open("AliceInWonderland copy.txt", "r", encoding="utf8")
        for line in text_file:
            if words[value] in line:
                cleaned_count[value] += 1
        text_file.close()

    #This loop prints the results
    for value in range(0, 15):
        print("Word: %-8s        Raw Count: %-5d        Cleaned Count: %-5d        Expected Count: %-5d"\
            %(words[value], raw_count[value], cleaned_count[value], expected_count[value]))

if __name__ == "__main__":
    main()
