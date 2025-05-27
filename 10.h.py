# Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
n=int(input("Enter a number"))
def num(n):
    if n==0:
        return
    num(n-1)
    print(n)
num(n)

  
