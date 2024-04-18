import math

def get_primes(s, n):
    prime = [1] * n
    for i in range(2, math.ceil(math.sqrt(n))):
        if prime[i]:
            for j in range(i+i, n, i):
                prime[j] = 0

    cnt = 0
    for i in range(s, n):
        if prime[i]:
            cnt += 1
    return [i for i in range(s, n) if prime[i]]



a, b = map(int,input().split())
c, d = map(int,input().split())

young = set(get_primes(a, b+1))
yu = set(get_primes(c, d+1))

ans = set()

tea = len(young)
zin = len(yu)

turn = 1
while True:
    # print(ans)
    flag = 0
    if turn == 1:
        turn = 0
        if tea <= 0:
            print('yj')
            break
        tea -= 1
        for num in young:
            if num in yu and num not in ans:
                ans.add(num)
                flag = 1
                break
        if flag == 0:
            for num in young:
                if num not in ans:
                    ans.add(num)
                    flag = 1
                    break
        if flag == 0:
            print('yj')
            break

    else:
        turn = 1
        if zin <= 0:
            print('yt')
            break
        zin -= 1
        for num in yu:
            if num in young and num not in ans:
                flag = 1
                ans.add(num)
                break
        if flag == 0:
            for num in yu:
                if num not in ans:
                    ans.add(num)
                    flag = 1
                    break

        if flag == 0:
            print('yt')
            break