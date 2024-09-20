import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

if (n < k):
    print(0)
    exit()

distance = []

for i in range(1, n):
    distance.append(sensor[i] - sensor[i-1])

distance.sort()

for i in range(k-1):
    distance.pop()
print(sum(distance))