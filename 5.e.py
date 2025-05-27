num = int(input("Enter a number"))
r = 0
temp = num
while temp>0:
    r = r * 10 + (temp%10)
    temp = temp//10
if r==num:
    print("The number is a palindrome number",r)
else:
    print("The number is not a palindrome number",r)
