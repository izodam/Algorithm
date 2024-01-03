# 26069번
N = int(input())
meet = ['ChongChong']
for _ in range(N):
    x,y = input().split()
    if x in meet:
        meet.append(y)
    if y in meet:
        meet.append(x)
res = list(set(meet))
print(len(res))