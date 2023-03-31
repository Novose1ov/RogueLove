import os
from big_latters import Start_game
from choose_person import choose_person


#####################################################################################
class Character:
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign
        self.hp = None
        self.dmg = None
        print('Character was created')

    def move(self):
        print('Куда то идем...')

#####################################################################################
class PLAYER_HERO(Character):
    def __init__(self):
        Character.__init__(self)
        self.x = int(160 / 2)
        self.y = int(45 / 2)
        self.sign = '@'
        print('PLAYER_HERO was created')

    def move(self):
        moves = {"w": (0, -1),
                 "a": (-1, 0),
                 "s": (0, 1),
                 "d": (1, 0)}
        key = input("Куда идём? ").lower()
        while key not in ("w", "a", "s", "d"):
            key = input("Куда идём? ").lower()
        x, y = moves[key]
        self.x += x
        self.y += y


class Enemy(Character):
    def move(self):
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        x, y = random.choice(moves)
        self.x += x
        self.y += y

#####################################################################################
class Knight(PLAYER_HERO):
    def __init__(self):
        self.hp = 5
        self.damage = 3


class Archer(PLAYER_HERO):
    def __init__(self):
        self.hp = 3
        self.damage = 5


class Wizard(PLAYER_HERO):
    def __init__(self):
        self.hp = 6
        self.damage = 2


class Goblin(PLAYER_HERO):
    def __init__(self):
        self.hp = 2
        self.damage = 6

##################################################################################
os.system('CLS')

choose_person()

player_choice_num = (input('Ваш выбор [1 / 2 / 3 / 4]: '))

while player_choice_num not in ('1', '2', '3', '4'):
    print('Некорректный ввод, попробуйте ещё раз:')
    player_choice_num = (input('Ваш выбор [1 / 2 / 3 / 4]: '))

else:
    if player_choice_num == 1:
        player_class = Knight(PLAYER_HERO)
        input()
        
    elif player_choice_num == 2:
        player_class = Archer(PLAYER_HERO)
        input()
        
    elif player_choice_num == 3:
        player_class = Wizard(PLAYER_HERO)
        input()
        
    elif player_choice_num == 4:
        player_class = Goblin(PLAYER_HERO)
        input()

#os.system('CLS')
#import generate_map


