#pattern
'''
    * 
    * * 
    * * * 
    * * * * 
    * * * * *
    * * * *
    * * *
    * *
    *
'''
row = 5
for i in range(row):
    for j in range(i):
        print("*", end=' ')
    print('')
n = row
for i in range(row, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print("\r")