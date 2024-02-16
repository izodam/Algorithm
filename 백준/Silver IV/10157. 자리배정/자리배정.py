import sys
input = sys.stdin.readline
c,r=map(int,input().split())
k=int(input())

dx=[1,0,-1,0]
dy=[0,1,0,-1]

grid=[[0]*c for _ in range(r)]
direction,x,y=0,0,0

if k>c*r:
    print(0)
    exit()

for i in range(1,c*r+1):
    if i==k:
        print(y+1,x+1)
        break
    grid[x][y]=i
    x+=dx[direction]
    y+=dy[direction]
    if x<0 or y<0 or x>=r or y>=c or grid[x][y]!=0:
        x -= dx[direction]
        y -= dy[direction]
        direction = (direction + 1) % 4
        x += dx[direction]
        y += dy[direction]

