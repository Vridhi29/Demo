import math
import cmath
a=int( input("Enter a number: "))
b=int( input("Enter a number: "))
c=int( input("Enter a number: "))
D =b**2-4*a*c
if D==0:
    print("The roots are real")
    print("The real root is",(-b)/(2*a))
elif D>0:
     print("There are 2 real solutions")
     print("The first real root is", -((b+math.sqrt(D))/(2*a)))
     print("The first real root is", -((b-math.sqrt(D))/(2*a)))
else :
     print("The roots are imaginary")
     print("The first real root is", ((b+cmath.sqrt(D))/(2*a)))
     print("The first real root is", (-b-cmath.sqrt(D))/(2*a))
