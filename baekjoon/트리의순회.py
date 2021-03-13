import sys

sys.setrecursionlimit(10**6)
N = int(input())

in_arr = list(map(int, sys.stdin.readline().split()))
post_arr = list(map(int, sys.stdin.readline().split()))

index_arr = [0]*(N+1)
for i in range(N):
    index_arr[in_arr[i]] = i


def free_order(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return

    root = post_arr[post_right]
    print(root, end=' ')
    index_root = index_arr[root]
    slice_size = index_root-in_left
    free_order(in_left, index_root-1, post_left, post_left+slice_size-1)
    free_order(index_root+1, in_right, post_left+slice_size, post_right-1)


free_order(0, N-1, 0, N-1)
