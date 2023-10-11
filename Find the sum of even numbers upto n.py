#find the sum of even numbers upto n
n=int(input("enter the number"))
sum=0
i=0
while i<=n:
    sum=sum+i
    i=i+2
print(sum)