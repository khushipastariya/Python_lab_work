
a = int(input('Enter The Amount Of Units Consumed:'))

if a <= 50:
    amt = a*0.50
    print('Amount To Be Paid Is:',amt)

elif a <= 150 and a > 50:
    amt = (50*0.5) + ((a-50)*0.75)
    print('Amount To Be Paid Is:',amt)

elif a <= 250 and a > 150:
    amt = (50*0.5) + (100*0.75) + ((a-150)*1.2)
    print('Amount To Be Paid Is:',amt)

else:
    amt = (50*0.5) + (100*0.75) + (100*1.2) + ((a-250)*1.5)
    print('Amount To Be Paid Is:',amt)



