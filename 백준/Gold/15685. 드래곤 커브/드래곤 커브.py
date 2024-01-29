# 15685번
N = int(input())
graph = [[0] * 101 for _ in range(101)]

# 방향 지정
# 만약 방향이 0이면 90도 회전하면 다음 방향은 1
# 만약 방향이 1이면 90도 회전하면 다음 방향은 2
# 만약 방향이 2이면 90도 회전하면 다음 방향은 3
# 만약 방향이 3이면 90도 회전하면 다음 방향은 0
# 즉 (방향 + 1)을 4로 나눈 나머지!

# 방향대로 움직이는 리스트 선언
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


for _ in range(N):
    y, x, d, g = map(int,input().split())
    # 방문한 곳 1로 처리
    graph[x][y] = 1

    # 커브 방향을 저장하는 리스트
    curve = [d]

    # 세대만큼 반복
    for i in range(g):
        for j in range(len(curve)-1, -1, -1):
            curve.append((curve[j] + 1) % 4)        # 다음 방향 지정

    # 드래곤 커브
    for i in curve:
        x += dx[i]
        y += dy[i]

        # 격자 밖으로 넘어가면 무시
        if x<0 or x>=101 or y<0 or y>=101:
            continue

        # 넘어가지 않았다면 방문처리
        graph[x][y] = 1

res = 0
for i in range(100):
    for j in range(100):
        # 1*1 모서리 확인
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            res += 1
print(res)