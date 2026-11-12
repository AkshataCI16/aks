value = input("Enter number or string: ")

if value == value[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")