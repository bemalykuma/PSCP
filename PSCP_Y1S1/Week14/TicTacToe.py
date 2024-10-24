'''TicTacToe'''
def game():
    '''TicTacToe'''
    temp = []
    result = []
    for _ in range(3):
        turn = input()
        temp += turn
        result.append(temp)
        temp = []
    x_win = ['X', 'X', 'X'] in result or (result[0][0] == 'X' and result[1][0] == 'X'\
        and result[2][0] == 'X') or (result[0][1] == 'X' and result[1][1] == 'X'\
        and result[2][1] == 'X') or (result[0][2] == 'X' and result[1][2] == 'X'\
        and result[2][2] == 'X') or (result[0][0] == 'X' and result[1][1] == 'X'\
        and result[2][2] == 'X') or (result[0][2] == 'X' and result[1][1] == 'X'\
        and result[2][0] == 'X')
    o_win = ['O', 'O', 'O'] in result or (result[0][0] == 'O' and result[1][0] == 'O'\
        and result[2][0] == 'O') or (result[0][1] == 'O' and result[1][1] == 'O'\
        and result[2][1] == 'O') or (result[0][2] == 'O' and result[1][2] == 'O'\
        and result[2][2] == 'O') or (result[0][0] == 'O' and result[1][1] == 'O'\
        and result[2][2] == 'O') or (result[0][2] == 'O' and result[1][1] == 'O'\
        and result[2][0] == 'O')
    if x_win:
        print("X WIN")
    elif o_win:
        print("O WIN")
    else:
        print("DRAW")
game()
