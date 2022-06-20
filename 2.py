# Python program to add all the array elements
lst = []
num = int(input("Enter the size of the array: "))

for n in range(num):
    numbers = int(input())
    lst.append(numbers)
print("Sum:", sum(lst))
