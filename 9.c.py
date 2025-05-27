Input = input("Enter any name: ").upper()
unique = set(Input)
count=0
sort = sorted(unique)
for i in sort:  
    if i.isalpha():
        count=Input.count(i) 
        print(f"countof {i}: {count}")





