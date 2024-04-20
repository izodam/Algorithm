# 12908
def cal_time(dot1, dot2):
    return abs(dot1[0] - dot2[0]) + abs(dot1[1] - dot2[1])

xs, ys = map(int,input().split())
xe, ye = map(int,input().split())

# 시작점, 텔레포트 위치, 끝점 순으로 점 8개가 들어감
dot = [0] * 8
dot[0] = (xs, ys)
dot[7] = (xe, ye)
#
# distance[0][1] = 0번 점 ~ 1번 점 사이의 거리
distance = [[float('inf')] * 8 for _ in range(8)]
distance[0][7] = distance[7][0] = cal_time(dot[0], dot[7])

for i in range(1,4):
    x1, y1, x2, y2 = map(int,input().split())
    dot[i*2-1] = (x1, y1)
    dot[i*2] = (x2, y2)
    # 순간이동과 점프 중 더 빠른 것 선택
    distance[i*2-1][i*2] = distance[i*2][i*2-1] = min(cal_time(dot[i*2-1], dot[i*2]), 10)

for i in range(8):
    for j in range(8):
        distance[i][j] = min(distance[i][j], cal_time(dot[i], dot[j]))

for k in range(8):
    for i in range(8):
        for j in range(8):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])


print(distance[0][7])
# print('\n'.join(map(str, distance)))