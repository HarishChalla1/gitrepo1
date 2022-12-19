'''a=200
b=200
if a>b:
    print(a ," is big")
elif b>a:
    print(b," is big")


else:
    print("both are equal")'''


marks=eval(input("enter total marks"))
if marks>100:
    print("out of range marks")
elif marks>90:
    print("A grade")

elif marks>80:
    print("B grade")
elif marks>50:
    print("C grade")

else:
    print("FAIL")
    
