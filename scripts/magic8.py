import random


def magic_eight_dict(x):
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
    return in_out.get(x, "Input must be an int between 1 and 8")


def magic_eight_tuple(x):
    """Magic 8 ball accepting an int and returning some postulations"""
    in_out = (
        "Straight up, nope",
        "I wouldn't put money on it",
        "YASS",
        "I'm sorry, I wasn't listening...",
        "Are you really asking ME that kind of question!?",
        "...",
        "No",
        "Perhaps"
    )
    return in_out[x - 1] if x in range(1, 8) else "Input must be an int between 1 and 8"


def magic_eight(x):
    """Magic 8 ball accepting an int and returning some postulations"""
    return (
        "Straight up, nope" if x == 1 else
        "I wouldn't put money on it" if x == 2 else
        "YASS" if x == 3 else
        "I'm sorry, I wasn't listening..." if x == 4 else
        "Are you really asking ME that kind of question!?" if x == 5 else
        "..." if x == 6 else
        "No" if x == 7 else
        "Perhaps" if x == 8 else
        "Input must be an int between 1 and 8"
    )


magic_eight_dict(random.randint(1, 8))
magic_eight_tuple(random.randint(1, 8))
magic_eight(random.randint(1, 8))
