import random


def map_generator(ROWS, COLS):
    mapp = []

    for y in range(ROWS):
        newRow = []
        
        for x in range(COLS):
            if (x == 0) or (x == (COLS-1)) or (random.random() < 0.36):
                newRow.append('#')

            else:
                newRow.append('.')
                
        mapp.append(newRow)

    print('#' * COLS)
    for row in mapp:
        print(''.join([str(elem) for elem in row]))
    print('#' * COLS)
    
map_generator(45, 160)
