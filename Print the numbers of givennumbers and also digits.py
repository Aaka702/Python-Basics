n=int(input("enter the number"))
sum=0
print("Digits are")
while n>0:
    d=n%10
    n=n//10
    print(d)
    sum=sum+1
print("Number of digits",sum)