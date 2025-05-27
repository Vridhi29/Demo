#Write a recursive function to print Fibonacci series upto n terms.
num=int(input("Number:"))
        
def fibo(num, a=0, b=1):
    if num > 0:
        print(a)
        fibo(num - 1, b, a + b)
fibo(num)
    

