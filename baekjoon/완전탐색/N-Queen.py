# pypy
def dfs(n, y, col, upper_diag, low_diag):
    global answer
    if y == n:
        answer += 1
        return

    for x in range(n):
        if x in col or (x + y) in upper_diag or (y - x) in low_diag:
            continue
        col.add(x)
        upper_diag.add(x + y)
        low_diag.add(y - x)
        dfs(n, y+1, col, upper_diag, low_diag)
        col.remove(x)
        upper_diag.remove(x + y)
        low_diag.remove(y - x)


def solution(n):
    global answer
    col, upper_diag, low_diag = set(), set(), set()
    answer = 0
    dfs(n, 0, col, upper_diag, low_diag)
    return answer


N = int(input())
print(solution(N))
