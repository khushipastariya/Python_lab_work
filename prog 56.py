# 7 and 9 multiples
nl=[]
for x in range(100, 500):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))
