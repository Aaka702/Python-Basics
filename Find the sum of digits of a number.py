#find the sum of digits of a number
# n=int(input("enter the number"))
# sum=0
# while n>0:
#     d=n%10
#     n=n//10
#     sum=sum+d
# print(sum)

#find the sum of squares of a number

n=int(input("enter the number"))
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d**2
print(sum)