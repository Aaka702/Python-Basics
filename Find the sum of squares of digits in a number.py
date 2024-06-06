# Find the sum of squares of digits in a number

n = int(input("Enter the number"))
sum =0
while n>0:
    d = n%10
    n =n//10
    sum = sum + d*d
print("Sum is ",sum)