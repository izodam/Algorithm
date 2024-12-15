import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort()

max_diff = 0
res = -1

for i in range(1, n):
    diff = (arr[i] - arr[i - 1]) // 2
    if max_diff < diff:
        max_diff = diff
        res = (arr[i] + arr[i - 1]) // 2

print(res)