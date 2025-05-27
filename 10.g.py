#Write a Python function with return
num = int(input("Enter a number : "))
def sumission(n):
    return sum(i**3 for i in range (1,n))
print(sumission(num))
