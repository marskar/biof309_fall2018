# assign more than one variable at a time
x = y = z = 1

# assign more than one variable at a time using tuple unpacking
values = 1, 2, 3
one, two, three = values

# assign more than one variable at a time from a list comprehension
one, two, three = [x+1 for x in range(3)]

about_me = 'Martin', 'Skarzynski', 1985, 'Warsaw', 'Poland'
firstname, lastname, birthyear, birthcity, birthcountry = about_me
first, last, *birth = about_me

# swap two variables
a = 'a'
b = 'b'
a, b = b, a
a, b

# pair up keys and values to make a dictionary
vals = 'Martin', 'Skarzynski', 1985, 'Warsaw', 'Poland'
keys = 'firstname', 'lastname', 'birthyear', 'birthcity', 'birthcountry'
d = dict(zip(keys, about_me))

# add more than one key-value pair to a dictionary at a time
d['job', 'hobby'] = 'scientist', 'zumba'

nums = 1, 2, 3, 4

# unpack two tuples into a list
[*vals, *keys]

# if you want to do something fancy.
d2 = {'My ' + key: 'is ' + str(value) for key, value in zip(keys, vals)}
d2.items()
https://goo.gl/8J5EMK
