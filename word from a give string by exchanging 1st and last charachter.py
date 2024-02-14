word=input("enter the word: ")
l=list(word)
char=l[0]
l[0]=l[-1]
l[-1]=char
neword=''.join(l)
print("The new word is: ",neword)