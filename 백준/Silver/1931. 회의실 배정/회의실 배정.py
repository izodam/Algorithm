n = int(input())
meeting = []
for i in range(n):
    s,e = map(int,input().split())
    meeting.append((s,e))

meeting.sort(key=lambda x:(x[1],x[0]))

cnt = 1
e = meeting[0][1]

for i in meeting[1::]:
    if i[0] >= e:
        cnt += 1
        e = i[1]
print(cnt)