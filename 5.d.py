num = int(input("Enter a number"))
A = True
for i in range (2,num):
    if num % i==0:
        A = False
        break
if A == True:
      print("The number is a prime number")
else:
    print("The number is not a prime number")

