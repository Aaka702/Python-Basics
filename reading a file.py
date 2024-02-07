inf=False
try:
    inf=open('example.txt')
    line=inf.read()
except IOError as io:
    print(io)
finally:
    if inf:inf.close()