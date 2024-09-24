import sys
input = sys.stdin.readline

n = int(input())

res = 1
for i in range(1, n):
    if i % 2 != 0:
        res *= i
print(res)