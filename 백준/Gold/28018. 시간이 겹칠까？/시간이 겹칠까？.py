import sys
input = sys.stdin.readline

n = int(input())
in_time = [0] * 1000001
out_time = [0] * 1000001
primary_sum = [0] * 1000001

for _ in range(n):
    s, e = map(int, input().split())
    in_time[s] += 1
    out_time[e] += 1

for i in range(1, 1000001):
    primary_sum[i] = primary_sum[i - 1] + in_time[i] - out_time[i - 1]

q = int(input())
lst = list(map(int,input().split()))

for i in lst:
    print(primary_sum[i])