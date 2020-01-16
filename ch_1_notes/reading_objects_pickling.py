lyst = list()
file_obj = open("items.dat", "rb")
while True:
    try:
        item = pickle.load(file_obj)
        lyst.append(item)
    except EOFError:  # uses exception because eof has no warning and causes error
        file_obj.close()
        break
print(lyst)