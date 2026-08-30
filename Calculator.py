a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
print("Select operation: \n 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division \n 5: Modulus \n 6: Floor Division \n 7: Exponentiation")
o=int(input("Enter Choice:"))
if o==1:
    print(a+b)
elif o==2:
    print(a-b)
elif o==3:
    print(a*b)
elif o==4:
    print(a/b)
elif o==5:
    print(a%b)
elif o==6:
    print(a//b)
elif o==7:
    print(a**b)
else:
    print("Invalid response")