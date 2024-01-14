# 12865번
n, k = map(int,input().split())
item = [[0,0]]
for _ in range(n):
    item.append(list(map(int,input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]     # dp의 0 인덱스는 최대 가치, 1 인덱스는 남은 무게

for i in range(1,n+1):
    for j in range(1,k+1):
        w = item[i][0]
        v = item[i][1]

        if j < w:       # 가방에 넣을 수 없으면
            dp[i][j] = dp[i-1][j]       # 이전 값 그대로 사용
        else:           # 가방에 넣을 수 있다면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])
