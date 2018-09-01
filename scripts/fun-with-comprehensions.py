letters, numbers, xyz = [chr(65+i) for i in range(10)], [n for n in range(10)], {'X': 24, 'Y': 25, 'Z': 26}

d1 = dict(zip(letters, numbers))

d2 = {**d1, **xyz}

def add_vals(**kwargs):
    return ' + '.join(k for k in kwargs.keys()) + ' = ' + str(sum(v for v in kwargs.values()))

add_vals(**d2)

[c for c in "I love PyCharm!"]

d = {L: n+1 for n, L in enumerate(chr(65+i) for i in range(5))}
d
