n = int(input())
chang = 100
sang = 100

for _ in range(n):
    c, s = map(int,input().split())
    if c > s:
        sang -= c
    elif s > c:
        chang -= s

print(chang)
print(sang)