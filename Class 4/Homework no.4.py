Totaldataused=int(input("how many giga bits did you use?"))
isprimeuser=input("are you a prime user?")
totalcost= 300
if Totaldataused > 5:
    totalcost = totalcost+50
elif isprimeuser == "yes":
    totalcost = totalcost+50*0.1
print(f"you total is {totalcost}")