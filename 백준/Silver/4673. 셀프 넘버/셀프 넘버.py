# 4673번
def d(n):
    n += sum(map(int,str(n)))
    return n

nself = set()

for i in range(1,10001):
    nself.add(d(i))

for i in range(1,10001):
    if i not in nself:
        print(i)