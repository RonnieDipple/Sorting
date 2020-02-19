# STRETCH: implement Linear Search				
def linear_search(lys, element):
    for i in range(len(lys)):
        if lys[i] == element:
            return i
    return -1


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, x, l, r):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursive(arr, l, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1
