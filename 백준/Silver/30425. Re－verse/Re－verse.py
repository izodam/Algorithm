import sys

N = int(input())
Alpha = input().strip()
routine = N

for i in range(1, N):
    check = False
    for j in range(i, N):
        if Alpha[j - i] != Alpha[j]:
            check = True
            break
    if not check:
        routine = i
        break

print((N - 1) // routine + 1)
