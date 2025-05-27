def max_min(**number):
    numbers=list(number.values())
    max_num=numbers[0]
    min_num=numbers[0]
    for num in numbers:
        if num > max_num:
         max_num = num
        if num < min_num:
         min_num = num
    print("The maximum number in the sequence of list is:",max_num)
    print("The minimum number in the sequence of list is:",min_num)
max_min(a=0,b=1,c=2,d=3,e=4,f=5,g=6,h=7,i=8,j=9)

