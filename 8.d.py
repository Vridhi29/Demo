Student = {}
n = int(input("Enter the number of Student: "))
for i in range(n):
    name = input("Enter Student's name: ")
    Course=input("Enter Student's course name: ")
    Age = int(input("Enter Student's age : "))
    Marks = int(input("Enter Student's Marks: "))
    Student[name] = {"Age":Age,"Marks":Marks,"Course":Course}
print("All Names:",Student.keys())
print("Values:",Student.values())
print(Student.get("Marks"))
