import math
import sys
input = sys.stdin.readline

w,h,x,y,p = map(int,input().split())
r = h//2
c1x,c1y = x,y+r
c2x,c2y = x+w,y+r

cnt = 0
for i in range(p):
    player_x,player_y = map(int,input().split())

    #각 원의 중심에서의 거리
    d1 = math.sqrt((c1x-player_x)**2 + (c1y-player_y)**2)
    d2 = math.sqrt((c2x-player_x)**2 + (c2y-player_y)**2)

    if d1<=r or d2<=r:
        cnt+=1
    elif x<=player_x<=x+w and y<=player_y<=y+h:
        cnt+=1


print(cnt)