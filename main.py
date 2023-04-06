import os
import random
###########################################################################################################
labirint = ['  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████   ',
            '  ██          ██  ██          ██                  ██                              ██  ██  ██  ██  ██      ██  ██  ██          ██                ██   ',
            '  ██          ██  ██  ██████  ██  ██████████  ██  ██  ██████████████████████████  ██  ██              ██████          ██  ██      ████  ██████  ██   ',
            '  ██          ██  ██  ██  ██  ██  ██          ██  ██  ██                      ██      ██  ██████████          ██████████  ████████████  ██  ██  ██   ',
            '  ██          ██  ██  ██  ██  ██  ██████████████      ██  ████████████  ████  ██  ██████    ██  ████████████████  ██  ██████  ██        ██  ██  ██   ',
            '  ██          ██  ██      ██  ██                  ██  ██  ██              ██  ██  ██      ████                    ██          ██  ████      ██  ██   ',
            '  ██  ██████████  ██  ██  ██  ████  ██  ██  ████████  ██  ██  ██████████  ██  ██  ██  ██████    ████████████████  ██  ██████      ██    ██████  ██   ',
            '  ██  ██  ██  ██  ██  ██  ██  ██    ██  ██        ██  ██  ██  ██  ██  ██  ██  ██  ██      ████              ████  ██████  ██████  ██  ████  ██  ██   ',
            '  ██      ██      ██  ██  ██  ████████  ████████████  ██  ██          ██  ██  ██████  ██  ████  ██  ██  ██    ██              ██  ██  ██        ██   ',
            '  ██  ██  ██████  ██  ██  ██                          ██  ██████████████  ██    ██    ██    ██  ██  ██  ██  ██████████████  ████  ██  ████████  ██   ',
            '  ██  ██          ██  ██  ██  ████  ████████████████████        ██  ██        ████  ██████████  ██      ██  ██          ██    ██  ██        ██  ██   ',
            '  ██  ██████████████  ██  ██  ██            ██        ██  ████  ██  ████████  ██    ██  ██      ██  ██  ██  ██  ██████  ████  ████████  ██████  ██   ',
            '  ██                  ██  ██  ██  ██  ████  ██  ████████    ██  ██            ████      ██████              ██  ██  ██    ██        ██      ██  ██   ',
            '  ████  ████████  ██████  ██  ██  ██    ██  ██  ██    ██  ████  ████████  ████████████      ██  ██████████████  ██  ████  ██████████████  ████  ██   ',
            '  ██    ████  ██████  ██  ██  ██  ████  ██  ██  ████  ██  ██          ██  ██        ██  ██                      ██                ██  ██  ██    ██   ',
            '  ██  ████            ██  ██  ██  ████      ██  ██    ██  ██████  ██  ██  ██  ████  ████████████████  ██████████████████  ██████  ██  ██  ████████   ',
            '  ██  ████  ████████████  ██  ██        ██████  ████  ██      ██████  ██  ██  ████                ██████          ██  ██████  ██  ██  ██        ██   ',
            '  ██                      ██  ████████████      ██    ██  ██  ██      ██  ██    ██  ██  ████████          ██████              ██  ██  ████████  ██   ',
            '  ██████████████████████████  ██        ██  ████████  ██  ██  ██  ██  ██  ████████  ██████  ████████████████  ██████████████████  ██      ████  ██   ',
            '  ██      ██                  ██  ████  ██  ██        ██████  ██  ██  ██  ██  ██    ██                ██                          ██  ██    ██  ██   ',
            '  ██  ██  ██  ██████████████████  ████████  ██████  ████  ██  ██  ██████  ██  ██  ████  ████████  ████████  ██  ████████  ██████████  ██  ████  ██   ',
            '  ██  ██  ██  ██  ██                                  ██  ██  ██████  ██      ██  ██          ██      ██    ██    ██  ██████  ██      ████████  ██   ',
            '  ██  ██  ██  ██  ██  ██  ████  ██  ██████████████  ████              ██████  ██  ████  ████  ██████      ██████████              ██████        ██   ',
            '  ██  ██  ██  ██  ██  ██    ██  ██  ██                    ████  ████  ██  ██  ██    ██    ██      ██████████      ██████████████      ████  ██  ██   ',
            '  ██  ██  ██  ██      ██  ████  ██  ██  ████████████████████    ██        ██  ████  ████████████          ██  ██  ██          ██████    ██  ██  ██   ',
            '  ██  ██  ██  ██████████  ████████  ██  ██    ██      ████    ████  ████████    ██    ██  ██      ██████      ██  ██████████    ████  ████  ██  ██   ',
            '  ██  ██  ██  ██          ██        ██  ██  ████████  ██████████      ██      ████  ████  ██████████  ██████  ██              ████    ██    ██  ██   ',
            '  ██  ██      ██  ██████████  ████████  ██                ██      ██  ██████  ██    ██                    ██████████████████  ██    ██████  ██  ██   ',
            '  ██  ██  ██  ██              ██    ██  ██  ████  ██  ██  ██  ██████    ████  ██  ██████████████████████      ████  ████          ████  ██  ██  ██   ',
            '  ██  ██  ██  ██  ██  ██  ████████  ██  ██            ██  ██    ██████    ██  ██                      ██████  ██          ██  ██████        ██  ██   ',
            '  ██  ██  ██  ██  ██  ██        ██      ████████████████  ██  ████  ████  ██  ██████████████████████      ██  ████  ████████████  ████████  ██  ██   ',
            '  ██  ██  ██  ██  ██  ████  ██  ██  ██                ██  ██  ██      ██  ██                      ██████  ██    ██  ██                      ██  ██   ',
            '  ██  ██  ██  ██  ██  ████  ██  ██  ████████████  ██  ██  ████████  ████  ██  ██████  ██████  ██    ██    ██  ████  ██  ██  ██  ██████  ██████  ██   ',
            '  ██  ██  ██  ██  ██  ██    ██                    ██  ██                  ██      ██  ██  ██████████████  ██  ██    ██  ██████████  ██████  ██  ██   ',
            '  ██  ██  ██  ██████  ████████████████████████  ████  ██████  ████  ██  ████  ██  ██  ██                  ██  ████  ██  ██                      ██   ',
            '  ██  ██  ██                                          ██  ██████    ██    ██  ██  ██  ██  ██████████████████        ██  ██  ██  ██████████████  ██   ',
            '  ██  ████████████  ██████████████████  ████████████████          ██████  ██████  ██  ██  ██    ██            ████████  ██  ██████          ██  ██   ',
            '  ██            ██████          ██                        ██████████  ██████  ██  ██  ██  ██  ████  ████████  ██        ██  ██  ██  ██  ██  ██  ██   ',
            '  ████████████          ██████      ████████████████████████      ██  ██          ██  ██  ██  ██    ██    ████████████  ██  ██  ██  ██  ██  ██  ██   ',
            '  ██        ██████████████  ██████████                        ██          ██████████  ██  ██  ██  ██████                ██  ██      ██  ██  ██  ██   ',
            '  ██  ████  ██                          ██  ██████████  ██████████  ████  ██  ████    ██  ██  ██      ████████████  ██████  ██  ██████████  ██  ██   ',
            '  ██  ██    ██  ██  ██  ████  ████  ██████  ██      ████████  ██████████████  ████  ████  ██  ██████            ██  ██      ██  ██          ██  ██   ',
            '  ██  ████                ██████    ██  ██      ██                ██          ██    ██    ██      ████████  ██  ██  ██  ██████  ██  ██  ██  ██  ██   ',
            '  ██    ██  ██  ████  ██          ████  ████████████████  ██████  ██  ████████████████  ████  ██████    ██  ██  ██  ██  ████    ██  ██████████████   ',
            '  ████  ██████        ██████████████                ████████  ██                        ██        ██  ████████  ██  ██    ████  ██  ██          ██   ',
            '  ██    ██      ████████      ██      ██████  ████            ██████████  ██████████████████  ██  ██            ██  ████  ████  ██  ██          ██   ',
            '  ██  ████  ██      ████  ██  ██  ██  ██  ██    ████████████          ██        ██            ██  ██  ████████████    ██    ██  ██  ██          ██   ',
            '  ██  ████  ██  ██  ████  ██████  ██████  ████████  ██        ██████  ████████████  ████████  ██  ██  ██  ██  ██████  ████████  ██  ██          ██   ',
            '  ██        ██                    ██                    ████  ██                        ██    ██          ██                    ██              ██   ',
            '  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████   '
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
        self.sign = 'e'
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
        self.weapon_inventory = []

    def add_item(self, item):
        self.weapon_inventory.append(item)

    def remove_item(self, item):
        if item in self.weapon_inventory:
            self.weapon_inventory.remove(item)
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
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
###########################################################################################################
class Weapon(Object):

    def __init__(self, x, y, symbol):
        Object.__init__(self, x, y, symbol)
        self.x = x
        self.y = y
        self.simbol = symbol
###########################################################################################################
class Armor(Object):
    def __init__(self, x, y, symbol):
        Object.__init__(self, x, y, symbol)
        self.x = x
        self.y = y
        self.symbol = symbol
###########################################################################################################
class Potions(Object):

    #option_Potion = ['attack', 'protect', 'luck']
    #option = random.choice(option_Potion)

    def __init__(self,x, y, symbol):
        Object.__init__(self, x, y, symbol)
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


            elif (x == we1.x) and (y == we1.y) and (we1.symbol not in player.weapon_inventory):
                print(we1.symbol, end="")
            elif (x == we2.x) and (y == we2.y) and (we2.symbol not in player.weapon_inventory):
                print(we2.symbol, end="")
            elif (x == we3.x) and (y == we3.y) and (we3.symbol not in player.weapon_inventory):
                print(we3.symbol, end="")
            elif (x == we4.x) and (y == we4.y) and (we4.symbol not in player.weapon_inventory):
                print(we4.symbol, end="")
            else:
                print(char, end="")


            if x == 147 and y == 0:
                print("  ___   ___   ___    ___    _   _ ", end='')
            elif x == 147 and y == 1:
                print(" | __| | __| | _ \  / _ \  | | | |", end='')
            elif x == 147 and y == 2:
                print(" | |   | _|  |  _/ | (_) | | |_| |", end='')
            elif x == 147 and y == 3:
                print(" |_|   |___| |_|    \___/   \__,_| ", end='')
            elif x == 147 and y == 4:
                hero_type = ['Рыцарь', 'Лучник', 'Викинг', 'Oхотник']
                print(f"   Герой: {hero_type[int(player_choice_num) - 1]}", end='')
            elif x == 147 and y == 5:
                print(f"   HP: {player.hp} / {player.static_hp}", end='')
            elif x == 147 and y == 6:
                print(f"   DMG: {player.dmg} / {player.static_dmg}", end='')


            elif x == 147 and y == 8:
                print("  _   _   _  _   ___   ___   _  _   _____    _     ___   _    ", end='')
            elif x == 147 and y == 9:
                print(" | | | | | || | | _ ) | __| | || | |_   _|  /_\   | _ \ | |__ ", end='')
            elif x == 147 and y == 10:
                print(" | |_| | | __ | | _ \ | _|  | __ |   | |   / _ \  |  _/ | '_ ", end='')
            elif x == 147 and y == 11:
                print("  \__,_| |_||_| |___/ |___| |_||_|   |_|  /_/ \_\ |_|   |_.__/", end='')
            elif x == 147 and y == 12:
                if len(player.weapon_inventory) != 0:
                    wee = {'|': 'Меч', ')': 'Лук', 'Г': 'Топор', 'L': 'Ружьё'}
                    print(f"Оружие: {wee[player.weapon_inventory[0]]}", end='')
                else:
                    print("Оружие: ")
            elif x == 147 and y == 13:
                print(f"Броня: ", end='')
            elif x == 147 and y == 14:
                print(f"Зелье 1: ", end='')
            elif x == 147 and y == 15:
                print(f"Зелье 2: ", end='')


            #if x == 147 and y == 0:
            #    print("  __  __    ___    _  _    ___   _____   ___   _    _ ", end='')
            #elif x == 147 and y == 1:
            #    print(' |  \/  |  / _ \  | || |  / __| |_   _| | _ \ | |__| |', end='')
            #elif x == 147 and y == 2:
            #    print(" | |\/| | | (_) | | __ | | (__    | |   |  _/ | '_ \ |", end='')
            #elif x == 147 and y == 3:
            #    print(" |_|  |_|  \___/  |_||_|  \___|   |_|   |_|   |_.__/_|", end='')


            #elif x == 147 and y == 13:
            #    print(f'   enemy 1  [HP: {en1.hp}/{en1.static_hp}   DMG: {en1.dmg}]', end='')
            #elif x == 147 and y == 14:
            #    print(f'   enemy 2  [HP: {en2.hp}/{en2.static_hp}   DMG: {en2.dmg}]', end='')
            #elif x == 147 and y == 15:
            #    print(f'   enemy 3  [HP: {en3.hp}/{en3.static_hp}   DMG: {en3.dmg}]', end='')
            #elif x == 147 and y == 16:
            #    print(f'   enemy 4  [HP: {en4.hp}/{en4.static_hp}   DMG: {en4.dmg}]', end='')
            #elif x == 147 and y == 17:
            #    print(f'   enemy 5  [HP: {en5.hp}/{en5.static_hp}   DMG: {en5.dmg}]', end='')
            #elif x == 147 and y == 18:
            #    print(f'   enemy 6  [HP: {en6.hp}/{en6.static_hp}   DMG: {en6.dmg}]', end='')
            #elif x == 147 and y == 19:
            #    print(f'   enemy 7  [HP: {en7.hp}/{en7.static_hp}   DMG: {en7.dmg}]', end='')
            #elif x == 147 and y == 20:
            #    print(f'   enemy 8  [HP: {en8.hp}/{en8.static_hp}   DMG: {en8.dmg}]', end='')
            #elif x == 147 and y == 21:
            #    print(f'   enemy 9  [HP: {en9.hp}/{en9.static_hp}   DMG: {en9.dmg}]', end='')
            #elif x == 147 and y == 22:
            #    print(f'   enemy 10 [HP: {en10.hp}/{en10.static_hp}   DMG: {en10.dmg}]', end='')







        print()
###########################################################################################################
list_history = []

if len(list_history) > 3:
    list_history.remove(list_history[3])

def add_to_history(text:str):
    list_history.append(text)

def print_history(index:int) -> list:
    print(list_history[index])
###########################################################################################################
class Game:
    def __init__(self, player):
        self.player = player


    def play(self):
        while True:
            os.system('CLS')
            if (player.hp > 0):
                if (player.x == en1.x and player.y == en1.y and en1.hp > 0):
                    en1.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en1.dmg)
                    add_to_history("Монстр ударил Вас")
                elif (player.x == en2.x and player.y == en2.y and en2.hp > 0):
                    en2.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en2.dmg)
                    add_to_history("Монстр ударил Вас")
                elif (player.x == en3.x and player.y == en3.y and en3.hp > 0):
                    en3.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en3.dmg)
                    add_to_history("Монстр ударил Вас")
                elif (player.x == en4.x and player.y == en4.y and en4.hp > 0):
                    en4.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en4.dmg)
                    add_to_history("Монстр ударил Вас")
                elif (player.x == en5.x and player.y == en5.y and en5.hp > 0):
                    en5.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en5.dmg)
                    add_to_history("Монстр ударил Вас")
                elif (player.x == en6.x and player.y == en6.y and en6.hp > 0):
                    en6.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en6.dmg)
                    add_to_history("Монстр ударил Вас")
                elif (player.x == en7.x and player.y == en7.y and en7.hp > 0):
                    en7.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en7.dmg)
                    add_to_history("Монстр ударил Вас")
                elif (player.x == en8.x and player.y == en8.y and en8.hp > 0):
                    en8.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en8.dmg)
                    add_to_history("Монстр ударил Вас")
                elif (player.x == en9.x and player.y == en9.y and en9.hp > 0):
                    en9.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en9.dmg)
                    add_to_history("Монстр ударил Вас")
                elif (player.x == en10.x and player.y == en10.y and en10.hp > 0):
                    en10.hit(player.dmg)
                    add_to_history("Вы ударили Монстра")
                    player.hit(en10.dmg)


                if len(list_history) > 0:
                    print_history(0)
                    if len(list_history) > 1:
                        print_history(1)
                        if len(list_history) > 2:
                            print_history(2)


                print_level_with_player()


                if len(player.weapon_inventory) != 0:
                    weapons = {'|': 'Меч',
                               ')': 'Лук',
                               'Г': 'Топор',
                               'L': 'Ружьё'}
                    weee = list(x for x in player.weapon_inventory)
                    if weee:
                        print("\nWeapon:", weapons[weee[0]])

                move = input('\t\tКуда идём [ W / A / S / D ]: ').lower()

                while (move not in ('w', 'a', 's', 'd', 'ц', 'ф', 'ы', 'в')) or (move == '') or (move == ' '):
                    os.system('CLS')

                    if len(list_history) > 0:
                        print_history(0)
                        if len(list_history) > 1:
                            print_history(1)
                            if len(list_history) > 2:
                                print_history(2)

                    print_level_with_player()

                    move = input('\t\tКуда идём [ W / A / S / D ]: ').lower()
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
player_choice_num = input('Ваш выбор [ 1 / 2 / 3 / 4 ]: ')
while player_choice_num not in ('1', '2', '3', '4'):
    os.system('CLS')
    choose_hero_menu()
    player_choice_num = input('Ваш выбор [ 1 / 2 / 3 / 4 ]: ')
else:
    if player_choice_num == '1':
        player = Knight(4, 1)
        os.system('CLS')
    elif player_choice_num == '2':
        player = Archer(4, 1)
        os.system('CLS')
    elif player_choice_num == '3':
        player = Viking(4, 1)
        os.system('CLS')
    elif player_choice_num == '4':
        player = Hunter(4, 1)
        os.system('CLS')
###########################################################################################################
en1 = Enemy(40, 3)
en2 = Enemy(10, 27)
en3 = Enemy(67, 31)
en4 = Enemy(66, 8)
en5 = Enemy(6, 46)
en6 = Enemy(102, 43)
en7 = Enemy(87, 23)
en8 = Enemy(100, 10)
en9 = Enemy(138, 3)
en10 = Enemy(134, 48)

we1 = Weapon(4, 3, '|')
we2 = Weapon(4, 4, ')')
we3 = Weapon(4, 5, 'Г')
we4 = Weapon(4, 6, 'L')

game = Game(player)
game.play()
###########################################################################################################