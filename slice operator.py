#sequence[start:]
#sequence[start:end]
#sequence[start:end:step]
#  0 1 2 3 4 5 6 7
#  P A S S W O R D
# -8-7-6-5-4-3-2-1
s='PASSWORD'

print(s[4:])
print(s[3:7])
print(s[-3:-1])
print(s[::3])
print(s[::-2])