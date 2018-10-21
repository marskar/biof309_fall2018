import random


# Using conditional statements
def magic_eight_cond_stat(x):
    """Magic 8 ball accepting a string and returning some postulations"""
    if x == 1:
        return "Straight up, nope"
    elif x == 2:
        return "I wouldn't put money on it"
    elif x == 3:
        return "YASS"
    elif x == 4:
        return "I'm sorry, I wasn't listening..."
    elif x == 5:
        return "Are you really asking ME that kind of question!?"
    elif x == 6:
        return "..."
    elif x == 7:
        return "No"
    elif x == 8:
        return "Perhaps ;)"
    else:
        print("Input must be an int between 1 and 8")


# Using a conditional expression
def magic_eight_cond_expr(integer):
    """Magic 8 ball accepting an int and returning some postulations"""
    return (
        "Straight up, nope" if integer == 1 else
        "I wouldn't put money on it" if integer == 2 else
        "YASS" if integer == 3 else
        "I'm sorry, I wasn't listening..." if integer == 4 else
        "Are you really asking ME that kind of question!?" if integer == 5 else
        "..." if integer == 6 else
        "No" if integer == 7 else
        "Perhaps" if integer == 8 else
        "Input must be an int between 1 and 8"
    )


# Using a dictionary
def magic_eight_dict(integer):
    """Magic 8 ball accepting an int and returning some postulations"""
    in_out = {
        1: "Straight up, nope",
        2: "I wouldn't put money on it",
        3: "YASS",
        4: "I'm sorry, I wasn't listening...",
        5: "Are you really asking ME that kind of question!?",
        6: "...",
        7: "No",
        8: "Perhaps"
    }
    return in_out.get(integer, "Input must be an int between 1 and 8")


# Using a dictionary comprehension and the enumerate function
def magic_eight_dict_comp(integer, strings):
    in_out = {i + 1: j for i, j in enumerate(strings)}
    return in_out.get(integer, "Input must be an int between 1 and 8")


# Using a tuple and a conditional expression
def magic_eight_tuple(integer, strings):
    """Magic 8 ball accepting an int and returning some postulations"""
    return (strings[integer - 1]
            if integer in range(1, len(strings))
            else "Input must be an int between 1 and 8"
            )


string_tuple = (
    "Straight up, nope",
    "I wouldn't put money on it",
    "YASS",
    "I'm sorry, I wasn't listening...",
    "Are you really asking ME that kind of question!?",
    "...",
    "No",
    "Perhaps"
)

magic_eight_cond_stat(random.randint(1, 8))
magic_eight_cond_expr(random.randint(1, 8))
magic_eight_dict(random.randint(1, 8))
magic_eight_dict_comp(random.randint(1, len(string_tuple)), string_tuple)
magic_eight_tuple(random.randint(1, len(string_tuple)), string_tuple)
