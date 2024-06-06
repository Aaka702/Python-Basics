# Find the sum of multiples of 5 below 50
sum = 0
for i in range (1,50):
    if i%5==0:
        sum = sum+i
print("Sum is",sum)