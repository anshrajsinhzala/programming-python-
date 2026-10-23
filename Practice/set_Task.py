my_set = {10 , 20 , 30 , 40 }
print("Method: 1) Add 2)update 3)clear 4)Delete 5)length 6)Exit ")
method = int(input("Select Method: "))
if method == 1:
    value = (input("Enter value: "))

    my_set.add(value)
    print("value inserted succesfully")
    print(my_set)
elif method == 2:
    value = input("Enter Value: ")

    my_set.update([value])
    print("Updated Succesfully")
    print(my_set)
elif method == 3:
    my_set.clear()
    print(my_set)
elif method == 4:
    del my_set
elif method == 5:
    print("set Length:",len(my_set))
elif method == 6:
    exit()
else:
    print("Invalid Number")