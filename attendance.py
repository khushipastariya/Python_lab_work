a=int(input("Number of classes held:"))
b=int(input("Number of classes attended:"))

percent=b/a*100

if percent>=80:
    print("The student is allowed to sit in the exam hall")
else:
    print("The student is not allowed to sit in the exam hall")



