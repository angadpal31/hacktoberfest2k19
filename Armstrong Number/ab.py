num=int(input("Enter the number to be checked for: "))
summ=0
for i in str(num):
    summ+=(int(i)**3)

if summ==num:
    print(" armstrong number")
else:
    print("isn't an armstrong number")
