#Write a Python function without parameter that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
a=int(input("Enter a number"))
def sumission():
    return sum(i**3 for i in range(1, a))
print(sumission())






