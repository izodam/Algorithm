from collections import deque


n = int(input())
#  큐라면 0
# 스택이라면 1
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))

q = deque()
for i in range(n):
    if a[i] == 0:
        q.append(b[i])

for number in c:
    q.appendleft(number)
    print(q.pop(),end=' ')
