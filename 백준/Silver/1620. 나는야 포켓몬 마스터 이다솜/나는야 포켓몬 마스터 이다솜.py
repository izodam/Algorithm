# 1620번
from sys import stdin
def input():
    return stdin.readline().rstrip()

n,m = map(int,input().split())
id = {}
name = {}
for i in range(1,n+1):
    pokemon = input()
    id[i] = pokemon
    name[pokemon] = i

for _ in range(m):
    i = input()
    if i.isdigit() == True:
        print(id[int(i)])
    else:
        print(name[i])