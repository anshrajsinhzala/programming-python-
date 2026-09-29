n1=int(input("Enter Number 1: "))
n2=int(input("Enter Number 2: "))
n3=int(input("Enter Number 3: "))

#n1=15200 n2=350 n3=1220
if n1>n2:
    if n1>n3:
        print(f"{n1} is greatest!!")

    else:
        print(n3,"is greatest!!")

else:
    if n2>n3:
        print("Number 2 is greatest!!")
    else:
        print("Number 3 is greatest!!")