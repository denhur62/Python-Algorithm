N, r, c = map(int, input().split())

start = 0
while N != 0:
    if 0 <= r < 2**(N-1) and 0 <= c < 2**(N-1):
        pass
    elif 0 <= r < 2**(N-1) and 2**(N-1) <= c < 2**N:
        c -= 2**(N-1)
        start += 2**(2*N-2)
    elif 2**(N-1) <= r < 2**N and 0 <= c < 2**(N-1):
        r -= 2**(N-1)
        start += 2**(2*N-1)
    else:
        r -= 2**(N-1)
        c -= 2**(N-1)
        start += 2**(2*N-2)*3
    N -= 1
print(start)
