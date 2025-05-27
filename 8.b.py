Input = input("Enter any name: ")
vowels = "aeiou"
count = 0
for i in Input.lower():  
    if i in vowels:
        count+= 1
print(f"{count} vowels found")
