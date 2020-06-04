###############################################################################
# Program to find an element in a given list using bisection search           #
# through RECURSION                                                           #
###############################################################################

array = [1, 2, 3, 4, 5, 6]

def find_num(array, k):
    mid_index = len(array)//2
    if array[mid_index] == k:
        return True
    elif len(array) == 1:
        return False
    if array[mid_index] > k:
        array = array[0 : mid_index ]
        return find_num(array, k)
    else:
        array = array[mid_index : ]
        return find_num(array, k)

print(find_num(array, 10))
