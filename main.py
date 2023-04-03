import os
import random



labirint = ['████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████',
            '██          ██  ██          ██                  ██                              ██  ██  ██  ██  ██      ██  ██  ██          ██                ██',
            '██          ██  ██  ██████  ██  ██████████  ██  ██  ██████████████████████████  ██  ██              ██████          ██  ██      ████  ██████  ██',
            '██          ██  ██  ██  ██  ██  ██          ██  ██  ██                      ██      ██  ██████████          ██████████  ████████████  ██  ██  ██',
            '██          ██  ██  ██  ██  ██  ██████████████      ██  ████████████  ████  ██  ██████    ██  ████████████████  ██  ██████  ██        ██  ██  ██',
            '██          ██  ██      ██  ██                  ██  ██  ██              ██  ██  ██      ████                    ██          ██  ████      ██  ██',
            '██  ██████████  ██  ██  ██  ████  ██  ██  ████████  ██  ██  ██████████  ██  ██  ██  ██████    ████████████████  ██  ██████      ██    ██████  ██',
            '██  ██  ██  ██  ██  ██  ██  ██    ██  ██        ██  ██  ██  ██  ██  ██  ██  ██  ██      ████              ████  ██████  ██████  ██  ████  ██  ██',
            '██      ██      ██  ██  ██  ████████  ████████████  ██  ██          ██  ██  ██████  ██  ████  ██  ██  ██    ██              ██  ██  ██        ██',
            '██  ██  ██████  ██  ██  ██                          ██  ██████████████  ██    ██    ██    ██  ██  ██  ██  ██████████████  ████  ██  ████████  ██',
            '██  ██          ██  ██  ██  ████  ████████████████████        ██  ██        ████  ██████████  ██      ██  ██          ██    ██  ██        ██  ██',
            '██  ██████████████  ██  ██  ██            ██        ██  ████  ██  ████████  ██    ██  ██      ██  ██  ██  ██  ██████  ████  ████████  ██████  ██',
            '██                  ██  ██  ██  ██  ████  ██  ████████    ██  ██            ████      ██████              ██  ██  ██    ██        ██      ██  ██',
            '████  ████████  ██████  ██  ██  ██    ██  ██  ██    ██  ████  ████████  ████████████      ██  ██████████████  ██  ████  ██████████████  ████  ██',
            '██    ████  ██████  ██  ██  ██  ████  ██  ██  ████  ██  ██          ██  ██        ██  ██                      ██                ██  ██  ██    ██',
            '██  ████            ██  ██  ██  ████      ██  ██    ██  ██████  ██  ██  ██  ████  ████████████████  ██████████████████  ██████  ██  ██  ████████',
            '██  ████  ████████████  ██  ██        ██████  ████  ██      ██████  ██  ██  ████                ██████          ██  ██████  ██  ██  ██        ██',
            '██                      ██  ████████████      ██    ██  ██  ██      ██  ██    ██  ██  ████████          ██████              ██  ██  ████████  ██',
            '██████████████████████████  ██        ██  ████████  ██  ██  ██  ██  ██  ████████  ██████  ████████████████  ██████████████████  ██      ████  ██',
            '██      ██                  ██  ████  ██  ██        ██████  ██  ██  ██  ██  ██    ██                ██                          ██  ██    ██  ██',
            '██  ██  ██  ██████████████████  ████████  ██████  ████  ██  ██  ██████  ██  ██  ████  ████████  ████████  ██  ████████  ██████████  ██  ████  ██',
            '██  ██  ██  ██  ██                                  ██  ██  ██████  ██      ██  ██          ██      ██    ██    ██  ██████  ██      ████████  ██',
            '██  ██  ██  ██  ██  ██  ████  ██  ██████████████  ████              ██████  ██  ████  ████  ██████      ██████████              ██████        ██',
            '██  ██  ██  ██  ██  ██    ██  ██  ██                    ████  ████  ██  ██  ██    ██    ██      ██████████      ██████████████      ████  ██  ██',
            '██  ██  ██  ██      ██  ████  ██  ██  ████████████████████    ██        ██  ████  ████████████          ██  ██  ██          ██████    ██  ██  ██',
            '██  ██  ██  ██████████  ████████  ██  ██    ██      ████    ████  ████████    ██    ██  ██      ██████      ██  ██████████    ████  ████  ██  ██',
            '██  ██  ██  ██          ██        ██  ██  ████████  ██████████      ██      ████  ████  ██████████  ██████  ██              ████    ██    ██  ██',
            '██  ██      ██  ██████████  ████████  ██                ██      ██  ██████  ██    ██                    ██████████████████  ██    ██████  ██  ██',
            '██  ██  ██  ██              ██    ██  ██  ████  ██  ██  ██  ██████    ████  ██  ██████████████████████      ████  ████          ████  ██  ██  ██',
            '██  ██  ██  ██  ██  ██  ████████  ██  ██            ██  ██    ██████    ██  ██                      ██████  ██          ██  ██████        ██  ██',
            '██  ██  ██  ██  ██  ██        ██      ████████████████  ██  ████  ████  ██  ██████████████████████      ██  ████  ████████████  ████████  ██  ██',
            '██  ██  ██  ██  ██  ████  ██  ██  ██                ██  ██  ██      ██  ██                      ██████  ██    ██  ██                      ██  ██',
            '██  ██  ██  ██  ██  ████  ██  ██  ████████████  ██  ██  ████████  ████  ██  ██████  ██████  ██    ██    ██  ████  ██  ██  ██  ██████  ██████  ██',
            '██  ██  ██  ██  ██  ██    ██                    ██  ██                  ██      ██  ██  ██████████████  ██  ██    ██  ██████████  ██████  ██  ██',
            '██  ██  ██  ██████  ████████████████████████  ████  ██████  ████  ██  ████  ██  ██  ██                  ██  ████  ██  ██                      ██',
            '██  ██  ██                                          ██  ██████    ██    ██  ██  ██  ██  ██████████████████        ██  ██  ██  ██████████████  ██',
            '██  ████████████  ██████████████████  ████████████████          ██████  ██████  ██  ██  ██    ██            ████████  ██  ██████          ██  ██',
            '██            ██████          ██                        ██████████  ██████  ██  ██  ██  ██  ████  ████████  ██        ██  ██  ██  ██  ██  ██  ██',
            '████████████          ██████      ████████████████████████      ██  ██          ██  ██  ██  ██    ██    ████████████  ██  ██  ██  ██  ██  ██  ██',
            '██        ██████████████  ██████████                        ██          ██████████  ██  ██  ██  ██████                ██  ██      ██  ██  ██  ██',
            '██  ████  ██                          ██  ██████████  ██████████  ████  ██  ████    ██  ██  ██      ████████████  ██████  ██  ██████████  ██  ██',
            '██  ██    ██  ██  ██  ████  ████  ██████  ██      ████████  ██████████████  ████  ████  ██  ██████            ██  ██      ██  ██          ██  ██',
            '██  ████                ██████    ██  ██      ██                ██          ██    ██    ██      ████████  ██  ██  ██  ██████  ██  ██  ██  ██  ██',
            '██    ██  ██  ████  ██          ████  ████████████████  ██████  ██  ████████████████  ████  ██████    ██  ██  ██  ██  ████    ██  ██████████████',
            '████  ██████        ██████████████                ████████  ██                        ██        ██  ████████  ██  ██    ████  ██  ██          ██',
            '██    ██      ████████      ██      ██████  ████            ██████████  ██████████████████  ██  ██            ██  ████  ████  ██  ██          ██',
            '██  ████  ██      ████  ██  ██  ██  ██  ██    ████████████          ██        ██            ██  ██  ████████████    ██    ██  ██  ██          ██',
            '██  ████  ██  ██  ████  ██████  ██████  ████████  ██        ██████  ████████████  ████████  ██  ██  ██  ██  ██████  ████████  ██  ██          ██',
            '██        ██                    ██                    ████  ██                        ██    ██          ██                    ██              ██',
            '████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████'
]


