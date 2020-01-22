""" To show funtionality of the insertion sort algorithm. """
from swap import swap

def insertion_sort(lyst):
    """  """
    i = 1

    while i < len(lyst):
        item_to_insert = lyst[i]
        j = i - 1

        while j >= 0:
            if item_to_insert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = item_to_insert
        i += 1

def main():
    """ Main driver to test function. """
    lyst = [6, 2, 4, 1, 8, 3, 5, 7, 9]

    print(lyst)
    insertion_sort(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
def insertion_sort(lyst, left, right):
    held = lyst[0]

    while i < len(lyst):
        item_to_insert = lyst[i]
        j = i - 1

        while j >= 0:
            if item_to_insert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = item_to_insert
        i += 1
        
        
    held[0] = lyst[0]
    temp = 1
    while left < right:
        if held[0] > lyst[temp]:
            held.append(lyst[temp])
            
        
        
        
        
        left += 1
        
        
        
def insertion_sort(lyst):
    i = 1

    while i < len(lyst):
        item_to_insert = lyst[i]
        j = i - 1

        while j >= 0:
            if item_to_insert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = item_to_insert
        i += 1