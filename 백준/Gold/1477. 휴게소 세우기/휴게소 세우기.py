import sys
input = sys.stdin.readline
# 휴게소를 m개 지어서 휴게서 없는 구간의 길이의 최대값을 최소로 만들기
# -> 이분탐색 이용해서 구간의 길이를 찾음
n, m, l = map(int,input().split())
location = [0] + sorted(list(map(int,input().split()))) + [l]

start = 1
end = l-1
res = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, len(location)):
        if location[i] - location[i-1] > mid:
            cnt += (location[i] - location[i-1] - 1) // mid

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        res = mid
print(res)