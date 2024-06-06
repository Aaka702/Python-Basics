# Check the given number is amstrong or not

n= int(input("Enter the number "))
sum = 0
num = n
while n>0:
    d = n%10
    n = n//10
    sum =sum + d*d*d
if num == sum:
    print("amstrong")
else:
    print("not amstrong")