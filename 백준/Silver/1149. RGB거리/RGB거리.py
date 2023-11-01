n = int(input())
cost = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    # 빨 -> 전 집의 초,파를 선택했을 때의 최소값과 합한 것으로 결정
    cost[i][0] = min(cost[i-1][1],cost[i-1][2]) + cost[i][0]

    # 초
    cost[i][1] = min(cost[i-1][0],cost[i-1][2]) + cost[i][1]

    # 파
    cost[i][2] = min(cost[i - 1][0], cost[i - 1][1]) + cost[i][2]

print(min(cost[n-1]))