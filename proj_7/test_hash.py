def string_hash(item):
        """ Converts the key into a hash value. """
        if len(item) > 4 and \
            (item[0].islower() or item[0].isupper()):
            item = item[1:]

        total = 0
        for char in item:
            total += ord(char)
        if len(item) > 2:
            total -= 2 * ord(item[-1])

        return total

def main():
    test = "it"
    #for item in range(0,1000):
    #    print(string_hash(str(item)))

    print(abs(hash("iceman"))%16)
    print(abs(hash("cinema"))%16)

if __name__ == "__main__":
    main()
