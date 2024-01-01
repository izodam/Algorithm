T = int(input())
for i in range(T):
    n = list(map(int,input().split()))

    print(f'#{i+1} {max(n)}')