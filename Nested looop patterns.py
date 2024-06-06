
# Normal patter
for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()


# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
for i in range(1,5):
    for j in range(1,5):
        print(j,end= " ")
    print()


# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in  range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#1
#2 2
#3 3 3
#4 4 4 4

for i in  range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10

k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()



#a
#b c
#d e f
#g h i j

k=65
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()
