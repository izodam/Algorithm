import sys
input = sys.stdin.readline
def move():
    for i in range(n):
        now = i
        for j in range(h):
            # 가로선 존재
            if board[j][now]:
                now += 1
            elif now>0 and board[j][now-1]:
                now -= 1
        if now != i:
            return False
    return True



def dfs(cnt, x, y):
    global res
    if move():
        res = min(res, cnt)
        return

    elif cnt >= 3 or cnt >= res:
        return

    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0

        for j in range(now, n-1):
            if not board[i][j] and not board[i][j+1]:
                if j > 0 and board[i][j-1]:
                    continue
                board[i][j] = 1
                dfs(cnt+1, i, j+2)
                board[i][j] = 0



# n개의 세로선과 m개의 가로선
n, m, h = map(int,input().split())
board = [[0] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int,input().split())
    board[a-1][b-1] = 1

res = float('inf')
dfs(0,0,0)
if res > 4:
    print(-1)
else:
    print(res)
