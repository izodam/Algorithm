# 마름모 찾기
def area(k):
    idx_list = []
    for i in range(k):
        for j in range(-k + 1 + i, k - i):
            if i == 0:
                idx_list.append((i, j))
            else:
                idx_list.append((i, j))
                idx_list.append((-i, j))
    return idx_list

# 집이 가장 많이 들어가는 위치 찾기
def findhouse(area):
    house = 0
    for r in range(n):
        for c in range(n):
            now = 0
            for i in area:
                nx = r + i[0]
                ny = c + i[1]
                if 0<=nx<n and 0<=ny<n and board[nx][ny] == 1:
                    now += 1
            if now > house:
                house = now
    return house


T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    # 운영 비용 = k^2 + (k-1)^2
    board = [list(map(int,input().split())) for _ in range(n)]

    res = 0


    for k in range(n+2):
        cost = (k**2) + ((k-1)**2)
        house = findhouse(area(k))
        if house * m - cost >= 0:
            res = max(res, house)
    print(f'#{tc}',res)