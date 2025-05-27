n = int(input("Enter the number of fruits in each set: "))
s1 = set()
print(f"Enter {n} fruits for set s1:")
for i in range(n):
    fruit = input()
    s1.add(fruit)

s2 = set()
print(f"Enter {n} fruits for set s2:")
for i in range(n):
    fruit = input()
    s2.add(fruit)

print("Fruits in both sets:", s1&s2)
print("Fruits only in s1:", s1-s2)
print("Count of all unique fruits:", len(s1|s2))
