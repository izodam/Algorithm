na,nb = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

res=[]
for i in a:
       if i not in b:
              res.append(i)
res.sort()
if len(res)==0:
       print(0)
else:
       print(len(res))
       print(' '.join(map(str,res)))