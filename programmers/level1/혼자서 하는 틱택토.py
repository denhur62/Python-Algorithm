def solution(board):
    flat_board = "".join(board)
    o_cnt = flat_board.count('O')
    x_cnt = flat_board.count('X')
    if (o_cnt == x_cnt and find_win(flat_board)== 'x_win') \
        or (o_cnt -1 == x_cnt and find_win(flat_board) == 'o_win'):
        return 1
    else:
        if x_cnt > o_cnt:
            return 0
        else:
            return 1

    
def find_win(fb):
    if (fb[0]=='O' and fb[3]=='O' and fb[6]=='O') \
        or (fb[1]=='O' and fb[4]=='O' and fb[7]=='O') \
        or (fb[2]=='O' and fb[5]=='O' and fb[8]=='O') \
        or (fb[0]=='O' and fb[4]=='O' and fb[8]=='O') \
        or (fb[2]=='O' and fb[4]=='O' and fb[6]=='O') :
        return 'o_win'
    elif (fb[0]=='X' and fb[3]=='X' and fb[6]=='X') \
        or (fb[1]=='X' and fb[4]=='X' and fb[7]=='X') \
        or (fb[2]=='X' and fb[5]=='X' and fb[8]=='X') \
        or (fb[0]=='X' and fb[4]=='X' and fb[8]=='X') \
        or (fb[2]=='X' and fb[4]=='X' and fb[6]=='X') :
        return 'x_win'

print(solution(["OOO", "...", "XXX"]))