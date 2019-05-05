s1 = "I'm \ta super student."
print(s1.split())
print(s1.split('s'))
print(s1.split('super'))
print(s1.split('super '))
print(s1.split(' '))
print(s1.split('', maxsplit=2))
print(s1.split('\t', maxsplit=2))
