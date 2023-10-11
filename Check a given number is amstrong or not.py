n=int(input("enter the number"))
sum=0
num=n
while n>0:
    d=n%10
    n=n//10
    sum=sum+d**3
if num==sum:
    print("it is an amstrong number")
else:
    print("it is not an amstrong number")