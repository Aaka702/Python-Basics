s = input("Enter the string: ")
string = s[0] + s[1:].replace(s[0], '&')
print("the new string is:", string)
