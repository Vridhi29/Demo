#function using paramaters to find the maximum and minimum number in the sequence
def max_min(numbers):
    max_num=numbers[0]
    min_num=numbers[0]
    for num in numbers:
        if num > max_num:
         max_num = num
        if num < min_num:
         min_num = num
    print("The maximum number in the sequence of list is:",max_num)
    print("The minimum number in the sequence of list is:",min_num)
max_min(numbers=[0,1,2,3,4,5,6,7,8,9])


