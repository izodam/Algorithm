n, l = map(int, input().split())
location = list(map(int, input().split()))
location.sort()

start = location[0]
cnt = 1

for i in location[1:]:
    if i in range(start, start+l):
        continue
    else:
        start = i
        cnt += 1

print(cnt)
