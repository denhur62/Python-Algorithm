import sys

N, M = map(int, sys.stdin.readline().split())
email_list = []
pwd_list = {}
for _ in range(N):
    email, pwd = sys.stdin.readline().split()
    pwd_list[email] = pwd
for _ in range(M):
    seek = sys.stdin.readline().rstrip()
    print(pwd_list[seek])
