# This is a string object
name = 'Shawn'

if name.startswith('Sha'):
    print('Yes, the string starts with "Sha"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
