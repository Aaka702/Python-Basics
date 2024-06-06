#Find the sum of even numbers upto n
n= int(input("input enter the limit")) #Accept input from the user
sum = 0 #valriable used to store the sum
i=0 # starting from 0
while i<=n:
    sum=sum+i
    i=i+2
print(sum)