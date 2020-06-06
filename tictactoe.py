mat = []
turn = 0
x,y = 0,0
#  Display the Matrix
def display():
    print('---------')
    count = 0
    for row in range(3):
        mat.append([])
        for col in range(3):
            mat[row].append(' ')
            count += 1
    for row in mat:
        print('|',' '.join(row), '|')
    print('---------')
def user_input():
    global turn
    if turn < 9:
        x,y = input('Enter the coordinates:').split()
        if x.isnumeric() and y.isnumeric():
            if x == '1' and y == '1':
                x,y = 2,0
            elif x == '1' and y == '2':
                x,y = 1,0
            elif x == '1' and y == '3':
                x,y = 0,0
            elif x == '2' and y == '1':
                x,y = 2,1
            elif x == '2' and y == '2':
                x,y = 1,1
            elif x == '2' and y == '3':
                x,y = 0,1
            elif x == '3' and y == '1':
                x,y = 2,2
            elif x == '3' and y == '2':
                x,y = 1,2
            elif x == '3' and y == '3':
                x,y = 0,2
            if int(x) in [0,1,2] and int(y) in [0,1,2]:
                if mat[x][y] == '_' or mat[x][y] == ' ':
                    turn += 1
                    if turn % 2 == 0:
                        mat[x][y] = 'O'
                        check_box()
                    else:
                        mat[x][y] = 'X'
                        check_box()
                    print('---------')
                    for row in mat:
                        print('|',' '.join(row), '|')
                    print('---------')
                else:
                    print('This cell is occupied! Choose another one!')
                    user_input()
            else:
                print('Coordinates should be from 1 to 3!')
                user_input()
        else:
            print('You should enter numbers!')
            user_input()
    else:
        print(turn)
        print('Draw')
        return 'Draw'

def check_box():
    col = 0
    for row in range(3):
            if mat[row][col + 0] == 'X' and mat[row][col + 1] == 'X' and mat[row][col + 2] == 'X':
                print('X wins')
                return 'X wins'
            elif mat[row][col + 1] == 'O' and mat[row][col + 2] == 'O' and mat[row][col + 0] == 'O':
                print('O wins')
                return 'O wins'
            elif mat[1][1] == 'O' and mat[2][2] == 'O' and mat[0][0] == 'O':
                print('O wins')
                return 'O wins'
            elif mat[0][2] == 'O' and mat[1][1] == 'O' and mat[2][0] == 'O':
                print('O wins')
                return 'O wins'
            elif mat[1][1] == 'X' and mat[2][2] == 'X' and mat[0][0] == 'X':
                print('X wins')
                return 'X wins'
            elif mat[0][2] == 'X' and mat[1][1] == 'X' and mat[2][0] == 'X':
                print('X wins')
                return 'X wins'

display()
while True:
    user_input()
    if check_box() == 'X wins' or check_box() == 'O wins' or user_input() == 'Draw':
        break
