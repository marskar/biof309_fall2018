# %% import numpy
import numpy as np

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
z.shape = 4, 3
z.shape

# %% check types
a.dtype
z.dtype
type(a)
type(z)
type(a.shape)

# %% common functions
a.sum()
a.max()
a.min()
np.exp(a)

# %% flattening
a.shape
a
np.arange(9)  # start flat
a.reshape(-1)  # using reshape
a.shape = 9  # using shape, if size is exactly 9
a.size

list(a.flat)  # into a single list
a.ravel()  # into an array
a.flatten()  # into an array
print(*a)  # into arguments (rows)
print(*a.flat)  # into arguments (values)

# %% When in doubt, use -1 in shape and reshape
a.shape = 3, 3  # using shape, if size is exactly 9
a.shape = -1  # using shape, regardless of size
a.shape = 3, -1  # using shape, if size a multiple of 3

# %% transposing
a.T

# %% iterate by row
for row in a:
    print(row)

# %% iterate by value
for row in a.flat:
    print(row)

for row in "pythoniscool":
    print(row)

# %% iteration example
# a list of strings
list("pythoniscool")
p = np.array(list("pythoniscool")).reshape(2, 6)
p
f = p.flat
next(f)

for i in p.flat:
    print(i)

# back to a list of strings
[x for x in p.flat]

# back to a string
''.join(p.flat)

# %% basic arithmetic
a - a
a ** 2
a

# %% re-assignment
a += a
a = a + a
a

c = 0
c += 1
c += 1
c

# %% boolean array
True
type(True)
a
a < 4

# %% indexing with boolean array
z[z == 0]

# %% be careful with bools...
isinstance(True, bool)
isinstance(True, int)
issubclass(bool, int)
True - 1

# %% indexing with ints
a[0]  # first row
a.flat[0]  # first value
a[-1]  # last row
a.flat[-1]  # last value

# %% indexing with tuples
a
a[1, 2]
a[(1, 2)]

# also works with a single item tuple
a[(2)]
a[2, ]

# don't use lists for this
a[[1, 2]]

# %% indexing with variables
r = 0
c = 1
a[r, c]

# %% slicing with ints
a[:]  # all rows
a[1:]  # second row and all subsequent rows (skip first 1)
a[:1]  # all rows up to, but not including, the third row (get first 2)
a[:-1]  # all rows up to, but not including, the last row
a[::2]  # every other row (count by 2)
a[::2]  # every other row (count by 2)
"a[start:stop:step]"[::-1]
"a[start:stop:step]"[::-2]
"a[start:stop:step]"[2:7]

# %% slicing with tuples
a[:, :]  # all rows
a[1:, 1]  # second row and all subsequent rows (skip first 1) in the second column
a[:2, 2]  # all rows up to, but not including, the third row (get first 2) in the third column

# %% slicing alternatives
first, second, third = a  # requires exactly 3 rows
first, *others = a  # will work for any number of rows
_, second, *_ = a  # will work for any number of rows
*others, last = a  # will work for any number of rows
_, _, third, *_ = a  # will work for any number of rows

# similar to using -1 in shape and reshape,
# in that both can work regardless of array size
a.reshape(3, -1)
# this results in more robust (less fragile) code!

# %% no copy
b = a
a == b
a is b
id(a) == id(b)
a.shape = 3, 3
b.shape = 9
a.shape  # a's shape changes
b.shape = 3, 3
b[1, 2] = 9
a  # a's data changes

# %% shallow copy
c = a[:]
c is a
id(c) == id(a)
c[0, 0] = 9
a  # a's data changes
a.shape = 3, 3
c.shape = 9
a.shape  # a's shape does not change
c.T
a.T

# %% deep copy
d = a.copy()
d is a
id(d) == id(a)
d is a
d[2, 2] = 9
a  # a's data does not change
a.shape = 3, 3
d.shape = 9
a.shape  # a's shape does not change

# %% view
v = a.view
v is a
id(v) == id(a)
a.shape = 3, 3

# These 3 lines result in errors!
# remove the #s to see the errors
#v.shape = 9  # a view has no shape
#v[1, 2] = 9  # a view does not support item assignment
#v_copy = v.copy()  # a view does not have the copy method

# %% copy types explained in lists
from copy import deepcopy

original = ["a", ["b", "c"]]
alias = original  # alias
shallow = list(original)  # shallow copy
shallow = original[:]  # shallow copy
deep = deepcopy(original)  # deep copy

original.append(4)  # only added to list1 and 2
print(original, alias, shallow, deep, sep="\n")

original[0] = 1  # only changed in list 1 and 2
print(original, alias, shallow, deep, sep="\n")

original[1][0] = 2  # changed in lists 1, 2 and 3
print(original, alias, shallow, deep, sep="\n")

# %% nesting
p = np.array(list("pythonisgr8!"), dtype=object).reshape(2, 6)
p.shape
p[1, 5] = np.array(list("!!!"))
p[-1]
p[-1][0]
p[-1][-1]
p[-1][-1][0]


# %% creating an array from a custom function
def f(x, y):
    return 10 * x + y


c = np.fromfunction(f, (3, 3), dtype=int)
c

# %% get sklearn datasets
from sklearn.datasets import (
    load_boston,
    load_breast_cancer,
    load_diabetes,
    load_digits,
    load_iris,
    load_wine
)

# Challenge: can you write a function that can take any of the strings below
# plot a histogram on the corresponding scikit-learn dataset's data?
datasets = ['breast_cancer', 'boston', 'diabetes', 'digits', 'iris', 'wine']
diabetes = load_diabetes()
digits = load_digits()

# you'll probably need to use eval in for your function
x = 'digits()'
dataset = eval('load_' + x)


# explore the dataset sklearn 'Bunch' type
type(diabetes)
diabetes.keys()
diabetes.feature_names

# %% explore the data
type(data)
data.shape
data.dtype
data.argmax()
data.max()
data.mean()
data.std()

# %% make a histogram of the diabetes data and matplotlib
import matplotlib.pyplot as plt

# https://docs.scipy.org/doc/numpy/user/quickstart.html
plt.hist(data, bins=50, density=1)
plt.show()
