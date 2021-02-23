import sys

Y, X = map(int, sys.stdin.readline().split())
board = [[] * Y for _ in range(Y)]
case1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
         'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
case2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
         'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']


def find_diff(board):
    count1 = 0
    count2 = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != case1[i][j]:
                count1 += 1
            if board[i][j] != case2[i][j]:
                count2 += 1
    return min(count1, count2)


for i in range(Y):
    board[i] += list(sys.stdin.readline().rstrip())
count = float('inf')
for i in range(Y-7):
    for j in range(X-7):
        test_board = [row[j:j+8] for row in board[i:i+8]]
        c = find_diff(test_board)
        if count > c:
            count = c
print(count)
