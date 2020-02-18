# [5 9 3 7 2 8 1 6]

# [3 2 1][5][9 7 8 6]

# [2 1][3][][5][7 8 6][9][]

# [1][2][3][5] [6][7][8] [9]

# Decide on base case
# base case is []

# Find the pivot point

# partition our data to the left and right of the pivot
# left -> smaller than pivot, right -> larger than pivot
# What if they're the same size as the pivot? Just pick one?  >=

# repeat, recurse

my_list = [5, 9, 3, 7, 2, 8, 1, 6]



def partition(data):
    left = []
    pivot = data[0]
    right = []

    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

        return left, pivot, right

def quicksort(data):
    if data == []:
        return data
    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(my_list))

# print(5 in my_list)

# def is_it_in_here(n):
#     for item in my_list:
#         if item == n:
#             return True
#     else:
#         return False

