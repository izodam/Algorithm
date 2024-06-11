import sys
input = sys.stdin.readline

k, l = map(int,input().split())
wait = {}
for i in range(l):
    wait[input().strip()] = i

sort_wait = sorted(wait.items(), key=lambda x:x[1])

for i in range(k):
    if i < len(sort_wait):
        print(sort_wait[i][0])
    else:
        break