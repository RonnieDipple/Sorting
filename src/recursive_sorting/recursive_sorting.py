# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(left_array, right_array):
    sorted_array = []  # created to put sorted elements in
    left_array_index = right_array_index = 0  # Both index's start at 0
    # added because I will be using array lengths often, can also use lists etc
    left_array_length, right_array_length = len(left_array), len(right_array)

    # A for loop with both array lengths combined to start it then
    for _ in range(left_array_length + right_array_length):
        # Checks which element from the start of each array is smaller
        if left_array_index < left_array_length and right_array_index < right_array_length:
            # If the element at the beginning of the left list is smaller, adds it
            # to the sorted array
            if left_array[left_array_index] <= right_array[right_array_index]:  # so if at index 0 in the left array
                # the element is smaller than the element at index 0 in the right array then
                # add it to the sorted array
                sorted_array.append(left_array[left_array_index])
                left_array_index += 1

            else:  # else add the element at index 0 from the right array to the sorted_array
                sorted_array.append(right_array[right_array_index])
                right_array_index += 1

        # once we reach the end of the of the left array, add the elements
        # from the right array
        elif left_array_index == left_array_length:
            sorted_array.append(right_array[right_array_index])
            right_array_index += 1

        # once we reach the end of the of the right array, add the elements
        # from the left array
        elif right_array_index == right_array_length:
            sorted_array.append(left_array[left_array_index])
            left_array_index += 1

    # returns a neatly sorted array that goes from smallest to largest
    # can easily reverse it by reversing the >

    return sorted_array


# implements the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # The setup
    left_array = []  # initialized with no elements because sorted elements will be placed here
    # and then combined with the right_array to form the complete sorted array
    # Pivot point
    mid = len(arr) // 2
    right_array = []
    # added because I will be using array lengths often, can also use lists etc
    left_array_index = right_array_index = 0  # Both index's start at 0
    left_array_length, right_array_length = len(left_array), len(right_array)

    # If the array or list is a single element return it as you can't sort a single element
    if len(arr) <= 1:
        return arr

    # sorts and merges each half,
    # this is where the recursion happens it keeps calling itself
    # splitting itself at the mid point
    left_array = merge_sort(arr[:mid])
    right_array = merge_sort(arr[mid:])

    #returns a sorted array which is the combination of both arrays
    return merge(left_array, right_array)

#time complexity of the Merge Sort algorithm is O(nlog(n)).


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    L = arr[start:mid]
    R = arr


    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
