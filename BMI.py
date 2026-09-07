w=float(input("Enter weight in kg :"))
h=float(input("Enter height in meter :"))
s=h*h
bmi=w/s
print(bmi)
if (bmi<18.5):
    print("Underweight")
elif(18.5<bmi<24.9):
    print("Normal weight")
elif(25<bmi<29.9):
    print("Over weight")
else:
    print("Obesity")