WALL_CHAR = "█"

###########################################################################################################


class Player_Hero():
    def __init__(self, x, y):
        self.sign = "❖"
        pass

    def move(self, dx, dy):
        pass

    def hit(self):
        pass
###########################################################################################################


class Enemy():
    def __init__(self, x, y):
        pass

    def move(self, dS):
        pass

    def hit(self):
        pass
###########################################################################################################


class Knight(Player_Hero):
    def __init__(self, x, y):
        Player_Hero.__init__(self, x, y)
        self.x = x
        self.y = y
        self.hp = 16
        self.damage = 5

    def move(self, dx, dy):
        if labirint[self.y + dy][self.x + dx] != WALL_CHAR:
            self.x += dx
            self.y += dy

    def hit(self, dmg):
        self.hp -= dmg


class Archer(Player_Hero):
    def __init__(self, x, y):
        Player_Hero.__init__(self, x, y)
        self.x = x
        self.y = y
        self.hp = 16
        self.damage = 5

    def move(self, dx, dy):
        if labirint[self.y + dy][self.x + dx] != WALL_CHAR:
            self.x += dx
            self.y += dy

    def hit(self, dmg):
        self.hp -= dmg
###########################################################################################################


class Ork(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y)
        self.sign = 'o'
        self.x = x
        self.y = y
        self.hp = 1
        self.damage = 2

    def move(self):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]
        dx, dy = random.choice(moves)
        if labirint[self.y + dy][self.x + dx] != WALL_CHAR:
            self.x += dx
            self.y += dy

    def hit(self, dmg):
        self.hp -= dmg


