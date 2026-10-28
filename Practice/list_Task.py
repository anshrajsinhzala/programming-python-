# print("Select Data Type :  , 1) integer 2) Float ")
# data_type = int(input("choose Data type : "))
# if data_type == 1:
#     num1=int(input("Enter First Number : "))
#     num2=int(input("Enter Second Number : "))
# elif data_type == 2:
#     num1=float(input("Enter First Number : "))
#     num2=float(input("Enter Second Number : "))
# else: 
#     print("Invalid Data Type ")
#     exit()
# print("Choose Method :  , 1) Add 2) Substraction 3) Multiplication 4) division 5) Clear 6) Exit ")
# while True:
#     Method = int(input("Enter Number : "))
#     if Method == 1:
#         print("Addition = " ,num1 + num2 )
#     elif Method == 2:
#         print("Substraction = " ,num1 - num2 )
#     elif Method == 3:
#         print("Multiplication = " ,num1 * num2 )
#     elif Method == 4:
#         print("Divison = " ,num1 / num2 )
#     elif Method == 5:
#         num1=0
#         num2=0
#         print("Clear! Number are Reset to 0")
#     elif Method ==6:
#         print("Exit ",)
#         exit()
#     else:
#         print("Invalid Number")
#         exit()
#     break


######################################################################################################################
my_list=[10 , 20 , 30 , 40 ]
# print("How many number you want to add in list : , 1) one 2) two 3) three ")
# number=int(input("Enter a number of element: "))
# if number == 1:
#     num1=int(input("Enter number: "))
#     print(my_list)
# elif number == 2:
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second numbr: "))
#     print(my_list)
# elif number == 3:
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second numbr: "))
#     num3=int(input("Enter third number: "))
#     print(my_list)
# else:
#     print("Invalid Number")

while True:
    print("Menu: 1) Add(insert) 2)Delete(remove) 3)clear 4)Delete 5)length 6)Exit ")
    method = int(input("Select Method: "))
    if method == 1:
        value = input("Enter value: ")
        index = int(input("Enter index: "))

        my_list.insert(index , value)
        print("value inserted succesfully")
        print(my_list)
        exit()
    elif method == 2:
        index = int(input("Enter index to delete: "))

        if 0 <= index < len(my_list):
            del my_list[index]
            print("Value deleted successfully!")
            print(my_list)
        else:
            print("Invalid index!")
        exit()
    elif method == 3:
        my_list.clear()
        print(my_list)
        exit()
    elif method == 4:
        del my_list
        exit()
    elif method == 5:
        print("List Length:",len(my_list))
        exit()
    elif method == 6:
        exit()
    else:
        print("Invalid Number")
    break