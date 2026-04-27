#assignment no.1
mathgrade=int(input("what is your math grade?"))
scigrade=int(input("what is your science grade?"))
Englishgrade=int(input("what is your English grade?"))
totalgrade= mathgrade + scigrade + Englishgrade
averagegrade= totalgrade/3
print("your total grade is:",totalgrade)
print("the averge of your grade is:",averagegrade)
#------------------------------------------------------------

#----------------------------------------------------------- 

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
mgrade= int(input("what is your math grade?"))
biograde=int(input("whaat is your bio grade?"))
litrgade=int(input("what is your english grade?"))
totalgrade= mgrade+biograde+litrgade
avggrade= totalgrade/3
if avggrade<= 100 or avggrade>=90:
    print("you got an A!")
elif avggrade <90 or avggrade >=75:
    print ("you got an B!")
elif avggrade <75 or avggrade >= 50:
    print("you got a C")
elif avggrade <50:
    print("you have failed")