class Zombie(Player_Hero):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y)
        self.sign = 'z'
        self.x = x
        self.y = y
        self.hp = 2
        self.damage = 1

    def move(self):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]
        dx, dy = random.choice(moves)
        if labirint[self.y + dy][self.x + dx] != WALL_CHAR:
            self.x += dx
            self.y += dy

    def hit(self, dmg):
        self.hp -= dmg
###########################################################################################################
print(
    """
                ВЫБЕРИТЕ ПЕРСОНАЖА:                    
  1. Рыцарь  |  2. Лучник  |
    HP: 16   |    HP: 16   |
    DMG: 5   |    DMG: 5   |
    """)

player_choice_num = input('Ваш выбор [1 / 2]: ')

while player_choice_num not in ('1', '2'):
    os.system('CLS')
    print(
    """
                ВЫБЕРИТЕ ПЕРСОНАЖА:                    
  1. Рыцарь  |  2. Лучник  |
    HP: 16   |    HP: 16   |
    DMG: 5   |    DMG: 5   |
    """)
    print('Некорректный ввод, попробуйте ещё раз:')
    player_choice_num = input('Ваш выбор [1 / 2]: ')

else:
    if player_choice_num == '1':
        player = Knight(2, 1)
        os.system('CLS')

    elif player_choice_num == '2':
        player = Archer(2, 1)
        os.system('CLS')
