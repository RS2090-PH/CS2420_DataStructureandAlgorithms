def string_hash(item):
    if len(item) > 4 and \
        (item[0].islower() or item[0].isupper()):
        item = item[1:]

    total = 0
    for ch in item:
        total += ord(ch)
    if len(item) > 2:
        total -= 2 * ord(item[-1])

    return total

def main():
    test1 = input("Provide a string: ")
    print(string_hash(test1))

    test2 = input("Provide a string: ")
    print(string_hash(test2))

if __name__ == "__main__":
    main()
