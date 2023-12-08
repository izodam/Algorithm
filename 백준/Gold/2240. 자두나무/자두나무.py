t,w = map(int,input().split())
tree = [0] + [int(input()) for _ in range(t)]
# dp[시간][이동횟수] = (시간)까지 (이동횟수)만큼 이동했을때 얻을 수 있는 최대 자두 개수
dp = [[0]*(w+1) for _ in range(t+1)]

# 1초일때
# 0번 이동했으면 1번 나무아래
# 1번 이동했으면 2번 나무아래
dp[1][0] = tree[1] % 2
dp[1][1] = tree[1] // 2

for i in range(2,t+1):
    for j in range(w+1):
        if j % 2 == 0:
            x = tree[i] % 2
        else:
            x = tree[i] // 2
        dp[i][j] = max(dp[i-1][0:j+1])+x
print(max(dp[-1]))