import sys
input = sys.stdin.readline

n = int(input())

visited = [0] * (n+1)
visited[0], visited[1] = 1, 1

# 소수 찾기
prims = []
for i in range(2, n + 1):
    if not visited[i]:
        prims.append(i)
        for j in range(2 * i, n + 1, i):
            visited[j] = 1
end = len(prims)

res = 0
left, right = 0, 0

while right <= end:
    now = sum(prims[left:right])
    if now == n:
        res += 1
        left += 1
    elif now < n:
        right += 1
    else:
        left += 1
print(res)