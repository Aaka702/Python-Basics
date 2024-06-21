n = int(input(""))
count = 0
non_zero = []
for i in range(n+1):
    print(i)
    binary = bin(i)[2:]
    print("binary of ",i,"is ",binary)
    count = binary.count('1')
    print("count of one",count)
    non_zero.append(count)
print(non_zero)



