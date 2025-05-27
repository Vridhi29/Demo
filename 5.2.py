num = int(input("Enter a number to check if it is an Armstrong number: "))
num_of_digits = len(str(num))
sum_of_powers = sum(int(digit) ** num_of_digits for digit in str(num))

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
