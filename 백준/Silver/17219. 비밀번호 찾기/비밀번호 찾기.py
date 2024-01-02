# 17219번
N, M = map(int,input().split())
save = {}
for _ in range(N):
    site, password = input().split()
    save[site] = password
for _ in range(M):
    site = input()
    print(save.get(site))