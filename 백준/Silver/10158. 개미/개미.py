# 10158번
w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

wlist = list(range(p,w)) + list(range(w,-1,-1)) + list(range(1,p))
hlist = list(range(q,h)) + list(range(h,-1,-1)) + list(range(1,q))

print(wlist[t%(2*w)],hlist[t%(2*h)])