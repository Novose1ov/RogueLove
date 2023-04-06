import os
import time

def new_game():
    out_purple(
        """
          /$$             /$$   /$$                                                                          
         /$$$$            | $$$ | $$                                                                          
        |_  $$            | $$$$| $$  /$$$$$$  /$$  /$$  /$$        /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
          | $$            | $$ $$ $$ /$$__  $$| $$ | $$ | $$       /$$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$
          | $$            | $$  $$$$| $$$$$$$$| $$ | $$ | $$      | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
          | $$            | $$\  $$$| $$_____/| $$ | $$ | $$      | $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/
         /$$$$$$ /$$      | $$ \  $$|  $$$$$$$|  $$$$$/$$$$/      |  $$$$$$$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
        |______/|__/      |__/  \__/ \_______/ \_____/\___/        \____  $$ \_______/|__/ |__/ |__/ \_______/
                                                                   /$$  \ $$                                  
                                                                  |  $$$$$$/                                  
                                                                   \______/                                   
          /$$$$$$            /$$$$$$$$           /$$   /$$                                                    
         /$$__  $$          | $$_____/          |__/  | $$                                                    
        |__/  \ $$          | $$       /$$   /$$ /$$ /$$$$$$                                                  
          /$$$$$$/          | $$$$$   |  $$ /$$/| $$|_  $$_/                                                  
         /$$____/           | $$__/    \  $$$$/ | $$  | $$                                                    
        | $$                | $$        >$$  $$ | $$  | $$ /$$                                                
        | $$$$$$$$ /$$      | $$$$$$$$ /$$/\  $$| $$  |  $$$$/                                                
        |________/|__/      |________/|__/  \__/|__/   \___/                                                  
        
        """
    )


def out_yellow(text):
    print("\033[33m {}".format(text))

def out_green(text):
    print("\033[32m {}".format(text))

def out_blue(text):
    print("\033[34m\033[1m {}".format(text))

def out_purple(text):
    print("\033[35m {}".format(text))

def out_red(text):
    print("\033[31m {}".format(text))


os.system("CLS")
new_game()
i = input("Выберите 1/2:")
while i not in ('1', '2'):
    os.system("CLS")
    i = input("Выберите 1/2:")
else:
    if i == '1':
        os.system("CLS")
        stroke = '''ОДНАЖДЫ В УШЕДШЕМ МИРЕ, ГДЕ МАГИЯ И ТЕХНОЛОГИИ ПЕРЕПЛЕЛИСЬ ВМЕСТЕ, БЫЛ СОЗДАН МОГУЩЕСТВЕННЫЙ АРТЕФАКТ - КРИСТАЛЛ ВСЕЛЕННОЙ.
        ЭТОТ КРИСТАЛЛ ИМЕЛ СПОСОБНОСТЬ КОНТРОЛИРОВАТЬ СИЛЫ ПРИРОДЫ И ДАВАТЬ ВЛАДЕЛЬЦУ НЕОГРАНИЧЕННУЮ МОЩЬ.
            В ОДИН ДЕНЬ КРИСТАЛЛ РАЗДРОБИЛСЯ НА МНОЖЕСТВО МЕЛКИХ ЧАСТЕЙ И БЫЛ РАЗБРОСАН ПО ВСЕМУ МИРУ.
        ТЕПЕРЬ МНОГИЕ ЛЮДИ СТРЕМЯТСЯ НАЙТИ ЭТИ ЧАСТИ И ПОЛУЧИТЬ БЕСПРЕДЕЛЬНУЮ ВЛАСТЬ.
            МНЕ НУЖЕН БЫЛ ЭТОТ КРИСТАЛЛ, ЧТОБЫ ВЫЛЕЧИТЬ СВОЮ СЕМЬЮ ОТ НЕИЗЛЕЧИМОЙ БОЛЕЗНИ.
        НО ДОСТАТЬ ЭТОТ КРИСТАЛЛ БЫЛО НЕ ТАК-ТО И ПРОСТО, ВЕДЬ ЛЕС, В КОТОРОМ ВИДЕЛИ ЕГО ОСКОЛКИ, ПОХОЖ НА НЕПРОХОДИМЫ ЛАБИРИНТ, ПО КОТОРОМУ БРОДЯТ МОНСТРЫ.'''

        def print_text(stroke):
            for i in range(len(stroke)):
                print(stroke[i], end="")
                time.sleep(0.005)
        print_text(stroke)

