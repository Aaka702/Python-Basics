#print the number of digits in a given number and also print the digits

n=int(input("enter the number"))
count=0
print("the digits are")
while n>0:
    d=n%10
    n=n//10
    count=count+1
    print(d)
print("number of digits",count)


