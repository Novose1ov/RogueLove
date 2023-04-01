import random


class Object:
    def __init__(self, symbol, color):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        self.symbol = symbol
        self.color = color


class Armor(Object):

    Armor_hero = Object(symbol='^', color='red')

    def __init__(self, symbol, color, hp=None):
        Object.__init__(self, symbol, color)
        self.value = "protect"
        self.hp = hp + 10


class Weapon(Object):

    sign_Weapon = ['|', '*', ')']
    sign = random.choice(sign_Weapon)

    if sign == '|':
        def __init__(self, symbol, color, dmg=None):
            Object.__init__(self, symbol, color)
            self.color = 'grey'
            self.value = "attack"
            self.dmg = dmg + 10

    if sign == '*':
        def __init__(self, symbol, color, dmg=None):
            Object.__init__(self, symbol, color)
            self.color = 'brown'
            self.value = "attack"
            self.dmg = dmg + 15

    if sign == ')':
        def __init__(self, symbol, color, dmg=None):
            Object.__init__(self, symbol, color)
            self.color = 'white'
            self.value = "attack"
            self.dmg = dmg + 5


class Potions(Object):

    option_Potion = ['attack', 'protect', 'luck']
    option = random.choice(option_Potion)

    if option == 'attack':
        def __init__(self, symbol, color, dmg=None):
            Object.__init__(self, symbol, color)
            self.dmg = dmg + 15

    if option == 'protect':
        def __init__(self, symbol, color, hp=None):
            Object.__init__(self, symbol, color)
            self.hp = hp + 10

    if option == 'protect':
        def __init__(self, symbol, color, money=None):
            Object.__init__(self, symbol, color)
            chance = random.random() + 1
            self.money = money * chance
