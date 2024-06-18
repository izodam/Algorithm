from collections import Counter
import sys
input = sys.stdin.readline

n=int(input())
num=[int(input()) for i in range(n)]
num.sort()
print(round(sum(num)/n))
print(num[(n//2)])

count=Counter(num)
order=count.most_common()
freq=order[0][1]

fq=[]
for i in order:
    if i[1]==freq:
        fq.append(i[0])
if len(fq)==1:
    print(fq[0])
else:
    print(sorted(fq)[1])

print(num[-1]-num[0])