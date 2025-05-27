#Write a Python function without return
that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
num=int(input("Enter a number"))
def sumission(a):
    total =  sum(i**3 for i in range(1, a))
    print (total)
sumission(num)
