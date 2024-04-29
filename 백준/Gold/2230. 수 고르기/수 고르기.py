import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nums = sorted([int(input()) for _ in range(n)])

res = float('inf')
st, en = 0, 0

while en < n and st < n:
    if nums[en] - nums[st] >= m:
        res = min(res, nums[en]-nums[st])
        st += 1
    else:
        en += 1


print(res)