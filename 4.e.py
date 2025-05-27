Date=int(input("Enter the Date(1-31):"))
Month=int(input("Enter the Month(1-12):"))
Year=int(input("Enter the Year(e.g., 2023):"))
print("The Date is:", Date,"/",Month,"/",Year)

if Month==1 or Month==3 or Month==5 or Month==7 or Month==9 or Month==11:
     Days=31
elif Month==4 or Month==6 or Month==8 or Month==10 or Month==12:
     Days=30
else:
     Days=28

if Date<Days:
     Date=Date+1
     print("Date") 

if Date > Days:
    Date = 1
    Month += 1

if Month > 12:
    Month = 1
    Year += 1
    
print("The Next Date is:", Date,"/",Month,"/",Year)
