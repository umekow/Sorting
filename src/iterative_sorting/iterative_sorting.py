# TO-DO: Complete the selection_sort() function below
"""
while i is less than or equal to len(list) - 1:
smallest_value = current value

check if smallest value is less than next value (index + 1)
    if true:
        move to next value
    if value is more than next value:
        smallest_value = next_value
    Repeat until end of list:
        swap indices
"""


def selection_sort(arr):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        cur_index = i
        next_index = cur_index + 1
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # how would i find the smallest value?

        if arr[cur_index] > arr[next_index]:
            smallest_index = next_index

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[
            cur_index]

    return arr


print(selection_sort([2, 3, 4, 1, 5]))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
