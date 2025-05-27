class Student:
    def _init_(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks (Physics, Chemistry, Maths):", self.marks)

students = []
for i in range(3):
    name = input("Enter student name: ")
    sap_id = input("Enter student SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))
    marks = [phy,chem,maths]

    student = Student(name, sap_id, marks)  
    students.append(student)


print("\nDetails\n:")
for student in students:
    student.display_details()