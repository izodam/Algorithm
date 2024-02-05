# 2346번
from collections import deque
n = int(input())
# 풍선 번호를 얻어내기 위해 enumerate로 생성
ball = deque(enumerate(map(int,input().split())))

while ball:
    idx, paper = ball.popleft()
    print(idx+1, end=' ')

    if paper > 0:
        ball.rotate(-paper + 1)
    elif paper < 0:
        ball.rotate(-paper)