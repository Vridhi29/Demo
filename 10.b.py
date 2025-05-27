#function using paramaters to find the maximum and minimum number in the sequence
def max_min(*numbers):
    max_num = min_num = numbers[0]  

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num
max_num, min_num = max_min(0, 1, 2, 3, 4, 5, 6, 7, 8)
print(f"The maximum number is {max_num}")
print(f"The minimum number is {min_num}")
