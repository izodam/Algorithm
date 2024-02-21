n=int(input())
card=list(map(int,input().split()))
m=int(input())
cheak=list(map(int,input().split()))

cnt={}
for i in card:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1

for i in cheak:
    if i in cnt:
        print(cnt[i],end=' ')
    else:
        print(0,end=' ')