#         out_green(
#             """
#    ___           _  _         __   __         _    _     ___                                                                                             __
#   / _ \   __ _  | || |  __ _  \ \|/ /  __ _  | |__| |   | _ )    _  _  __ __ __  ___   __ _  __ __ __  ___   _ __      _ __    _  _   _ __   ___        | _|  __ _   ___
#  | (_) | / _` | | __ | / _` |  > | <  / _` | | '_ \ |   | _ \   | || | \ V  V / / -_) / _` | \ V  V / / -_) | '  \    | '  \  | || | | '_ \ / -_)  _    | |  / _` | / -_)
#   \___/  \__, | |_||_| \__,_| /_/|\_\ \__, | |_.__/_|   |___/    \_, |  \____/  \___| \__, |  \____/  \___| |_|_|_|   |_|_|_|  \_,_| | .__/ \___| ( )   | |  \__, | \___|
#          |___/     __          ___    |___/      _____           |__/_  _           _ |___/     __                                   |_|          |/     _   |___/     _                 _         ___                      _____                __   _    _     _                  ____                _  _                    __                               _____   ___         _  _   _  _   _    _    __                     _____             _              _     _____                  _  __                     _____            _       _        ___                _           _  _   _  _          __
#     _ __    __ _  | _|  _  _  / _ |     _  _    |_   _|  ___  __ __ | || |  ___    / \    ___  | _|  _  _   _  _      _ _    ___   _ __   ___   _ _     / \    ___    / \    _  _   __  | |__     | _ )  _ __    ___   __  |_   _|  ___         / /  | |__| |   /_\      __   ___  |__ /  __ _   __ _  | || |     _ __    ___  | _|  _  _  __ __ __   ___   __  |_   _| | _ )  ___  | || | | || | | |__| |  _  _      __ _   _ __  |_   _|  ___   ___| |___   __ _  | |__ |_   _|     _______    | |/ /  _ __   _  _   __  |_   _|  __ _    / \     / \      | _ )  __   ___    / \    ___  | || | | || |  ___   _  _
#    | '  \  / _` | | |  | || | \   |    | || |     | |   / -_) \ \ / | __ | / _ \  / | \  / _ \ | |  | || | | || |    | ' \  / -_) | '_ \ / -_) | ' \   / | \  / -_)  / | \  | || | / _| | '_ \    | _ \ | '  \  / -_) / _|   | |   / -_)  _    / _ \ | '_ \ |  / _ \    / _| / _ \  |_ \ / _` | / _` | | __ |    | '  \  / _ \ | |  | || | \ V  V /  / -_) / _|   | |   | _ \ / -_) | __ | | __ | | '_ \ | | || |    / _` | | '_ \   | |   / -_) / _ \ / _ \ / _` | | / /   | |      |_______|   | ' <  | '_ \ | || | / _|   | |   / _` |  / | \   / | \     | _ \ / _| / -_)  / | \  / -_) | __ | | __ | / _ \ | || |  _
#    |_|_|_| \__,_| |_|   \_,_| /_|_|     \_,_|     |_|   \___| /_\_\ |_||_| \___/ /_/ \_\ \___/ |_|   \_,_|  \_,_|    |_||_| \___| | .__/ \___| |_||_| /_/ \_\ \___| /_/ \_\  \_,_| \__| |_.__/    |___/ |_|_|_| \___| \__|   |_|   \___| ( )   \___/ |_.__/_| /_/ \_\   \__| \___/ |___/ \__, | \__,_| |_||_|    |_|_|_| \___/ |_|   \_, |  \____  ) \___| \__|   |_|   |___/ \___| |_||_| |_||_| |_.__/_|  \_,_|    \__,_| | .__/   |_|   \___| \___/ \___/ \__,_| |_\_\   |_|                  |_|\_\ | .__/  \_,_| \__|   |_|   \__,_| /_/ \_\ /_/ \_\    |___/ \__| \___| /_/ \_\ \___| |_||_| |_||_| \___/  \_,_| (_)
#
#   ___   _____    ___    _____      _                        _____            _       _                               _                                      __   _  _              _____   _         _           _  _   _____                  _                         ___          _____   _                       _     _    _                                               _    _                              ___          _____   _                     ____  ___          _  _             _  _               __                 _  _          _ _          _  _   _  _          _    ___                               _
#  |__ \ |_   _|  / _ \  |_   _|    | |__  _ __   _  _   __  |_   _|  __ _    / \     / \       _  _   _ __    ___    / \       __   _ _    ___   __   ___   / /  | || |  ___   __  |_   _| | |__     | |__  ___  | || | |_   _|  _ __   ___    / \    _  _   _ __   ___  | _ )  __ _  |_   _| | |__      __   _  _    / \   | |__| |     _ _    _ __   _  _   _ __   ___   __ _  | |__| |     _  _      __ _   __ _  | _ )  __ _  |_   _| | |__     __ __  ___  |__ / / _ |  _  _  | || |  _  _     | || |  ___   ___  | _|  _ __   __ _  | || |  _  _  | | |   ___  | || | | || |  _  _  | |_ / _ \      _ __    ___  __ __ __  | |__
#   |_ |   | |   | (_) |   | |      | / / | '_ \ | || | / _|   | |   / _` |  / | \   / | \     | || | | '  \  / -_)  / | \     / _| | ' \  / _ \ / _| / _ \ / _ \ | __ | / _ \ / _|   | |   | '_ \    | / / / _ \ | __ |   | |   | '_ \ / _ \  / | \  | || | | '_ \ / _ \ | _ \ / _` |   | |   | '_ \    / _| | || |  / | \  | '_ \ |    | ' \  | '_ \ | || | | '_ \ / _ \ / _` | | '_ \ |    | || |    / _` | / _` | | _ \ / _` |   | |   | '_ \    \ \ / / _ \  |_ \ \   | | || | | __ | | || |    | __ | / -_) / _ \ | |  | '_ \ / _` | | __ | | || | |_  |  / -_) | __ | | __ | | || | | |_| (_) |    | '  \  / _ \ \ V  V /  | '_ \  _
#  |___/   |_|    \___/    |_|      |_\_\ | .__/  \_,_| \__|   |_|   \__,_| /_/ \_\ /_/ \_\     \_,_| |_|_|_| \___| /_/ \_\    \__| |_||_| \___/ \__| \___/ \___/ |_||_| \___/ \__|   |_|   |_.__/    |_\_\ \___/ |_||_|   |_|   | .__/ \___/ /_/ \_\  \_,_| | .__/ \___/ |___/ \__,_|   |_|   |_.__/    \__|  \_,_| /_/ \_\ |_.__/_|    |_||_| | .__/  \_,_| | .__/ \___/ \__, | |_.__/_|     \_,_|    \__, | \__,_| |___/ \__,_|   |_|   |_.__/    /_\_\ \___/ |___/ /_|_|  \_,_| |_||_|  \_, |    |_||_| \___| \___/ |_|  | .__/ \__,_| |_||_|  \_,_|   |_|  \___| |_||_| |_||_|  \_, | |_|  \___/     |_|_|_| \___/  \____  ) |_.__/ (_)
#                                         |_|                                                                                                                                                                                    |_|                         |_|                                                                                |_|           |_|          |___/                        |___/                                                                               |__/                             |_|                                                     |__/                                     |/
#
#   _  _            ___                          _  _                   _  _   _         _                        _____            _       _                      ____                       __            _          ___      _  _                     _  _                          _____   ___                            _     _                                _             _     _           ___                 __   _    _     _                      ____   __                            _  _                      ___
#  | || |  ___     | _ )     ___   __ _   _  _  | || |     __ _   ___  | || | | |__     | |__  _ __   _  _   __  |_   _|  __ _    / \     / \       _ __   __ _  |__ /  __ _   _ __   ___   / /   _  _    / \    __  / _ |    | || |  __ _      _ __   | || |  ___  __ __  ___   __  |_   _| | _ )  ___      _ __    ___    / \   | |__  _  _  __ __     ___   __  | |__  ___    / \   | |__  ___  | _ )     _  _      / /  | |__| |   / \       _ __   __ _  |__ /  / /   _ __   ___   __   __ _  | || |     _ _    ___     | _ )  __   ___   _ __    _  _      _ __    _  _   _ __   _  _
#  | __ | / _ \    | _ \    / _ \ / _` | | || | | __ |    / _` | / -_) | __ | | '_ \    | / / | '_ \ | || | / _|   | |   / _` |  / | \   / | \     | '_ \ / _` |  |_ \ / _` | | '_ \ / _ \ / _ \ | || |  / | \  / _| \   |    | __ | / _` |    | '  \  | __ | / _ \ \ \ / / -_) / _|   | |   | _ \ / _ \    | '  \  / -_)  / | \  | / / | || | \ \ /    / _ \ / _| | / / / _ \  / | \  | / / / _ \ | _ \    | || |    / _ \ | '_ \ |  / | \     | '_ \ / _` |  |_ \ / _ \ | '_ \ / _ \ / _| / _` | | __ |    | ' \  / _ \    | _ \ / _| / -_) | '  \  | || |    | '  \  | || | | '_ \ | || |  _
#  |_||_| \___/    |___/    \___/ \__, |  \_,_| |_||_|    \__, | \___| |_||_| |_.__/    |_\_\ | .__/  \_,_| \__|   |_|   \__,_| /_/ \_\ /_/ \_\    | .__/ \__,_| |___/ \__, | | .__/ \___/ \___/  \_,_| /_/ \_\ \__| /_|_|    |_||_| \__,_|    |_|_|_| |_||_| \___/ /_\_\ \___| \__|   |_|   |___/ \___/    |_|_|_| \___| /_/ \_\ |_\_\  \_,_| /_\_\    \___/ \__| |_\_\ \___/ /_/ \_\ |_\_\ \___/ |___/     \_,_|    \___/ |_.__/_| /_/ \_\    | .__/ \__,_| |___/ \___/ | .__/ \___/ \__| \__,_| |_||_|    |_||_| \___/    |___/ \__| \___| |_|_|_|  \_, |    |_|_|_|  \_,_| | .__/  \_, | (_)
#                                 |___/                   |___/                               |_|                                                  |_|                 |___/  |_|                                                                                                                                                                                                                                                               |_|                       |_|                                                                          |__/                    |_|     |__/
#
#   _____                             _                 _  _                                 _     _    ___                          _____                        ___   _____        ___      _  _           __    _____                                       _            _  _          _____   _          __                                                 _     _      _  _          _    ___       ___     _                 _____   _
#  |_   _|  ___   _ _    ___   _ __  | |__      _ __   | || |  ___   _ _   _  _   ___       / \   | |_ / _ \   __ _   _  _      __  |_   _|  _ __   ___   _ __   / _ | |_   _|  __  / _ |    | || |  __ _   _  _  |_   _|  _  _      _  _      _ _     ___    / \    _  _  | || |  _  _  |_   _| | |__      / /   ___   __   _ _    _ __   ___   __ _   ___    /_\   | |__  | || |  _  _  | |_ / _ \     | _ )   / \    __ _   __  |_   _| | |__
#    | |   / -_) | ' \  / -_) | '_ \ | '_ \    | '  \  | __ | / _ \ | '_| | || | / -_)     / | \  | |_| (_) | / _` | | || |    / _|   | |   | '_ \ / -_) | '  \  \   |   | |   / _| \   |    | __ | / _` | | || |   | |   | || |    | || |    | ' \   / _ \  / | \  | || | |___ | | || |   | |   | '_ \    / _ \ / -_) / _| | ' \  | '_ \ / -_) / _` | / -_)  / _ \  | '_ \ | __ | | || | | |_| (_) |    | _ \  / | \  / _` | / _|   | |   | '_ \  _
#    |_|   \___| |_||_| \___| | .__/ |_.__/    |_|_|_| |_||_| \___/ |_|    \_,_| \___|    /_/ \_\ |_|  \___/  \__, |  \_,_|    \__|   |_|   | .__/ \___| |_|_|_| /_|_|   |_|   \__| /_|_|    |_||_| \__,_|  \_,_|   |_|    \_,_|     \_,_|    |_||_|  \___/ /_/ \_\  \_, |    |_|  \_,_|   |_|   |_.__/    \___/ \___| \__| |_||_| | .__/ \___| \__, | \___| /_/ \_\ |_.__/ |_||_|  \_, | |_|  \___/     |___/ /_/ \_\ \__,_| \__|   |_|   |_.__/ (_)
#                             |_|                                                                             |___/                         |_|                                                                                                                      |__/                                                          |_|          |___/                               |__/
#
#   __  __   _  _            _  _                      _  _       __   _    _     _       ____  _____         _____      _  __                     _____            _       _          _  _   _____          __   _    _      ___   _    _     _           _  _          _____   _              ___         _    ___                         _      _    ___            _____       _  _                ____    _           _  _                         __        __           _           ____  _  _
#  |  \/  | | || |  ___     | || |  _  _  __ __  ___  | || |     / /  | |__| |   /_\     |__ / |_   _|  ___  |_   _|    | |/ /  _ __   _  _   __  |_   _|  __ _    / \     / \        | || | |_   _|  ___   / /  | |__| |    | _ ) | |__| |   / \    ___  | || |  _  _  |_   _| | |__      __  | _ )  ___  | |_ / _ \     __   ___   _ __   | |__  | |_ / _ \     ___  |_   _|     | || |  ___   _  _  |__ /   / \    ___  | || |  _  _   _ __    ___   _  _      / /   ___    / \    ___  |__ / | || |  _  _
#  | |\/| | | __ | / -_)    | __ | | || | \ \ / / -_) | __ |    / _ \ | '_ \ |  / _ \     |_ \   | |   / _ \   | |      | ' <  | '_ \ | || | / _|   | |   / _` |  / | \   / | \   _   |___ |   | |   / _ \ / _ \ | '_ \ |    | _ \ | '_ \ |  / | \  / -_) |___ | | || |   | |   | '_ \    / _| | _ \ / _ \ | |_| (_) |   / _| / -_) | '  \  | '_ \ | |_| (_) |   / _ \   | |       | __ | / -_) | || |  |_ \  / | \  / -_) |___ | | || | | '  \  / _ \ | || |    / _ \ / _ \  / | \  / -_)  |_ \ | __ | | || |  _
#  |_|  |_| |_||_| \___|    |_||_|  \_, | /_\_\ \___| |_||_|    \___/ |_.__/_| /_/ \_\   |___/   |_|   \___/   |_|      |_|\_\ | .__/  \_,_| \__|   |_|   \__,_| /_/ \_\ /_/ \_\ ( )     |_|   |_|   \___/ \___/ |_.__/_|    |___/ |_.__/_| /_/ \_\ \___|    |_|  \_,_|   |_|   |_.__/    \__| |___/ \___/ |_|  \___/    \__| \___| |_|_|_| |_.__/ |_|  \___/    \___/   |_|       |_||_| \___|  \_,_| |___/ /_/ \_\ \___|    |_|  \_,_| |_|_|_| \___/  \_,_|    \___/ \___/ /_/ \_\ \___| |___/ |_||_|  \_,_| (_)
#                                   |__/                                                                                       |_|                                               |/
#
#   _  _                              _____          _____   _               __             __   _    _     _              _  _            _____          _           _____                                               _____         _       _                       ___      _           _____                                 ___                         _                     __                       _             _     _                                                       _  _             _  _                                                               _    _    __         _             __                        _  _   _____                          _  __        _____                                         __                       ___   _____                     _  _        _____          _    _
#  | || |  ___      __ _   ___   __  |_   _|  __ _  |_   _| | |__      ___  | _|  ___      / /  | |__| |   / \    ___     | || |  ___     |_   _|  __ _  | |__  ___  |_   _|  ___      _  _      _ _    _ __   ___   __  |_   _|  ___  (_)     / \    ___   __         | _ )    | |__  ___  |_   _|  ___   _ __   ___   _ __      | _ )  _  _   __ _   ___    / \    _  _      ___  | _|  ___      ___   __  | |__  ___    / \   | |__  _  _          _ _    ___  __ __  ___  __   __    | || |  __ _     | || |  ___   _ _    _ __   ___  __ __  ___   __ _   _  _   _ __   | |__| |  _  _       / \    __ _   / /   _  _   _ __   _  _  | || | |_   _|         _ _    ___     | |/ /  ___  |_   _|  ___   _ __   ___   _ __    _  _      / /   _ __   ___   __ _  / _ | |_   _|      _ __    ___  | || |  __  |_   _|  _ __  | |__| |
#  | __ | / _ \    / _` | / _ \ / _|   | |   / _` |   | |   | '_ \    / -_) | |  / _ \    / _ \ | '_ \ |  / | \  / _ \    | __ | / -_)      | |   / _` | | / / |___|   | |   / _ \    | || |    | ' \  | '_ \ / _ \ / _|   | |   / _ \  _     / | \  / -_) / _|  _     | _ \    | / / / _ \   | |   / _ \ | '_ \ / _ \ | '  \     | _ \ | || | / _` | / -_)  / | \  | || |    / -_) | |  / _ \    / _ \ / _| | / / / _ \  / | \  | / / | || |  _     | ' \  / _ \ \ \ / / _ \ \ \|/ /    | __ | / _` |    | __ | / -_) | ' \  | '_ \ / _ \ \ \ / / _ \ / _` | | || | | '  \  | '_ \ | | || |     / | \  / _` | / _ \ | || | | '_ \ | || | | __ |   | |    _     | ' \  / _ \    | ' <  / _ \   | |   / _ \ | '_ \ / _ \ | '  \  | || |    / _ \ | '_ \ / _ \ / _` | \   |   | |       | '  \  / _ \ | __ | / _|   | |   | '_ \ | '_ \ |  _
#  |_||_| \___/    \__, | \___/ \__|   |_|   \__,_|   |_|   |_.__/    \___| |_|  \___/    \___/ |_.__/_| /_/ \_\ \___/    |_||_| \___|      |_|   \__,_| |_\_\         |_|   \___/     \_,_|    |_||_| | .__/ \___/ \__|   |_|   \___/ (_)   /_/ \_\ \___| \__| ( )    |___/    |_\_\ \___/   |_|   \___/ | .__/ \___/ |_|_|_|    |___/  \_,_| \__, | \___| /_/ \_\  \_,_|    \___| |_|  \___/    \___/ \__| |_\_\ \___/ /_/ \_\ |_\_\  \_,_| ( )    |_||_| \___/ /_\_\ \___/ /_/|\_\    |_||_| \__,_|    |_||_| \___| |_||_| | .__/ \___/ /_\_\ \___/ \__, |  \_,_| |_|_|_| |_.__/_|  \_,_|    /_/ \_\ \__,_| \___/  \_,_| | .__/  \_,_| |_||_|   |_|   ( )    |_||_| \___/    |_|\_\ \___/   |_|   \___/ | .__/ \___/ |_|_|_|  \_, |    \___/ | .__/ \___/ \__, | /_|_|   |_|       |_|_|_| \___/ |_||_| \__|   |_|   | .__/ |_.__/_| (_)
#                  |___/                                                                                                                                                                               |_|                                                      |/                                        |_|                                  |___/                                                                                          |/                                                                              |_|                      |___/                                                                |_|                          |/                                                |_|                   |__/           |_|          |___/                                                      |_|
#             """
# )

        input()
        os.system("CLS")
        out_yellow(
            """
                  /$$$$$$  /$$                                                                                                                                             
                 /$$__  $$| $$                                                                                                                                             
                | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$         /$$$$$$                                                                                
                | $$      | $$__  $$ /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$       |____  $$                                                                               
                | $$      | $$  \ $$| $$  \ $$| $$  \ $$|  $$$$$$ | $$$$$$$$        /$$$$$$$                                                                               
                | $$    $$| $$  | $$| $$  | $$| $$  | $$ \____  $$| $$_____/       /$$__  $$                                                                               
                |  $$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/ /$$$$$$$/|  $$$$$$$      |  $$$$$$$                                                                               
                 \______/ |__/  |__/ \______/  \______/ |_______/  \_______/       \_______/                                                                               
    
                                                            /$$                                                /$$                              
                                                            | $$                                               | $$                              
                                                    /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       
                                                   /$$_____/| $$__  $$ |____  $$ /$$__  $$|____  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      
                                                  | $$      | $$  \ $$  /$$$$$$$| $$  \__/ /$$$$$$$| $$        | $$    | $$$$$$$$| $$  \__/      
                                                  | $$      | $$  | $$ /$$__  $$| $$      /$$__  $$| $$        | $$ /$$| $$_____/| $$            
                                                  |  $$$$$$$| $$  | $$|  $$$$$$$| $$     |  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$            
                                                   \_______/|__/  |__/ \_______/|__/      \_______/ \_______/   \___/   \_______/|__/            
    
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                                          
                  __      _   __      _       _     _                    #############            _____        ___           _                
                 /  |    | | / /     (_)     | |   | |                   #############           / __  \      / _ \         | |               
                 `| |    | |/ / _ __  _  __ _| |__ | |_                  #############           `'  / /'    / /_\ \_ __ ___| |__   ___ _ __  
                  | |    |    \| '_ \| |/ _` | '_ \| __|                 #############              / /      |  _  | '__/ __| '_ \ / _ \ '__| 
                 _| |__  | |\  \ | | | | (_| | | | | |_                  #############            ./ /____   | | | | | | (__| | | |  __/ |    
                 \___(_) \_| \_/_| |_|_|\__, |_| |_|\__|                 #############            \_____(_)  \_| |_/_|  \___|_| |_|\___|_|    
                                         __/ |                           #############                            
                                        |___/                            #############                            
                                                                         #############
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                         _  _ ___    _   _  __                           #############                      _  _ ___   _   ____  
                        | || | _ \  (_) / |/  \                          #############                     | || | _ \ (_) |__  | 
                        | __ |  _/   _  | | () |                         #############                     | __ |  _/  _    / /  
                  ___  _|_||_|_|__  (_) |_|\__/                          #############              ___  __|_||_|_|_  (_)  /_/   
                 |   \|  \/  |/ __| (_) |_  )                            #############             |   \|  \/  |/ __| (_) | __|  
                 | |) | |\/| | (_ |  _   / /                             #############             | |) | |\/| | (_ |  _  |__ \  
                 |___/|_|  |_|\___| (_) /___|                            #############             |___/|_|  |_|\___| (_) |___/  
                                                                         #############  
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                      
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                         
                  _____    _   _             _                           #############               ___     _   _ _ _    _                
                 |____ |  | | | |           | |                          #############              /   |   | | | (_) |  (_)               
                     / /  | |_| |_   _ _ __ | |_ ___ _ __                #############             / /| |   | | | |_| | ___ _ __   __ _    
                     \ \  |  _  | | | | '_ \| __/ _ \ '__|               #############            / /_| |   | | | | | |/ / | '_ \ / _` |   
                 .___/ /  | | | | |_| | | | | ||  __/ |                  #############            \___  |_  \ \_/ / |   <| | | | | (_| |   
                 \____(_) \_| |_/\__,_|_| |_|\__\___|_|                  #############                |_(_)  \___/|_|_|\_\_|_| |_|\__, |   
                                                                         #############                                             __/ |   
                                                                         #############                                            |___/  
                                                                         #############                                                        
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                         _  _ ___    _   ___                             #############                        _  _ ___   _   ___      
                        | || | _ \  (_) ( _ )                            #############                       | || | _ \ (_) / _ \     
                        | __ |  _/   _  / _ \                            #############                       | __ |  _/  _  \_, /     
                  ___  _|_||_|_|__  (_) \___/                            #############                ___  _ |_||_|_|_  (_)  /_/  ____
                 |   \|  \/  |/ __| (_) | | |                            #############               |   \|  \/  |/ __| (_) |__ /
                 | |) | |\/| | (_ |  _  |_  _|                           #############               | |) | |\/| | (_ |  _   |_ \ 
                 |___/|_|  |_|\___| (_)   |_|                            #############               |___/|_|  |_|\___| (_) |___/
                                                                         #############
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                                                                                                                                                                                                                                                                                                                                                                                              
            """)

