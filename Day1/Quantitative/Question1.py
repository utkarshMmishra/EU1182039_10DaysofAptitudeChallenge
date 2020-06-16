for i in range(250,351):
	if i%2==1  and i%3==1 and i%4==1 and (i%5==1 or i%6==1):
		if i%7 == 0:
			num = str(i)
			print("Number :",int(i))

sum = 0
for i in num:
	sum = sum+int(i)
print("Sum :",sum)


