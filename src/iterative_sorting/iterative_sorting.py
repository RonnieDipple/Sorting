# TO-DO: Complete the selection_sort() function below
#Segments a list in to two parts one sorted and another unsorted
#Then we need to continously remove the smallest element from unsorted and append it to sorted
def selection_sort( arr ):
    # loop through n-1 elements
    answer = arr
    for i in range(0, len(arr) - 1):
        #cur_index = i
        smallest_index = i #This assumes i is the smallest so that on the next loop we can compare it to the next int
        # and sort accordingly
        # TO-DO: find next smallest element
        #for loop is always 1 ahead of the loop above
        for j in range(i + 1, len(arr)):
            #takes the int in position j which is 1 ahead of i and compares it to the smallest_index,
            # so to start smallest index is position 1 and J is position 2 and if J is smaller than
            # smallest_index make smallest index J if not then we already know smallest_index is the smallest
            # And don't need to do anything
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # (hint, can do in 3 loc)
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

        # Time Complexity > Selection Sort's time complexity is O(n^2)
    return arr


# TO-DO:  implement the Bubble Sort function below
#NEVER EVER USE THIS IN ANYTHING EVER LOL Jk if you perform **Bubble Sort** on an array that's already sorted,
#it will only require a single pass through the array, making its best-case performance linear.
#It's also very simple to implement.
def bubble_sort( arr ):

    #Set flag as true so we loop at least once
    flag = True

    while flag:
        flag = False
        for i in range(len(arr)-1):#Goes to the end
            if arr[i] > arr[i + 1]:# < this is where the terrible dark magic happens
            #it basically says if the number in the lower position is the larger number
            #when compared to the number in the higher position
            #swap it
                arr[i], arr[i + 1] = arr[i], arr[i + 1]
                flag = True

            # The algorithm runs in a while loop, only breaking when no items are swapped.
            # We set flag to True in the beginning to ensure that the algorithm runs at least once
            # Time Complexity > Bubble Sort's time complexity is O(n^2) time even if the array is sorted

    return arr


# STRETCH: implement the Count Sort function below
# Counting sort is a very efficient algorithm to sort a sequence of items,
# but all the items in the list must be non-negative integers.
def count_sort(arr):
    # Step 1
    # The first step in the implementation is to determine how many items of a particular value the input list has.
    # If it has 0 items it returns the array if not
    # We will initialize a temporary list called position and initialize each element to 0.
    # We will then iterate over the input list and increment the corresponding index in the position list for each item.
    if(len(arr) == 0):
        return arr

    n = len(arr)
    k = max(arr) + 1

    # initialize the position list
    position = [0] * k

    # check if an element in the array is 0 < if it is return error message else increment index v by 1
    for v in arr:
        if v < 0 :
            return "Error, negative numbers not allowed in Count Sort"
        position[v] += 1

    # Step 2
    # In the second step, for each item v in arr,
    # we determine how many items in the list are greater than v
    # and update the corresponding index that represents v in position list.

    s = 0
    for i in range(0, k):
        temp = position[i]
        position[i] = s
        s += temp
    # Step 3
    # In the final step, we place the items directly in it’s final sorted position
    # in the result list using the information in the position list. Initialize the result list by None

    result = [None] * n
    for v in arr:
        result[position[v]] = v
        position[v] += 1
    return result
