import sys
input = sys.stdin.readline


N = int(input())
stack = []

for _ in range(N):
    action, value = map(int,input().split())

    if action == 1:
        stack.append(value)
    else:
        if stack:
            k = stack.pop()
            stack.append(max(k-value, 0))

top = stack[-1] if stack else 0
res = 0
while stack:
    now = stack.pop()
    if now > top:
        res += top
    else:
        top = now
        res += now
print(res)