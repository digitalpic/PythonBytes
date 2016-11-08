# 'ab' is short for 'address book'

ab = {
    'Digital': 'digital3@gmail.com',
    'James': 'jimmydeam@sausage.com',
    'Ghost': 'ghost@intheshell.org',
    'Apple': 'applejack@rottencore.com'

}


print("Digital Pic's address is", ab['Digital'])

# Deleting a key-value pair
del ab['James']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
	print('Contact {} at {}'.format(name, address))


# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
	print("\nGuido's address is", ab['Guido'])