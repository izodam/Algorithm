from collections import deque
n = int(input())
ball = deque(enumerate(map(int,input().split())))
res = []

while ball:
    idx, paper = ball.popleft()
    res.append(idx + 1)
    if paper > 0:
        ball.rotate(-(paper-1))
    elif paper < 0:
        ball.rotate(-paper)
print(' '.join(map(str,res)))
