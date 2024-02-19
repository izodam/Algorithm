# 28278번
import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    a = list(map(int,input().split()))

    if a[0] == 1:
        stack.append(a[1])
    elif a[0] == 2:
        print(stack.pop()) if stack else print(-1)
    elif a[0] == 3:
        print(len(stack))
    elif a[0] == 4:
        print(0) if stack else print(1)
    else:
        print(stack[-1]) if stack else print(-1)
