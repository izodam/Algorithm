from collections import deque
import sys
input = sys.stdin.readline

r,c = map(int,input().split())
maze = [list(input()) for _ in range(r)]

#지환이와 불난 곳 저장
j = deque()
f = deque()

#이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visit_j = [[0]*c for _ in range(r)]
visit_f = [[0]*c for _ in range(r)]

def fbfs():
    while f:
        x,y = f.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not (0<=nx<r and 0<=ny<c):
                continue
            if maze[nx][ny]=='#' or visit_f[nx][ny]:
                continue
            visit_f[nx][ny] = visit_f[x][y]+1
            f.append((nx,ny))


def jbfs():
    while j:
        x,y = j.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #탈출 성공
            if not (0<=nx<r and 0<=ny<c):
                print(visit_j[x][y])
                return
            if maze[nx][ny]=='#' or visit_j[nx][ny]:
                continue
            if visit_f[nx][ny] and visit_j[x][y]+1>=visit_f[nx][ny]:
                continue
            visit_j[nx][ny]=visit_j[x][y]+1
            j.append((nx,ny))
    print('IMPOSSIBLE')
    return

for i in range(r):
    for k in range(c):
        if maze[i][k]=='J':
            j.append((i,k))
            visit_j[i][k] = 1
        elif maze[i][k]=='F':
            f.append((i,k))
            visit_f[i][k]=1

fbfs()
jbfs()
