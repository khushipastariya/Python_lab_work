qty=int(input("Write the quantity: "))
tent_cost= 100*qty
if tent_cost>=10000:
    print("Discounted cost is :", tent_cost*0.5)
else:
    print("Total cost is :",tent_cost)