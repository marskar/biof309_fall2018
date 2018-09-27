Last time, we learned to use the `help` function.

Today, we will pass the `round` function to `help` as an argument.

Do you remember how to get `help` with the `round` function?

```python
help(round)
```

The first line of the `help` function output tells us that `round` is a `built-in` function from the `builtins` module.

This just means that `round`, like other `built-in` functions, is ready for immediate use, right-out-of-the-box.

The `round` function can take exactly 1 or 2 arguments. While the `number` argument is required, the `ndigits` argument is optional, because it has a default value.

Regardless of whether an argument is required or optional, it can be passed to a function in 2 different forms.

If it is passed to a function by itself, it is called a **positional argument**, because its position can affect the result, e.g. 

`round(-1, 42)==round(42, -1)` evaluates to:

The other flavor of argument is a **named argument**, because it follows the argument *name* and an equals sign (`=`). 

The order of the named arguments does not matter, as long as all positional arguments are passed beforehand.

We'll get an error unless we give `round`

1. a single positional argument,
2. two positional arguments.
3. a positional argument followed by `ndigits` as a named argument, or
4. `number` and `ndigits` as two named arguments,

Instead of passing values to `round`, we can pass variables. 

Pro-tip!

You can assign multiple variables on the same line!

To do this, the variables on the left side of the equals sign (`=`) must be separated by commas (`,`), while the values on the right side can be a list or a tuple.

Another cool trick related to functions is **argument unpacking**:

1. Store all of the positional arguments in a list or tuple and then
2. use the star (`*`) operator to **unpack** the arguments.

The code below evaluates to 40.

Now for a little fun!

What happens when you call `help` on `help`, i.e. `help(help)`? 

We already knew what calling `help` on a 'thing' does, but what about calling `help` without any arguments? Give `help()` a try in IDLE!

Inside the interactive help session initiated by running `help()`, type `builtins` and hit Enter/return to see all of the built-in functions available in Python listed in alphabetical order. 

The last built-in function in the list is `zip`.

The `zip` function is useful, because it can pair up values in two or more lists or tuples.

Run the code below.

Based on the ages, the eldest person of the three people below is Cindy.

What if we wanted to do the opposite of `zip`? Which function would we use? 

You might be thinking `unzip`, but such a function does not exist in Python. 
To recreate the original lists, we would actually just use `zip` again!

## Review
In this lesson, we learned that 

1. arguments that have default values are optional 
2. arguments can be passed with or without names
3. the order of positional arguments matters 
4. ready-to-use functions are called built-ins 

Next, we will move on from built-in functions to the Python standard library!
