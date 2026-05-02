numb1 = int(input("chose your starting number"))
numb2 =   int(input("chose your ending number"))
for i in range (numb1,numb2+1):
    print (f"the even numbers between {numb1} and {numb2} are:")
    print(i%2)