# assign more than one variable at a time
x = y = z = 1

# assign more than one variable at a time using tuple unpacking
values = 1, 2, 3
one, two, three = values

# assign more than one variable at a time from a list comprehension
one, two, three = [x+1 for x in range(3)]

# assign more than one variable at a time
about_me = 'Martin', 'Skarzynski', 1985, 'Warsaw', 'Poland'
firstname, lastname, birthyear, birthcity, birthcountry = about_me
first, last, *birth = about_me
first, last, *birth, nationality = about_me

# a string is a sequence of characters
a, b, c = 'a', 'b', 'c'
a, b, c = 'abc'

# swap two variables
a, b = 'a', 'b'
a, b = b, a
a, b

# pair up keys and values to make a dictionary
vals = 'Martin', 'Skarzynski', 1985, 'Warsaw', 'Poland'
keys = 'firstname', 'lastname', 'birthyear', 'birthcity', 'birthcountry'
d = dict(zip(keys, vals))

# add more than one key-value pair to a dictionary at a time
d['job', 'hobby'] = 'scientist', 'zumba'

nums = 1, 2, 3, 4

# unpack two tuples into a list
[*vals, *keys]

# if you want to do something fancy, use a dictionary comprehension
d2 = {'My ' + key: 'is ' + str(value) for key, value in zip(keys, vals)}
d2
