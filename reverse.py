string=input("Enter the string")
len=0
rev=''
for i in string:
    len+=1
    for j in range(len,0,-1):
        print(j)
print(len)
