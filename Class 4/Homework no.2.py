ticket=200
personage=int(input("what is your age?"))
Personsudent=(input("are you a student?"))
studentdiscount=0
agediscount=0
if personage<12:
    agediscount=ticket/2
if Personsudent == "yes":
    studentdiscount=ticket*0.2
finalprice=agediscount-studentdiscount
print (f"your total is {finalprice}")