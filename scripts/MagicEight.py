import random


class MagicEight():
    """MagicEight class to encapsulate magic_eight function"""
    def magic_eight(self, arg):
        """magic_eight function accepts an int and returns some postulations"""
        method_name = 'magic' + str(arg)
        method = getattr(self, method_name, lambda: "Input must be an int between 1 and 8")
        return method()

    @staticmethod
    def magic1():
        print("Straight up, nope")

    def magic2(self):
        print("I wouldn't put money on it")

    def magic3(self):
        print("YASS")

    def magic4(self):
        print("I'm sorry, I wasn't listening...")

    def magic5(self):
        print("Are you really asking ME that kind of question!?")

    def magic6(self):
        print("...")

    def magic7(self):
        print("no.")

    def magic8(self):
        print("perhaps ;)")

me = MagicEight()
me.magic_eight(random.randint(1, 8))
me.magic_eight(1)
