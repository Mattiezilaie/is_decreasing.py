# Author: Mahtab Zilaie
# Date: February 10, 2020
# Description: function takes a list and returns True if list is decreasing or False if not

def rec_is_decreasing(lst, i):
    """helper function takes list and index to determine if list is decreasing"""

    if (len(lst) - 1) == i:     # if last index is equal  to 0 return true
        return True

    if lst[i] <= lst[i+1]:   # if value in index i is less than/equal to value in index i+1 this is False
        return False

    return rec_is_decreasing(lst, i+1)  # list, add 1 to index


def is_decreasing(lst):

    """function takes helper function and only uses list sets variables"""

    return rec_is_decreasing(lst, i=0) # list, index set to 0

# 4, 3, 2
# (4, 3) = true
# (3, 2) = true
# (1, 2) = false
# (2, 5) = false
# (5, 4) = true
#
# [4, 3, 5]
#
# rec_is_decreasing(lst, 0) = rec_is_decreasing(lst, 1) = rec_is_decreasing(lst, 2)

#print(rec_is_decreasing([1, 2, 4], 0))
#print(rec_is_decreasing([6, 3, 1], 0))