def solution(n, lost, reserve):
    re = [i for i in reserve if i not in lost]
    lo = set([i for i in lost if i not in reserve])
    for r in re:
        left = r - 1
        right = r + 1
        if left in lo:
            lo.remove(left)
        elif right in lo:
            lo.remove(right)
    return n - len(lo)
