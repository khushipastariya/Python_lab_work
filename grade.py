Phy=int(input("Enter Physics marks out of 100 :"))
Chem=int(input("Enter Chemistry marks out of 100 :"))
Bio=int(input("Enter Biology marks out of 100 :"))
Math=int(input("Enter Mathemetics marks out of 100 :"))
Comp=int(input("Enter Computer marks out of 100 :"))
Percentage = (Phy+Chem+Bio+Math+Comp)/5
print("Percentage: ",Percentage)
if Percentage>=90:
    print("GRADE A")
elif Percentage>=80:
    print("GRADE B")
elif Percentage>=70:
    print("GRADE C")
elif Percentage>=60:
    print("GRADE D")
elif Percentage>=40:
    print("GRADE E")
elif Percentage<40:
    print("GRADE F")