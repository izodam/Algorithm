t = int(input())
for _ in range(t):
    a,b = input().split()

    x = sorted(list(a))
    y = sorted(list(b))

    if x == y:
        print(a,"&",b,"are anagrams.")
    else:
        print(a,"&",b,"are NOT anagrams.")
