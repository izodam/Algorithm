import sys
input = sys.stdin.readline

n, m = map(int,input().split())
board = dict()
for _ in range(n):
    board[input().strip()] = 1

res = n
for _ in range(m):
    words = sorted(input().strip().split(','))

    for word in words:
        if word in board.keys():
            if board[word] == 1:
                board[word] -= 1
                res -= 1
    print(res)