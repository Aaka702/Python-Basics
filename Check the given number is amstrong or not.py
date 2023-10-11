n=int(input("enter the number"))
num=n
i=0
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d**3
if num==sum:
    print("Angstrong number")
else:
    print("no an angsroting num")
