# Python program to check if a string is palindrome or not

st = input("Enter a string:")

if st == st[:: - 1]:
   print("Palindrome")
else:
   print("Not Palindrome")
