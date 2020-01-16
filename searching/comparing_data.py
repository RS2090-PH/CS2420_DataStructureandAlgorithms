""" Program to show how to assign class methods to allow class object comparisons. """

class SavingsAccount(object):
    """ This class represents a savings account
    with the owner's name, PIN, and balance. """

    def __init__(self, name, pin, balance = 0.0):
        """ Initializes any class objects made. """
        self.name = name
        self.pin = pin
        self.balance = balance

    def __eq__(self, other): 
        """ If == is used to compare two of these objects, this function is called """
        return self.name == other.name

    def __lt__(self, other):
        """ If < is used to compare two of these objects, this function is called """
        return self.name < other.name

    def __gt__(self, other):
        """ If > is used to compare two of these objects, this function is called """

        return self.name > other.name

def main():
    """ Main driver to test class/funtions. """
    sav_1 = SavingsAccount("Ken", 1000, 0)
    sav_2 = SavingsAccount("Bill", 1001, 30)

    print(sav_1 < sav_2)

if __name__ == "__main__":
    main()
