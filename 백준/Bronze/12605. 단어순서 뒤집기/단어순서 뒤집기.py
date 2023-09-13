n = int(input())
for i in range(1, n+1):
    word = list(input().split())
    print('Case #'+str(i),end=': ')
    print(' '.join(word[::-1]))
