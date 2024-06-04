r, c = map(int,input().split())
board = [input().strip() for _ in range(r)]
turn_board = list(map(list, zip(*board)))

res = []
for i in range(r):
    now = board[i].split('#')
    for j in now:
        if len(j) > 1:
            res.append(j)

for i in range(c):
    now = ''.join(turn_board[i]).split('#')
    for j in now:
        if len(j) > 1:
            res.append(j)

res.sort()
print(res[0])