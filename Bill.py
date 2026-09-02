p=float(input("Enter the cost: "))
d=float(input("Enter discount percentage: "))
b=p-((d/100)*p)
g=0.18*b
t=b+g
print(p)
print(d)
print(b)
print(g)
print(t)