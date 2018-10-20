import random


def magic8(integer):
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


magic8(random.randint(1, 8))
