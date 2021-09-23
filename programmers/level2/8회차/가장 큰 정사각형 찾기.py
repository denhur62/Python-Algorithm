
def solution(board):
    answer = []
    column=len(board[0])
    row=len(board)
    for i in range(1,row):
        for j in range(1,column):
            if board[i][j]!=0:
                board[i][j]=min(board[i][j-1],board[i-1][j],board[i-1][j-1])+1
    for i in range(row):
        answer.append(max(board[i]))
    
    answer=max(answer)

    return answer*answer



# def solution(board):
#     answer = 0
#     column=len(board[0])
#     row=len(board)
#     for i in range(row):
#         for j in range(column):
#             cnt=0
#             flag=True
#             if board[i][j]==1:
#                 ci, cj = i , j
#                 while ci<row and cj<column and board[ci][j]==1 and board[i][cj]==1:
#                     ci+=1
#                     cj+=1
#                     cnt+=1
                
#                 for k in range(i,ci):
#                     for w in range(j,cj):
#                         if board[k][w]!=1:
#                             flag=False
#                             break
#                     if not flag:
#                         break
#             if flag and answer < cnt:
#                 answer = cnt

#     return answer*answer