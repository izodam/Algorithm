import itertools
n, m =map(int,input().split())

l = [str(i) for i in range(1,n+1)]
print('\n'.join(list(map(' '.join, itertools.permutations(l,m)))))