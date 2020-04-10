class test_class(object):
    def __init__(self):
        self.lyst1 = list()
        self.lyst2 = [4,8,9,5,7,6,2,1,75,6]
        for item in range(0,15):
            self.lyst1.append(item)

    def __str__(self): #FIXME: Complete this
            temp = "["
            count = 0

            for item in self.lyst1:
                if count == 0:
                    temp = temp + str(item)
                    count += 1
                else:
                    temp = temp + ", " + str(item)
            temp = temp + "]"

            return temp


def main():
    test = test_class()
    print(test)

if __name__ == "__main__":
    main()
