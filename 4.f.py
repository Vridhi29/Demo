name = input("Name: ")
Roll_number = input("Roll Number: ")
Sap_ID = input("Sap Id: ")
Course = input("Course")
sem = input("Sem: ")
subject_name = input("Subject Name: ")

PDS = int(input("PDS: "))
PYTHON = int(input("PYTHON: "))
CHEM = int(input("Chemistry: "))
ENG = int(input("English: "))
PHYSICS = int(input("Physics: "))
    
Total = PDS + PYTHON + CHEM + ENG + PHYSICS
Percentage = (Total / 500) * 100
CGPA = Percentage / 10


if 0 <= CGPA <= 3.4:
        grade = "F"
elif 3.5 <= CGPA <= 5.0:
        grade = "C+"
elif 5.1 <= CGPA <= 6.0:
        grade = "B"
elif 6.1 <= CGPA <= 7.0:
        grade = "B+"
elif 7.1 <= CGPA <= 8.0:
        grade = "A"
elif 8.1 <= CGPA <= 9.0:
        grade = "A+"
elif 9.1 <= CGPA <= 10.0:
        grade = "O"
else:
        grade = "Invalid CGPA"

    
print(f"Name: {name}")
print(f"Roll Number: {Roll_number}\t\tSap Id: {Sap_ID}")
print(f"Semester:    {sem}  \tCourse: {Course}")
print(f"Subject Name: {subject_name}")
print(f"Total Marks: {Total}/500")
print(f"Percentage: {Percentage:.2f}%")
print(f"CGPA: {CGPA:.2f}")
print(f"Grade: {grade}")



