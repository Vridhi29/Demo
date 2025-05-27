a = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    a.append(element)

print("List:", a)

Unique=list(set(a))
print("Unique:",Unique)

for element in Unique:
    count=a.count(element)
    print(f"Count of '{element}': {count}")
    
