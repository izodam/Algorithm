from collections import deque
n, m = map(int,input().split())
jimin = list(map(int,input().split()))
q = deque([i for i in range(1,n+1)])
cnt = 0

for i in jimin:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i)<len(q)/2:  # i의 위치가 절반보다 작으면 3번 수행
                while q[0] != i:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != i:
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)