#k = input("Сделайте выбор 1/2/3/4:")
# нужно написать весь код
out_purple(
    """
                                         /$$     /$$                                                          /$$
                                        |  $$   /$$/                                                         | $$
                                         \  $$ /$$//$$$$$$  /$$   /$$       /$$  /$$  /$$  /$$$$$$  /$$$$$$$ | $$
                                          \  $$$$//$$__  $$| $$  | $$      | $$ | $$ | $$ /$$__  $$| $$__  $$| $$
                                           \  $$/| $$  \ $$| $$  | $$      | $$ | $$ | $$| $$  \ $$| $$  \ $$|__/
                                            | $$ | $$  | $$| $$  | $$      | $$ | $$ | $$| $$  | $$| $$  | $$    
                                            | $$ |  $$$$$$/|  $$$$$$/      |  $$$$$/$$$$/|  $$$$$$/| $$  | $$ /$$
                                            |__/  \______/  \______/        \_____/\___/  \______/ |__/  |__/|__/                                                                                                                                                                                                                                                                                                                                                                                          
    """)
out_blue(
    """
                                                                   ████████████████████████████
                                                                 ███════███═════█████████████████
                                                               ███══██══██═████═████═══██████═█████
                                                             ███══███══██══████═████═══██████══██████
                                                           ███═══███═══██═█████═████════██████═══█████
                                                          ██═══█████══██══█████═████════███████════█████
                                                        ██════█████═══██══█████═████═════██████═════██████
                                                       █████═════██══██══██████═████═════██████████████████
                                                         ███████════███══██████═████═══██████████████████
                                                          ███═══██████══════════████████████████████████
                                                            ██══█═══█████████████████████████████══███
                                                              ██═███═██═════════██████████████═══████
                                                               ██══██═██══█████═███══════████═══███
                                                                 ██═██═██══████═███═════████══███
                                                                  ██═██═██═████══██════████══███
                                                                    ██═█═██═███══██═══████═███
                                                                      █═█═██═██══██══████═███
                                                                       ██══█══█══██══██████
                                                                         █══█════██═██████
                                                                          ██═█═══███████
                                                                            ███══██████
                                                                             ███═████
                                                                               █████
                                                                                 █
    """)
