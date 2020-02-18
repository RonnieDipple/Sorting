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


# STRETCH: implement an in-place merge sort algorithm # Reference https://www.geeksforgeeks.org/in-place-merge-sort/
def merge_in_place(arr, start, mid, end):

    start2 = mid + 1

    # If the array is already sorted
    if (arr[mid] <= arr[start2]):
        return arr

    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1

    return arr


# l is for left index and r is right index of the
# sub array of arr aka array to be sorted
def merge_sort_in_place(arr, l, r):
    if l < r:

        m = l + (r - l) // 2 # m = left + (right minus left) divided by two

        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# This ones better https://www.codespeedy.com/timsort-algorithm-implementation-in-python/
minrun = 32


def InsSort(arr, start, end):
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


def merge(arr, start, mid, end):
    if mid == end:
        return arr
    first = arr[start:mid + 1]
    last = arr[mid + 1:end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def TimSort(arr):
    n = len(arr)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = InsSort(arr, start, end)

    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr
