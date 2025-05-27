list = []
count = 0
n = int(input("Enter the number of Marks to be taken: "))

for i in range(n):
    marks = int(input(f"Enter Marks {i+1}: "))  
    count += marks
    list.append(marks)  

print("List:", list)
list.sort()
list.pop()
runnerup=list[n-2]
print("runner up is ",runnerup)
