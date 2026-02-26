heroes = ['spider man','thor','hulk','iron man','captain america']
print(len(heroes))
heroes.append('black panther')
print(heroes)
heroes.remove('black panther')
heroes.insert(3, 'black panther')
print(heroes)
heroes[1:3] = ['docter strange']
print(heroes)
heroes.sort()
print(heroes)

expenses = [2200, 2350, 2600, 2130, 2190]
print(f'Feb compared to Jan: {expenses[1]-expenses[0]}')
print(f'Total in first quarter: {expenses[0]+expenses[1]+expenses[2]}')
print(f'Did I spend 2000 in any month? {2000 in expenses}')
expenses.append(1980)
print(expenses)
expenses[3]=expenses[3]-200
print(expenses)