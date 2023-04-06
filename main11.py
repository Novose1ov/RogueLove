import os
import random
###########################################################################################################
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
###########################################################################################################
class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sign = ''
        self.hp = 0
        self.dmg = 0
        self.is_dead = False

    def move(self, dx, dy):
        if labirint[self.y + dy][self.x + dx] != '█':
            self.x += dx
            self.y += dy

    def hit(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.is_dead = True
###########################################################################################################
class Enemy(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)
        self.x = x
        self.y = y
        self.sign = random.choice(['q','w','e','t','y','u','o','p','a','s','d', \
                                   'f','g','h','j','k','l','z','x','c','v','b','n','m'])
        self.static_hp = random.randint(2, 6)
        self.dmg = random.randint(1, 2)
        self.hp = self.static_hp

    def move(self):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)])
        if labirint[self.y + dy][self.x + dx] != '█':
            self.x += dx
            self.y += dy
###########################################################################################################
class Player(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)
        self.x = x
        self.y = y
        self.sign = '▼'
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
###########################################################################################################
class Knight(Player):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.x = x
        self.y = y
        self.static_hp = 10
        self.static_dmg = 2
        self.hp = 10
        self.dmg = 2
        self.weapon =  '|'
###########################################################################################################
class Archer(Player):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.x = x
        self.y = y
        self.static_hp = 7
        self.static_dmg = 5
        self.hp = 7
        self.dmg = 5
        self.weapon = ')'
###########################################################################################################
class Viking(Player):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.x = x
        self.y = y
        self.static_hp = 9
        self.static_dmg = 3
        self.hp = 9
        self.dmg = 3
        self.weapon = 'Г'
###########################################################################################################
class Hunter(Player):
    def __init__(self, x, y):
        Player.__init__(self, x, y)
        self.x = x
        self.y = y
        self.static_hp = 8
        self.static_dmg = 4
        self.hp = 8
        self.dmg = 4
        self.weapon = 'L'
###########################################################################################################
class Object:
    def __init__(self, x, y, simbol):
        self.x = x
        self.y = y
        self.simbol = simbol
###########################################################################################################
class Weapon(Object):

    def __init__(self, x, y, simbol):
        Object.__init__(self, x, y, simbol)
        self.x = x
        self.y = y
        self.simbol = simbol
        '''if self.simbol in player.inventory:
            if (self.simbol == player.weapon):
                player.dmg += 3
            else:
                player.dmg += 1'''

###########################################################################################################
class Armor(Object):
    def __init__(self, x, y, symbol):
        Object.__init__(self, x, y, simbol)
        self.x = x
        self.y = y
        self.symbol = symbol

###########################################################################################################
class Potions(Object):

    #option_Potion = ['attack', 'protect', 'luck']
    #option = random.choice(option_Potion)

    def __init__(self,x, y, simbol):
        Object.__init__(self, x, y, simbol)
        self.x = x
        self.y = y
        self.symbol = symbol

###########################################################################################################
def choose_hero_menu():
    print(
"""                ВЫБЕРИТЕ ГЕРОЯ:                    
|  1. Рыцарь  |  2. Лучник  |  
|    HP: 10   |    HP: 7    |
|    DMG: 2   |    DMG: 5   |
""")
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
            elif (x == we1.x) and (y == we1.y) and (we1.simbol not in player.inventory):
                print(we1.simbol, end="")
            else:
                print(char, end="")
        print()
###########################################################################################################
def view_hp_dmg_stroke():
    hero_type = ['Рыцарь', 'Лучник']
    print('Герой:', hero_type[int(player_choice_num) - 1], end='    ')
    print(f'HP: {player.hp}/{player.static_hp}    DMG: {player.dmg}/{player.static_dmg}')

    print(f'{en1.sign}[HP:{en1.hp}/{en1.static_hp} DMG:{en1.dmg}]', end='   ')
    print(f'{en2.sign}[HP:{en2.hp}/{en2.static_hp} DMG:{en2.dmg}]', end='   ')
    print(f'{en3.sign}[HP:{en3.hp}/{en3.static_hp} DMG:{en3.dmg}]', end='   ')
    print(f'{en4.sign}[HP:{en4.hp}/{en4.static_hp} DMG:{en4.dmg}]', end='   ')
    print(f'{en5.sign}[HP:{en5.hp}/{en5.static_hp} DMG:{en5.dmg}]', end='   ')
    print(f'{en6.sign}[HP:{en6.hp}/{en6.static_hp} DMG:{en6.dmg}]', end='   ')
    print(f'{en7.sign}[HP:{en7.hp}/{en7.static_hp} DMG:{en7.dmg}]', end='   ')
    print(f'{en8.sign}[HP:{en8.hp}/{en8.static_hp} DMG:{en8.dmg}]', end='   ')
    print(f'{en9.sign}[HP:{en9.hp}/{en9.static_hp} DMG:{en9.dmg}]', end='   ')
    print(f'{en10.sign}[HP:{en10.hp}/{en10.static_hp} DMG:{en10.dmg}]', end='   ')
