a= list(input("Enter the list elements : "))
b= int(input("Enter the no. to check : "))
print(all(c>=b for c in a))