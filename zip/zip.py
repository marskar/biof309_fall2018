names = ['Alice', 'Bob', 'Cindy']
ages = [63, 61, 65]

alice, bob, cindy = zip(names, ages)
names, heights = zip(alice, bob, cindy)

z = zip(names, ages)

list(z)

names, ages = zip(*z)
