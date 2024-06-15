from array import *
var = array('i',[3,5,2,1,6,4])
print(var)
var.sort()
print(var)
print(len(var))
for i in range(len(var)):
    if var[i]>2:
        print("the value is :",var[i])
    print()