###########################################################################################################
class Game:
    def __init__(self, player, en1, en2, en3, en4, en5, en6, en7, en8, en9, en10):
        self.player = player
        self.en1 = en1
        self.en1 = en2
        self.en1 = en3
        self.en1 = en4
        self.en1 = en5
        self.en1 = en6
        self.en1 = en7
        self.en1 = en8
        self.en1 = en9
        self.en1 = en10


    def play(self):
        hero_type = ['Рыцарь', 'Лучник', 'Викинг', 'Oхотник']
        while True:
            os.system('CLS')
            if (player.hp > 0):
                if (player.x == en1.x and player.y == en1.y and en1.hp > 0):
                    en1.hit(player.dmg)
                    player.hit(en1.dmg)
                elif (player.x == en2.x and player.y == en2.y and en2.hp > 0):
                    en2.hit(player.dmg)
                    player.hit(en2.dmg)
                elif (player.x == en3.x and player.y == en3.y and en3.hp > 0):
                    en3.hit(player.dmg)
                    player.hit(en3.dmg)
                elif (player.x == en4.x and player.y == en4.y and en4.hp > 0):
                    en4.hit(player.dmg)
                    player.hit(en4.dmg)
                elif (player.x == en5.x and player.y == en5.y and en5.hp > 0):
                    en5.hit(player.dmg)
                    player.hit(en5.dmg)
                elif (player.x == en6.x and player.y == en6.y and en6.hp > 0):
                    en6.hit(player.dmg)
                    player.hit(en6.dmg)
                elif (player.x == en7.x and player.y == en7.y and en7.hp > 0):
                    en7.hit(player.dmg)
                    player.hit(en7.dmg)
                elif (player.x == en8.x and player.y == en8.y and en8.hp > 0):
                    en8.hit(player.dmg)
                    player.hit(en8.dmg)
                elif (player.x == en9.x and player.y == en9.y and en9.hp > 0):
                    en9.hit(player.dmg)
                    player.hit(en9.dmg)
                elif (player.x == en10.x and player.y == en10.y and en10.hp > 0):
                    en10.hit(player.dmg)
                    player.hit(en10.dmg)
                elif (player.x == we1.x) and (player.y == we1.y):
                    player.add_item(we1.simbol)
                    if we1.simbol in player.inventory:
                        if (we1.simbol == player.weapon):
                            player.dmg += 3
                        else:
                            player.dmg += 1

                print_level_with_player()
                view_hp_dmg_stroke()

                if len(player.inventory) != 0:
                    print("\n", player.inventory[0])

                move = input('\n\n\tКуда идём [ W / A / S / D ]: ').lower()

                while (move not in ('w', 'a', 's', 'd', 'ц', 'ф', 'ы', 'в')) or (move == '') or (move == ' '):
                    os.system('CLS')
                    print_level_with_player()
                    view_hp_dmg_stroke()
                    move = input('\n\n\tКуда идём [ W / A / S / D ]: ').lower()
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
                    if move == 'a' or move == 'ф':
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
                    if move == 's' or move == 'ы':
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
                    if move == 'd' or move == 'в':
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

            else:
                os.system('CLS')
                input('GAME OVER')
                break
###########################################################################################################
os.system('CLS')
choose_hero_menu()
player_choice_num = input('Ваш выбор [1 / 2]: ')
while player_choice_num not in ('1', '2'):
    os.system('CLS')
    choose_hero_menu()
    player_choice_num = input('Ваш выбор [1 / 2]: ')
else:
    if player_choice_num == '1':
        player = Knight(2, 1)
        os.system('CLS')
    elif player_choice_num == '2':
        player = Archer(2, 1)
        os.system('CLS')
###########################################################################################################
en1 = Enemy(38, 3)
en2 = Enemy(8, 27)
en3 = Enemy(65, 31)
en4 = Enemy(64, 8)
en5 = Enemy(4, 46)
en6 = Enemy(100, 43)
en7 = Enemy(85, 23)
en8 = Enemy(98, 10)
en9 = Enemy(136, 3)
en10 = Enemy(132, 48)

we1 = Weapon(2,3, '|')

game = Game(player, en1, en2, en3, en4, en5, en6, en7, en8, en9, en10)
game.play()
###########################################################################################################