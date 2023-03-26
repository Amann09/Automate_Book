# The Collatz Sequence
""" Write a function named collatz() that has one parameter named number. If number is even, 
then collatz() should print number // 2 and return this value. If number is odd, then collatz() 
should print and return 3 * number + 1. Then write a program that lets the user type in an integer 
and that keeps calling collatz() on that number until the function returns the value 1.
For more information.. Check out page no. 77 of the book.
"""
def collatz(number): # Defining the function
    # Checking the odd or even
    if number%2 == 0:
        return number // 2
    else:
        return 3 * number + 1
        
# Taking the input from the user
n = int(input("Enter the number: "))

l = [] # Creating an empty list
l.append(collatz(n))

print(collatz(n)) # Printing the first function call number/return value.
while True:
    if l[-1] == 1:
        break
    else:
        print(collatz(l[-1])) # Calling the function with next number
        l.append(collatz(l[-1]))

# try:
#     n = int(input("Enter the number: "))
# except ValueError:
#     print("Error: Please enter an integer")