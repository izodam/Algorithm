# 17103번
import sys
input = sys.stdin.readline

f = int(1000000**0.5)
prime = [1] * (1000000 + 1)
prime[0], prime[1] = 0, 0
for i in range(2, f+1):
    if prime[i]:
        for j in range(i+i, 1000000+1, i):
            prime[j] = 0

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, n//2+1):
        if prime[i] and prime[n-i]:
            cnt += 1
    print(cnt)


