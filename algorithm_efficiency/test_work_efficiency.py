""" To compare the work efficiency of n ** 4 and 2 ** n """

def alg_rep():
    """ creates creates comparison functions and loops them to compare results """

    def alg_a(value):
        """ calculates n ** 4 """
        answer = value ** 4
        return answer

    def alg_b(value):
        """ calculates 2 ** n """
        answer = 2 ** value
        return answer

    for rep in range(1, 20):
        if (alg_a(rep)) == (alg_b(rep)):
            print("A - %-7d%7d - B     Equal Work     Line:%2d" % (alg_a(rep), alg_b(rep), rep))
        elif (alg_a(rep)) < (alg_b(rep)):
            print("A - %-7d%7d - B    A Efficient     Line:%2d" % (alg_a(rep), alg_b(rep), rep))
        elif (alg_a(rep)) > (alg_b(rep)):
            print("A - %-7d%7d - B    B Efficient     Line:%2d" % (alg_a(rep), alg_b(rep), rep))

def main():
    """ main driver to test comparison function """
    alg_rep()

if __name__ == "__main__":
    main()
