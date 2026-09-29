"""
Conditional Satments

When our Programme Goes on multiple ways it is called Conditional Statement

3) Types

1) normal if/else
2) ladder if/else
3) nested if/else
"""

age=int(input("Enter Age: "))

if(age>100):
    print("Invalid age!!")

elif (age>=18):
    print("Eligible for vote")

else:
    print("NOt Elible FOr Vote")

a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2: "))

if(a>b):
    print("a is greater than b")

else:
    print("b is greater than a")