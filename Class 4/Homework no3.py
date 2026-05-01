unitsbought = int(input("how many units did you buy?"))
price = 0
if unitsbought < 100:
    price = unitsbought*5
elif unitsbought < 300:
    price = unitsbought*5 +(unitsbought -100 )* 7
elif unitsbought > 300:
    price = unitsbought*5 + unitsbought*7 +(unitsbought - 200)*10
if price > 1500:
    price = price + price*0.08
print ("your total is:",price)