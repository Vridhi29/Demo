names = ["alice","bob","eve","charlie","oscar","Vridhi","Jain","Jiya"]
file_path = "file.txt"
with open(file_path,"w") as file:
    for name in names:
        file.write(name + "\n")
vowels = {'A','E','I','O','U'}
name_count = 0
vowel_start_count = 0
longest_name = ""

with open(file_path,"r") as file:
    for line in file:
        name = line.strip()
        name_count+=1
        if name[0].upper() in vowels:
            vowel_start_count +=1
        if len(name)>len(longest_name):
            longest_name = name

print("total number of names",name_count)
print("number of names starting with a vowel",vowel_start_count)
print("longest name: ",longest_name)