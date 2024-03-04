#1.
def chk(line):
    res = 1
    for i in range(1, N):
        # 같은 층이면 1 추가
        if line[i] == line[i-1]:
            res += 1
        # 1 올라감, 기존에 X 만큼 채웠어야함
        elif line[i] - line[i-1] ==1 and res >= X:
            res = 1 # 다시 1부터
        # 1 낮아질때, 0보다 커야지 X 채우고 안 낮아진거임
        elif line[i-1] - line[i] ==1 and res >= 0:
            res = 1 - X # 현재 포함해야 되어서 1 하고 X 뺌
        else:
            return 0
    if res >= 0:
        return 1
    return 0
T = 1
for tc in range(1,T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += chk(arr[i])
        temp = []
        for j in range(N):
            temp.append(arr[j][i])
        ans += chk(temp)
    print(ans)
