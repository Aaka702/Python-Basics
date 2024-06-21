n = int(input("Enter the number"))
binary_rep = bin(n)[2:]
count = 0
for bit in binary_rep:
    if bit == '1':
        count = count+1
print(count)