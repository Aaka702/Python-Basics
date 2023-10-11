# s=input("enter the string")
# vowel=0
# for i in s:
#     if i in 'aeiouAEIOU':
#         vowel=vowel+1
# print(vowel)


#Count number of vowels and counts

s=input("enter the string")
vowel=0
digi=0
for i in s:
    if i in"aeiouAEIOU":
        vowel=vowel+1
    elif i in '0123456789':
        digi=digi+1
print(vowel)
print(digi)
