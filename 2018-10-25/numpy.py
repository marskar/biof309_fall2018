# %% imports
import numpy as np
from sklearn.datasets import load_boston

# %% create an array using the array function
a = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

# %% create an array - using other functions
a = np.arange(9).reshape(3, 3)
z = np.zeros((3, 4))
o = np.ones((4, 3))

# %% shape attribute
a.shape
z.shape

# %% check types
a.dtype
z.dtype
type(a)
type(z)
type(a.shape)

# %% iterate by row
for row in a:
    print(row)

# %% iterate by value
for row in a.flat:
    print(row)

# %% iteration example
p = np.array(list('python')).reshape(3, 2)
next(p.flat)
for i in p.flat:
    print(i)

# %% basic arithmetic
a - a
a ** 2

# %% re-assignment
a += a
a

# %% bools
a < 4

# %% indexing with bools
a[a < 4]

# %% indexing with ints
a[0]  # first row
a.flat[0]  # first value

# %% indexing with tuples
a
a[1, 2]
a[(1, 2)]

# also works with a single item tuple
a[(2)]
a[2,]

# don't use lists for this
a[[1, 2]]

# %% indexing with variables
r = 1
c = 2
a[r, c]

# %% slicing with ints
a[:]  # all rows
a[1:]  # second row and all subsequent rows (skip first 1)
a[:2]  # all rows up to, but not including, the third row (get first 2)
a[:-1]  # all rows up to, but not including, the last row
a[::2]  # every other row (count by 2)

# %% slicing with tuples
a[:, :]  # all rows
a[1:, 1]  # second row and all subsequent rows (skip first 1) in the second column
a[:2, 2]  # all rows up to, but not including, the third row (get first 2) in the third column


# %% creating an array from a custom function
def f(x, y):
    return 10 * x + y
c = np.fromfunction(f, (3, 3), dtype=int)
c

# pick a single value from b
c[1, 1]

# %% common functions
a.sum()
b.max()
b.min()
np.exp(a)


b = load_boston()

data = b['data']

type(data)

data.shape
data.dtype
