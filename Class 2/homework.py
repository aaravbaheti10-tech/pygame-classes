#assignment no.1
mathgrade=int(input("what is your math grade?"))
scigrade=int(input("what is your science grade?"))
Englishgrade=int(input("what is your English grade?"))
totalgrade= mathgrade + scigrade + Englishgrade
averagegrade= totalgrade/3
print("your total grade is:",totalgrade)
print("the averge of your grade is:",averagegrade)
#------------------------------------------------------------
#assignment no.2
principal=int(input("what is the amount?"))
rate=int(input("what is the rate of intrest?"))
time=int(input("how long is it?"))
total=principal*rate*time/100
print("your total is:",total)
#----------------------------------------------------------- 
#assignmet no.3
unit=int(input("how many units have you used:"))
price=0
if unit < 100:
    price= unit * 5
elif unit <200:
    price= unit* 7
elif unit > 200:
    price = unit* 10
print("each unit will cost:",price/unit)
print ("the price is:",price)
#----------------------------------------------------------
#assignment no.4
number=int(input("which number would you like to check?"))
if number%2 ==1:
    print(number,"is odd")
else:
    print(number,"is even")
#----------------------------------------------------------
#assignment no.5
number2=int(input("what number would you like to check?"))
square=number2**2
cubed=number2**3
print(square,"is your number squared")
print(cubed,"is your number cubed")
#----------------------------------------------------------
#bonus challenge
grade=int(input("enter your grade:"))
if grade >90:
    print("you got an A!")
elif grade > 75:
    print("you got a B!")
elif grade > 50:
    print("you got a C")
elif grade < 50:
    print("you have failed")