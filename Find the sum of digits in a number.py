# Find the sum of digits in a number using the while loop

n= int(input("Enter th number"))
sum =0
while n>0:
    d = n%10
    n = n//10
    sum =sum + d
print("The sum of the digits in a number is ",sum)
