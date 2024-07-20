n = int(input())
u = set()
for _ in range(n):
    u.add(int(input()))
sums = set()

ans = []
for i in u:
    for j in u:
        sums.add(i+j)


for i in u:
    for j in u:
        if (i-j) in sums:
            ans.append(i)
print(max(ans))