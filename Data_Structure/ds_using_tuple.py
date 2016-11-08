# Explicit is better than implicit
zoo = ('python', 'elephant', 'penquin')
print('NUmber of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All the animals in the new zoo', new_zoo)
print('Animals brought from the old zoo is', new_zoo[2])
print('Last animal brought from the old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo) - 1 + len(new_zoo[2]))
