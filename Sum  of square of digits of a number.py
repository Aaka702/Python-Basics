n=int(input("enter the number"))
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d**2
print("sum of squares is",sum)