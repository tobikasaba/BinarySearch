# Implementation of binary search algorithm!!

# We will prove that binary search is faster than naive search!

# naive search:
# scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1


def naive_seacrch(l, target):
    sorted_list = sorted(l)
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def naive_seacrch_b(l, target):
    # using just i puts the value of i, and the corresponding value in a tupple
    # using i and j, creates individual values for both
    sorted_list = sorted(l)
    for i, j in enumerate(l):
        if j == target:
            return i
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our klist is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    # example list = [1, 3, 5, 10, 12] | should return 3 the index of 10
    sorted_list = sorted(l)
    mid_point = (low + high) // 2

    if l[mid_point] == target:
        return mid_point
    elif l[mid_point] > target:
        return (binary_search(l, target, low, mid_point-1))
    else:
        # l[mid_point] < target
        return binary_search(l, target, mid_point+1, high)

    print(sorted_list[:mid_point])


if __name__ == "__main__":
    l = [1, 3, 5, 10, 12]
    target = 10

    print(f"Naive search function produced: {naive_seacrch(l, target)}")
    print(f"Naive search function b produced: {naive_seacrch_b(l, target)}")
    print(f"Binary search produced: {binary_search(l, target)}")
