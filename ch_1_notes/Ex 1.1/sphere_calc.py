""" To calculate the diameter, circumference
surface area, and volume of a circle and print
to the console """

from math import pi

def sphere_calc(radi):
    """ calculates and prints values """
    diameter = radi * 2
    circumference = diameter * pi
    area = 4 * pi * (radi ** 2)
    volume = (4/3) * pi * (radi ** 3)

    print(diameter)
    print(circumference)
    print(area)
    print(volume)

def main():
    """ main to test function """
    radius = float(input("Please provide the sphere radius: "))
    

    sphere_calc(radius)

if __name__ == "__main__":
    main()
