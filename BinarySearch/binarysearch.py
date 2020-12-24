import random
import time

# Implementation of binary search algorithm!!

# We will prove that binary search is faster than naive search!


# Essence of binary search:
# If you have a sorted list and you want to search this array for something,
# You could go through each item in the list and ask, is this equal to what we're looking for?
# But we can make this *faster* by leveraging the fact that our array is sorted!
# Binary search ~ O(log(n)), naive search ~ O(n)

# In these two examples, l is a list in ascending order, and target is something that we're looking for
# Return -1 if not found


# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED


def binary_search(l, target, low=None, high=None):
    # example l = [1, 3, 5, 10, 12]  # should return
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif(target < l[midpoint]):
        return binary_search(l, target, low, midpoint-1)
    else:  # Target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)


if __name__ == "__main__":
    '''
    l=[1,3,5,10,12]
    target=10
    print(naive_search(l, target))
    print(binary_search(l, target))
    '''

    length = 10000
    # build a sorted list
    sorted_list = set()
    while len(sorted_list) < length:
        # Range of -30K to +30K
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search = (sorted_list, target)
    end = time.time()
    print(f"Naive search time: {(end-start)/length} seconds.")

    start = time.time()
    for target in sorted_list:
        binary_search = (sorted_list, target)
    end = time.time()
    print(f"Binary search time: {(end-start)/length} seconds.")
