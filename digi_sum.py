a = 143
sum = 0
while (a != 0):
    sum = sum + int(a % 10)
    a = int(a/10)

print("sum of digits of a given number = " ,sum)

