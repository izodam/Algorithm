import sys
input = sys.stdin.readline
from collections import deque
a, b, c = map(int,input().split())

# 돌 개수의 총 합이 3의 배수가 아니면 불가능
total = a + b + c
if total % 3:
    print(0)
    exit()

visited = [[False] * total for _ in range(total)]
q = deque()
q.append((a, b))
visited[a][b] = True

while q:
    na, nb = q.popleft()
    nc = total - na - nb
    if na == nb == nc:
        print(1)
        exit()
    for x, y in [(na, nb), (na, nc), (nb, nc)]:
        if x == y:
            continue
        if x > y:
            x, y = y, x

        y = y - x
        x = x + x
        z = total - x - y

        new_a = min(x, y, z)
        new_b = max(x, y, z)
        if not visited[new_a][new_b]:
            q.append((new_a, new_b))
            visited[new_a][new_b] = True
print(0)