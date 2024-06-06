# Print the number of digits in a given number and also print the digits
#ecxample
#123 no of digits is 3
# 1
# 2
# 3'

# 7 5 6
# 756%10 - 6         75%10  -5            7%10 --7
# 756//10 75         75//10  5            7//10  7

n=int(input("enter the number"))
c=0
while n>0:
    d=n%10
    n=n//10
    print(d)
    c=c+1
print("Number of digits is ",c)
# 756

