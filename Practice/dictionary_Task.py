my_dictionary = {"id":"1" ,"name":"Zala","email":"abc@123"}
print("Choose Method :  , 1) Add 2) Remove 3) Update 4) Clear 5) Delete ")

choice = int(input("Enter Number: "))

if choice == 1:
    key = input("Enter New Key: ")
    value = input("Enter New Value: ")
    my_dictionary[key]=value
    print(f'Updated Dictionary: {my_dictionary}')

elif choice == 2:
    key = input("Enter Key: ")
    if key in my_dictionary:
        remove = my_dictionary.pop(key)
        print(f'removed item: {remove}')
        print(f'updated dictionary: {my_dictionary}')
    else :
        print("Invalid Key")

elif choice == 3:
    key = input("Enter Key: ")
    if key in my_dictionary:
        value = input("Enter New Value: ")
        my_dictionary[key] = value
        print(f'updated Dictionary: {my_dictionary}')
    else:
        print("Invalid key")

elif choice == 4:
    my_dictionary.clear()
    print(f'Dictionary Clear Succesfully: {my_dictionary}')

elif choice == 5:
    del my_dictionary
    print(f'Dictionary Deleted Succesfully')

else:
    print("Invalid Choice")