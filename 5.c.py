num=int(input("Enter a number"))
a = 0
b = 1
print(a)
print(b)
for i in range (0,num-2):
  c = a + b
  a = b
  b = c
  print(c)
