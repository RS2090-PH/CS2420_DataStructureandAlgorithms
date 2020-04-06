

def main():
    temp = open("AliceInWonderland.txt", "r", encoding="utf8")
    for line in temp:
        print(line)

    temp.close()

if __name__ == "__main__":
    main()
