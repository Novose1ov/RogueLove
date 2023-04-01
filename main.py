from big_latters import Start_game
import os


class Heroes:
    def __init__(self):
        self.sign = '@'
        self.hp = 4
        self.damage = 4


class Knight(Heroes):
    def __init__(self):
        Heroes.__init__(self)
        self.hp = 5
        self.damage = 3

        print('The Knight was created [HP: 5 | DMG: 3]')


class Archer(Heroes):
    def __init__(self):
        Heroes.__init__(self)
        self.hp = 3
        self.damage = 5
        print('The Archer was created [HP: 3 | DMG: 5]')

class Wizard(Heroes):
    def __init__(self):
        Heroes.__init__(self)
        self.hp = 6
        self.damage = 2
        print('The Wizard was created [HP: 6 | DMG: 2]')

class Goblin(Heroes):
    def __init__(self):
        Heroes.__init__(self)
        self.hp = 2
        self.damage = 6
        print('The Goblin was created [HP: 2 | DMG: 6]')

print("""
        Ты отправился в странствие навстречу приключениям и опасностям.
        Удачного путешествия!
""")

print(
    """
                ВЫБЕРИТЕ ПЕРСОНАЖА:                    
  1. Рыцарь  |  2. Лучник  |  3. Маг     |  4. Гоблин  
    HP: 5    |    HP: 3    |    HP: 6    |    HP: 2    
    DMG: 3   |    DMG: 5   |    DMG: 2   |    DMG: 6   
                                                       """)


player_choice_num = int(input('Ваш выбор [1 / 2 / 3 / 4]: '))


while player_choice_num not in (1, 2, 3, 4):
    print('Некорректный ввод, попробуйте ещё раз:')
    player_choice_num = int(input('Ваш выбор [1 / 2 / 3 / 4]: '))

else:
    if player_choice_num == 1:
        player_class = Knight()
        input()
        os.system('CLS')
        
    elif player_choice_num == 2:
        player_class = Archer()
        input()
        os.system('CLS')
        
    elif player_choice_num == 3:
        player_class = Wizard()
        input()
        os.system('CLS')
        
    elif player_choice_num == 4:
        player_class = Goblin()
        input()
        os.system('CLS')

