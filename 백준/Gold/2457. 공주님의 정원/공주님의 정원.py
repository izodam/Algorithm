import sys
input = sys.stdin.readline

n = int(input())
flower = [list(map(int,input().split())) for _ in range(n)]
flower.sort()

i = 0
last_day = (3, 1)
cnt = 0
res = 0

while i < n:
    start_month, start_day, end_month, end_day = flower[i]
    if (start_month, start_day) <= last_day < (end_month, end_day):
        end = (end_month, end_day)
        while i < n - 1:
            next_start_m, next_start_d, next_end_m, next_end_d = flower[i+1]
            if last_day < (next_start_m, next_start_d):
                break
            if end < (next_end_m, next_end_d):
                end = (next_end_m, next_end_d)
            i += 1
        cnt += 1
        last_day = end

        if (11, 30) < last_day:
            res = cnt
            break
    i += 1

print(res)