###########################################################################################################
en1 = Ork(132, 48)
en2 = Zombie(38, 3)
en3 = Ork(8, 27)
en4 = Zombie(4, 46)
en5 = Ork(65, 31)
en6 = Zombie(98, 10)
en7 = Ork(64, 8)
en8 = Zombie(136, 3)
en9 = Ork(85, 23)
en10 = Zombie(100, 43)
###########################################################################################################
def print_level_with_player():
    for y, row in enumerate(labirint):
        for x, char in enumerate(row):
            if (x == player.x) and (y == player.y) and (player.hp > 0):
                print(player.sign, end="")
            elif (x == en1.x) and (y == en1.y) and (en1.hp > 0):
                print(en1.sign, end="")
            elif (x == en2.x) and (y == en2.y) and (en2.hp > 0):
                print(en2.sign, end="")
            elif (x == en3.x) and (y == en3.y) and (en3.hp > 0):
                print(en3.sign, end="")
            elif (x == en4.x) and (y == en4.y) and (en4.hp > 0):
                print(en4.sign, end="")
            elif (x == en5.x) and (y == en5.y) and (en5.hp > 0):
                print(en5.sign, end="")
            elif (x == en6.x) and (y == en6.y) and (en6.hp > 0):
                print(en6.sign, end="")
            elif (x == en7.x) and (y == en7.y) and (en7.hp > 0):
                print(en7.sign, end="")
            elif (x == en8.x) and (y == en8.y) and (en8.hp > 0):
                print(en8.sign, end="")
            elif (x == en9.x) and (y == en9.y) and (en9.hp > 0):
                print(en9.sign, end="")
            elif (x == en10.x) and (y == en10.y) and (en10.hp > 0):
                print(en10.sign, end="")
            else:
                print(char, end="")
        print()
###########################################################################################################
hero_type = ['Рыцарь', 'Лучник']
while True:

    os.system('CLS')

    print_level_with_player()
    if (player.hp > 0) and (en1.hp > 0):
        if (player.x == en1.x and player.y == en1.y):
            en1.hit(player.damage)
            player.hit(en1.damage)
        elif (player.x == en2.x and player.y == en2.y):
            en2.hit(player.damage)
            player.hit(en2.damage)
        elif (player.x == en3.x and player.y == en3.y):
            en3.hit(player.damage)
            player.hit(en3.damage)
        elif (player.x == en4.x and player.y == en4.y):
            en4.hit(player.damage)
            player.hit(en4.damage)
        elif (player.x == en5.x and player.y == en5.y):
            en5.hit(player.damage)
            player.hit(en5.damage)
        elif (player.x == en6.x and player.y == en6.y):
            en6.hit(player.damage)
            player.hit(en6.damage)
        elif (player.x == en7.x and player.y == en7.y):
            en7.hit(player.damage)
            player.hit(en7.damage)
        elif (player.x == en8.x and player.y == en8.y):
            en8.hit(player.damage)
            player.hit(en8.damage)
        elif (player.x == en9.x and player.y == en9.y):
            en9.hit(player.damage)
            player.hit(en9.damage)
        elif (player.x == en10.x and player.y == en10.y):
            en10.hit(player.damage)
            player.hit(en10.damage)

    print('HERO:',hero_type[int(player_choice_num) - 1], end = '    ')
    print(f'HP: {player.hp}    DMG: {player.damage}')


    move = input('\nКуда идём [ W / A / S / D ]: ').lower()

    while (move not in ('w', 'a', 's', 'd', 'ц', 'ф', 'ы', 'в')) or (move == '') or (move == ' '):
        os.system('CLS')
        print_level_with_player()
        print('HERO type:', hero_type[int(player_choice_num) - 1])
        print(f'HP: {player.hp}    DMG: {player.damage}')
        move = input('\nКуда идём [ W / A / S / D ]: ').lower()
    else:
        if move == 'w' or move == 'ц':
            player.move(0, -1)
            en1.move()
            en2.move()
            en3.move()
            en4.move()
            en5.move()
            en6.move()
            en7.move()
            en8.move()
            en9.move()
            en10.move()
        elif move == 'a' or move == 'ф':
            player.move(-1, 0)
            en1.move()
            en2.move()
            en3.move()
            en4.move()
            en5.move()
            en6.move()
            en7.move()
            en8.move()
            en9.move()
            en10.move()
        elif move == 's' or move == 'ы':
            player.move(0, 1)
            en1.move()
            en2.move()
            en3.move()
            en4.move()
            en5.move()
            en6.move()
            en7.move()
            en8.move()
            en9.move()
            en10.move()
        elif move == 'd' or move == 'в':
            player.move(1, 0)
            en1.move()
            en2.move()
            en3.move()
            en4.move()
            en5.move()
            en6.move()
            en7.move()
            en8.move()
            en9.move()
            en10.move()




