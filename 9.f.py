n = int(input("Enter the number of colors in each set: "))
s1 = set()
print(f"Enter {n} colors for set s1:")
for i in range(n):
    colors = input()
    s1.add(colors)
s2 = set()
print(f"Enter {n} colors for set s2:")
for i in range(n):
    colors = input()
    s2.add(colors)

print("colors in both sets:", s1&s2)
print("colors only in s1:", s1-s2)
print("colors only in s1:", s2-s1)
print("Count of all unique colors:", len(s1|s2))
