import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

# r번 회전
for _ in range(r):
    for i in range(min(n,m)//2):
        x, y = i, i     # 맨 처음 좌표 지점
        temp = data[x][y]   # 맨 처음 좌표가 가진 값

        # 확인 방향 좌 -> 하 -> 우 -> 상
        for j in range(i+1, n-i):   # 좌
            x = j
            value = data[x][y]
            data[x][y] = temp
            temp = value

        for j in range(i+1, m-i):   # 하
            y = j
            value = data[x][y]
            data[x][y] = temp
            temp = value


        for j in range(i+1, n-i):   # 우
            x = n-j-1
            value = data[x][y]
            data[x][y] = temp
            temp = value
        for j in range(i+1, m-i):   # 상
            y = m-j-1
            value = data[x][y]
            data[x][y] = temp
            temp = value


for i in data:
    print(' '.join(map(str,i)))