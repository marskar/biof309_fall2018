def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 + n
        return echo_word

    # Return inner_echo
    return inner_echo
print(echo(1))
echo
# Call echo: twice
twice = echo(2)
twice
# Call echo: thrice
thrice = echo(3)
print(thrice.__closure__)
thrice.__closure__.__str__()

# Define a function
def foo(x):
    # inner function "bar"
    def bar(y):
        q = 10
        # inner function "baz"
        def baz(z):
            print("Locals: ", locals())
            print("Vars: ", vars())
            return x + y + q + z
        return baz
    return bar

# Locals: {'y': 20, 'x': 10, 'z': 30, 'q': 10}
# Vars: {'y': 20, 'x': 10, 'z': 30, 'q': 10}
print(foo(10)(20)(30)) # 70

bar = foo(10)
bar
print(bar.__closure__[0].cell_contents)
echo
print(baz.__closure__)
baz = bar(20)
type(baz.__closure__[1])
print(baz.__closure__[1])
locals()
%whos
%who
k=globals().keys()
v=globals().values()
k
name_I_want = "object"
def get_obj_name(arg):
    for name, obj in globals().items():
        if obj == arg:
            return name
    return None
get_obj_name(name_I_want)
globals()
%whos
id(bar)
print(baz.__closure__[0].cell_contents)
baz.__closure__[0].__getattribute__('y')
baz.__closure__.__contains__(*)
echo()