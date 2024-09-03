import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know = set(map(int, input().split()[1:]))

party_people = [set(map(int, input().split()[1:])) for _ in range(m)]

for i in range(m):
    for party in party_people:
        if party.intersection(know):
            know = know.union(party)

res = 0

for party in party_people:
    if party & know:
        continue
    res += 1
print(res)