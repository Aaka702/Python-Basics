s='I Love My India'
print(s.lower())
print(s.upper())
print(len(s))
print('swapcase',s.swapcase())
print('capitalize',s.capitalize())
print('title case',s.title())


record = 'Leo Tolstoy*1828-08-28*1910-11-20'
fields=record.split('*')
print(fields)
born=fields[1].split('-')
died=fields[2].split('-')
print(born,died)

print(fields[0],"lived about",int(died[0])-int(born[0]),"years")