""" Uses a binary function to located a target. """

def binary_search(target, sorted_lyst):
    """ Uses binary search to locate a target in a sorted list. """
    left = 0
    right = len(sorted_lyst) - 1

    while left <= right:
        midpoint = (left + right) // 2

        if target == sorted_lyst[midpoint]:
            return midpoint
        elif target < sorted_lyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

def main():
    """ Main driver to test funtion. """
    sorted_lyst = ["Amanda", "Annika", "Caleb", "Christina", "Dan", "Karen", "Kim", "Matthew", "Nona", "Ricky", "Robby", "Shauna", "Tiffany", "Tom", "Vila"]
    print(binary_search("Robby", sorted_lyst))

if __name__ == "__main__":
    main()
