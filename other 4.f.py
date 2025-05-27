
name=input("enter your name:")

roll=input("enter your Roll number:")

sem=input("enter your sem:")

sap=input("enter your sap id:")

course=input("enter your course  :")

a = int(input("enter the marks of PDS subject"))
b = int(input("enter the marks of Python subject"))
c = int(input("enter the marks of Chemistry subject"))
d = int(input("enter the marks of English subject"))
e = int(input("enter the marks of Physics subject"))


percentage = ((a+b+c+d+e)/500)*100

print("your overall percentage: ",percentage)

CGPA = percentage /10

print ("your CGPA is : ",(CGPA))

  
if(CGPA>=9.1):
    print("grade = outstanding")
elif(CGPA>=8.1):
    print("grade = A+")
elif(CGPA>=7.1):
    print("grade = A")
elif(CGPA>=6.1):
    print("grade = B+")
elif(CGPA>=5.1):
    print("grade = B")
elif(CGPA>=3.5):
    print("grade = C+")
else:
    print("grade = F")



print("\nSample Gradesheet")
print(f"Name: {name}")
print(f"Roll Number: {roll}\t\tSAPID: {sap}")
print(f"Sem: 1\t\t        Course: {course}")
print("\nSubject name:\tMarks")
print(f"PDS:\t\t{a}")
print(f"Python:\t\t{b}")
print(f"Chemistry:\t{c}")
print(f"English:\t{d}")
print(f"Physics:\t{e}")
print(f"\nPercentage:\t{percentage:}")
print(f"CGPA:\t\t{CGPA}")

