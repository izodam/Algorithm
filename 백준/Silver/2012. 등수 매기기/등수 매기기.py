import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)])

res = 0
for i in range(1, n+1):
  if arr[i-1] != i:
    res += abs(arr[i-1] - i)
print(res)