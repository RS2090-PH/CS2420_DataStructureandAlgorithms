
class Bottle():
    def __init__(self, cap="closed", lab="red", lao=True, hei=7.5, wid=3, ful=True):
        self.smiley = "present"
        self.cap = cap
        self.label = lab
        self.label_on = lao
        self.height = hei
        self.width = wid
        self.full = ful

    def __str__(self):
        return "%-8s %-8s %-8s %-8s %-8d %-8d %-8s" % \
            (self.smiley, self.cap, self.label, self.label_on, self.height, self.width, self.full)

def main():
    bottle_one = Bottle()
    print(bottle_one)

    bottle_two = Bottle("open", "blue", True, 10, 5, False)

    print(bottle_two)

if __name__ == "__main__":
    main()