input()

out_red(
    """
         
                                                             /$$     /$$                        /$$                               /$$
                                                            |  $$   /$$/                       | $$                              | $$
                                                             \  $$ /$$//$$$$$$  /$$   /$$      | $$  /$$$$$$   /$$$$$$$  /$$$$$$ | $$
                                                              \  $$$$//$$__  $$| $$  | $$      | $$ /$$__  $$ /$$_____/ /$$__  $$| $$
                                                               \  $$/| $$  \ $$| $$  | $$      | $$| $$  \ $$|  $$$$$$ | $$$$$$$$|__/
                                                                | $$ | $$  | $$| $$  | $$      | $$| $$  | $$ \____  $$| $$_____/    
                                                                | $$ |  $$$$$$/|  $$$$$$/      | $$|  $$$$$$/ /$$$$$$$/|  $$$$$$$ /$$
                                                                |__/  \______/  \______/       |__/ \______/ |_______/  \_______/|__/
                                                                                                                                     
                                                                                                                                     

                                                                                            ⢀⡄  ⢠⣄  ⢠⡀
                                                                                       ⢀⣶⢤⣠⡞⣭⣧⣼⣹⡎⣧⣼⢭⣳⣄⡤⡶⡄
                                                                                   ⠘⣶⢶⠾⡾⣿⣟⣻⠃⢷⣼⠃⠙⣇⡼⠘⣏⣻⣿⢷⠷⡶⣶⠃
                                                                                     ⢻⣘⣒⣧⣀⣤⣀⣠⣤⣤⣤⣤⣤⣤⣄⣀⣤⣀⣼⣒⣃⡟
                                                                                     ⠈⡿⢟⠋⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠙⠻⣿⠁
                                                                                     ⢰⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⡇
                                                                                     ⢸⡇⠄⠄⠄⠄⣀⣀⣀⠄⢠⡄⠄⣀⣀⣀⠄⠄⠄⠄⢸⡇
                                                                                     ⠸⡇⢸⠎⣠⣤⣤⣤⣌⠑⠄⠄⠊⣠⣤⣤⣤⣄⠑⡇⢸⡇
                                                                                      ⢹⣸⣾⣿⣿⣿⣿⣿⣷⢄⡠⣾⣿⣿⣿⣿⣿⣷⣇⡟
                                                                                       ⢻⠻⠿⣿⣿⣿⡿⠯⣱⣞⠽⢿⣿⣿⣿⡿⠟⡟⠁
                                                                                      ⢰⡻⣌⠙⠋⠉⠁⢩⣶⣿⣿⣦⡍⠈⠉⠙⠋⡁⢙⡶
                                                                                       ⠙⢾⣷⣶⣶⠄⠘⠟⠻⠟⠻⠃⠠⣶⣶⢾⣷⠋
                                                                                        ⢸⠃⢿⣿⢴⡆⣴⣤⣤⣶⣶⣷⣿⣿⠸⡇
                                                                                        ⠺⣦⡈⢿⢽⡗⣸⠄⠄⡇⢸⡏⡿⢃⣴⠿
                                                                                         ⠻⢵⣈⠎⠏⢱⠒⠒⠎⠹⠸⣁⡮⠞
                                                                                           ⠙⢦⡲⠤⠆⠰⠤⢖⣰⠋
                                                                                             ⠙⠛⠉⠉⠛⠋
                                                                                                                                  
    """)

input()