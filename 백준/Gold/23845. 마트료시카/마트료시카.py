import heapq

N = int(input())
X = sorted(list(map(int, input().split())), reverse=True)

pq = [[] for _ in range(100002)]

for x in X:
    if len(pq[x + 1]) == 0:
        heapq.heappush(pq[x], -x)  # 음수로 저장하여 최대 힙처럼 사용
    else:
        num = -heapq.heappop(pq[x + 1])
        heapq.heappush(pq[x], -num)

ans = 0
for i in range(1, 100001):
    while len(pq[i]) > 0:
        node = -heapq.heappop(pq[i])
        ans += node * (node - i + 1)

print(ans)