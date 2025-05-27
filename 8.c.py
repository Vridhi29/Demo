#Create a dictionary of n persons where key is name and value is city.  
#a) Display all names 
#b) Display all city names 
#c) Display student name and city of all students. 
#d) Count number of students in each city.
Person = {}
n = int(input("Enter the number of Persons: "))
for i in range(n):
    name = input("Enter Person name: ")
    city = input("Enter city name: ")
    Person[name] = city

print("All Names:",Person.keys())
print("All Cities:",Person.values())
print("Person and their Cities:")
for name, city in Person.items():
    print(f"{name}: {city}")
    
city_counts={}
for city in Person.values():
    if city in city_counts:
        city_counts[city]+=1
    else:
        city_counts[city]=1
print("Person Count in Each City:",city_counts)







