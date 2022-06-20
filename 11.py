# Iterative Binary Search Function method Python Implementation
# It returns index of n in given list1 if present,
# else returns -1
def binary_search(lst, n):
    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:
        # for get integer result
        mid = (high + low) // 2

        # Check if n is present at mid
        if lst[mid] < n:
            low = mid + 1

            # If n is greater, compare to the right of mid
        elif lst[mid] > n:
            high = mid - 1

            # If n is smaller, compared to the left of mid
        else:
            return mid

            # element was not present in the list, return -1
    return -1


# Initial list1
# list1 = [12, 24, 32, 39, 45, 50, 54]
# n = 45
# m = int(input("Enter the number of elements in the array: "))
# arr = []
#
# for i in range(m):
#     numbers = int(input("enter the Value:"))
#     list1 = arr.append(numbers)
#
# n = int(input())

# creating an empty list
lst = []

# number of elements as input
m = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, m):
    ele = int(input())

    lst.append(ele)  # adding the element

n = int(input())

# Function call
result = binary_search(lst, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")
