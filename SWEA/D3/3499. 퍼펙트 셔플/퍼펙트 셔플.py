T = int(input())
for tc in range(1, T+1):
    n = int(input())
    card = list(input().split())
    a = 0
    b = (n-1)//2 + 1
    print(f'#{tc}',end=' ')
    while a < (n-1)//2 + 1:
        print(card[a], end=' ')
        if b < n:
            print(card[b], end=' ')
        a += 1
        b += 1
    print()
