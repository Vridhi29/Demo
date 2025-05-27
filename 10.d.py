#Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
a=int(input("Enter a number"))
def sumission(n):
    if n <= 1:
        return 0
    return sum(i**3 for i in range(1, n))
print(sumission(a))
