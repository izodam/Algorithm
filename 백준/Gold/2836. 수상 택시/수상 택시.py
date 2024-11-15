import sys
input = sys.stdin.readline

n, m = map(int,input().split())

people = []
for _ in range(n):
    start, end = map(int,input().split())
    if start > end:
        people.append((end, start))
if len(people) == 0:
    print(m)
    exit()
people.sort(key=lambda x: -x[1])
tmp = []
ts, te = people[0]

for i in range(1, len(people)):
    s, e = people[i]

    if ts <= e:
        ts = min(ts, s)
    else:
        tmp.append((ts, te))
        ts, te = s, e
tmp.append((ts, te))

res = m
for i in range(len(tmp)):
    res += 2 * (tmp[i][1] - tmp[i][0])
print(res)