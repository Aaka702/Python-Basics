#Replace the repeated letter form the string except the first string
# eg onion on oak
# oni$n $n $ak

s=input("Enter the string")
chr=s[0]
s=s.replace(chr,'$')
s=chr+s[1:]
print("final string",s)