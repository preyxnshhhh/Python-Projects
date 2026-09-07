c=input("1. USD to INR \n2. INR to USD :")
f=float(input("Enter amt :"))
if (c=="1"):
    e=f*100
elif (c=="2"):
    e=f/100
else:
    print("Invalid choice")
print("After conversion : ",e)