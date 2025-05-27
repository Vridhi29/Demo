list = []
count = 0
n = int(input("Enter the number of Marks to be taken: "))

for i in range(n):
    marks = int(input(f"Enter Marks {i+1}: "))  
    count += marks
    list.append(marks)  

print("List:", list)
average = count/n
tuple1 = tuple(list)
print(f"Average Marks is {average}")
