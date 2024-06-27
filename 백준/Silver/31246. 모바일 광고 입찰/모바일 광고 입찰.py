import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst = []
for _ in range(n):
    a, b = map(int,input().split())
    lst.append(b-a)

lst.sort()
if lst[k-1] < 0:
    print(0)
else:
    print(lst[k-1])