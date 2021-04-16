n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
solve = []


def dfs(depth):
    if depth == m:
        print(' '.join(map(str, solve)))
        return
    for i in arr:
        if depth == 0 or solve[depth-1] <= i:
            solve.append(i)
            dfs(depth+1)
            solve.pop()


dfs(0)
