from collections import deque
import sys
input = sys.stdin.readline

r,c = map(int,input().split())
maze = [list(input()) for _ in range(r)]
res = 0

#지환이와 불난 곳 저장
j = deque()
f = deque()

#이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(r):
    for k in range(c):
        if maze[i][k]=='J':
            j.append((i,k))
        if maze[i][k]=='F':
            f.append((i,k))

def bfs():
    global f,j,res
    while True:
        res += 1
        temp = []
        while f:
            x,y = f.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or ny<0 or nx>=r or ny>=c:
                    continue
                if maze[nx][ny]=='.' or maze[nx][ny]=='$':
                    temp.append((nx,ny))
                    maze[nx][ny] = 'F'
        f = deque(temp)

        temp=[]
        while j:
            x,y = j.popleft()
            #미로 탈출
            if x==0 or y==0 or x==r-1 or y==c-1:
                return res
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue
                if maze[nx][ny] == '.':
                    temp.append((nx,ny))
                    #갔던 곳은 $로 표시
                    maze[x][y] = '$'
                    maze[nx][ny] = 'J'
        j = deque(temp)
        if not j:
            return False

if bfs():
    print(res)
else:
    print('IMPOSSIBLE')
