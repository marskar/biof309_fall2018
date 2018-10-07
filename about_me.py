# press i
# and now you can type normally
# getting in insert mode: i I a A o O
# to get into normal mode, press escape or ctrl + [
# to run a line of code in PyCharm, press alt+shift+E
# to assign a variable, run variable_name = value
x = 2
# assign two variables the same value
y = x = 5
# assign multiple variables at once
z = 1, 2, 3 # z is a tuple, this is a sequence of values
one, two, three = z
# to change a word, cw
# to change everything to the right, C
# to replace one character, hit r and then the replacement character
# assign multiple variables using a list comprehension
one, two, three = [y*y for y in range(3)]
zero, one, two = list(range(3))
# x is an int
x = 5
# y and z are floats
y = 1/3
z = 5.
# to change everything in quotes, place your cursor in the quotes & ci' or ci"
# replace my name with your name below
name = "Martin"
five = str(x)
# instead of the help function, use quick documentation in PyCharm
# check the type
# types we use today: int, str, float, list, tuple
print(type(5.))
