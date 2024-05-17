import bisect

t = int(input())
n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

# 누적 합 담을 list
a_sum = []
b_sum = []

for i in range(n):
    for j in range(i+1, n+1):
        a_sum.append(sum(a[i:j]))

for i in range(m):
    for j in range(i + 1, m + 1):
        b_sum.append(sum(b[i:j]))

a_sum.sort()
b_sum.sort()

res = 0
for num in a_sum:
    tmp = t - num
    left = bisect.bisect_left(b_sum, tmp)
    right = bisect.bisect_right(b_sum, tmp)
    res += (right - left)
print(res)