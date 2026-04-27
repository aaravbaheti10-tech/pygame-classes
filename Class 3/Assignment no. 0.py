price=int(input("what was the price?"))
member=(input("do you have a membership with us?"))
if price > 1000:
    price = price-price*0.1
if member == "yes" or "Yes":
    price = price - price*0.05
print ("your total is",price)