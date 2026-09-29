i=1
ev=0
od=0
evsum=0
odsum=0
sum=0

while(i <= 5):
    n=int(input("Enter Number :  "))

    if(n%2==0):
       print("Number is Even")
       ev=ev + 1
       evsum=evsum + n
    else:
        print("Number is odd")
        od=od+1
        odsum=odsum+n
    sum=sum+n
    i= i + 1

# sum=sum+n
# i = i + 1

print("Even Number are ",ev)
print("Even Number sum are ",evsum)
print("Odd Number are ",od)
print("Odd Number sum are ",odsum)
print("Totalsum is ",sum)