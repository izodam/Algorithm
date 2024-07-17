import sys
input = sys.stdin.readline

n, m = map(int,input().split())
machine = list(map(int,input().split()))

start = 0
end = n * 30
ride_people = float('inf')

while start < end:
    mid = (start + end) // 2
    # mid분에 처리한 인원 수
    now = 0
    for i in machine:
        now += mid // i + 1
    if now < n:
        start = mid + 1
    else:
        end = mid
        ride_people = min(now, ride_people)
# print(ride_people, end)
for i in range(m-1, -1, -1):
    if end % machine[i] == 0:
        if ride_people == n:
            print(i + 1)
            break
        ride_people -= 1