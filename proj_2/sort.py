from random import seed, sample
from recursioncounter import RecursionCounter

def selection_sort(lyst):
    if not isinstance(lyst, list):
        raise ValueError("Provided list must be of list type.")

    lyst_copy = lyst
    pos = 0
    length = len(lyst_copy)

    while pos != length:
        for rep in range(0, length):
            if lyst_copy[pos] < lyst_copy[rep]:
                temp = lyst_copy[rep]
                lyst_copy[rep] = lyst_copy[pos]
                lyst_copy[pos] = temp
        pos += 1

    return lyst_copy

def insertion_sort(lyst):
    if not isinstance(lyst, list):
        raise ValueError("Provided list must be of list type.")

    lyst_copy = [lyst[0]]
    length = len(lyst)
    copy_length = len(lyst_copy)
    pos = 1

    while pos < length:
        for rep in range(copy_length):
            if lyst[pos] == lyst_copy[rep]:
                lyst_copy.insert(rep, lyst[pos])
                copy_length = len(lyst_copy)
                break
            elif lyst[pos] < lyst_copy[rep]:
                lyst_copy.insert(rep, lyst[pos])
                copy_length = len(lyst_copy)
                break
        if lyst[pos] > lyst_copy[-1]:
            lyst_copy.append(lyst[pos])
            copy_length = len(lyst_copy)
        pos += 1

    return lyst_copy



def mergesort(lyst):
    if not isinstance(lyst, list):
        raise ValueError("Provided list must be of list type.")

    lyst_copy = []
    count = range(0, len(lyst) - 1)
    mergesort_helper(lyst, lyst_copy, count, 0, len(lyst))
    
    return lyst_copy

def mergesort_helper(lyst, lyst_copy, count, low, high):
    RecursionCounter()

    if len(count) == 1:

    else:
        mid = (count[0] + len(count) - 1) // 2
        
        mergesort_helper(lyst, lyst_copy, range(mid + 1, high), low, high)
        mergesort_helper(lyst, lyst_copy, range(low, mid), low, high)



#def quicksort(lyst):
#    if not isinstance(lyst, list):
#        raise ValueError("Provided list must be of list type.")

#    RecursionCounter()

#def is_sorted(lyst):


def main():
    test_val = 10
    val_range = range(0, test_val)
    #seed(3)
    test_array = sample(val_range, k=test_val)

    print(test_array)
    print(mergesort(test_array))

if __name__ == "__main__":
    main()
