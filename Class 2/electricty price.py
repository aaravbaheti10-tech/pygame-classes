#assignmet no.3
unit=int(input("how many units have you used:"))
price=0
if unit < 100:
    price= unit * 5
elif unit <200:
    price=  100*5 + (unit-100)* 7
elif unit > 200:
    price = 100*5 + 100*7 + (unit-200)*10
print("each unit will cost:",price/unit)
print ("the price is:",price)