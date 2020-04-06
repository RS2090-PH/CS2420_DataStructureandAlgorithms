"""
Author: Robby Stohel
File: main.py

A driver program to test/run the hashmap.py file. Converts the
file contents into hashmap contents, then determines the most used
words in the the hashmap. Currently incomplete, as some characters
in the file don't seem to decode properly with readline?
"""

from hashmap import HashMap

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
    """ Main driver to run program. """
    hashmap = HashMap()

    text_file = open("AliceInWonderland.txt", "r", encoding="utf8")

    for line in text_file:
        temp = clean_line(line)
        for word in temp:
            if hashmap.contains(word) is True:
                tempvalue = hashmap.get(word)
                hashmap.set(word, (tempvalue + 1))
            else:
                hashmap.set(word, 1)

    hashmap.print_top()
    text_file.close()

if __name__ == "__main__":
    main()
