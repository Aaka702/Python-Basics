n=int(input("enter the number"))
esum=0
osum=0
for i in range(1,n):
    if i%2==0:
        esum=esum+i

    else:
        osum=osum+i
print(osum)
print(esum)