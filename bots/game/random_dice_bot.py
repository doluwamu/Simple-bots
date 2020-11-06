import random


class Dice:
    def roll(self):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        if roll1 is not roll2 or roll1 == roll2 and roll1 and roll2 != 1:
            return roll1, roll2
        else:
            return None


roll = Dice.roll("")
print(roll)
