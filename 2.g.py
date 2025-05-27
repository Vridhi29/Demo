T=float(input("Enter time in seconds:"))
Hour=T//3600
T=T%3600
Min=T//60
T=T%60
Sec=T
print("The given seconds areequivalent to ",Hour,":",Min,":",Sec)
