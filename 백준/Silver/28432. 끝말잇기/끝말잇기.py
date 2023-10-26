n = int(input())
s = [input() for _ in range(n)]
m = int(input())
a = [input() for _ in range(m)]
res = ''
if n == 1:
    res = a[0]
else:
    for i in range(n):
        if s[i] == '?':
            if i == 0:
                for j in a:
                    if j[-1] == s[i+1][0]:
                        if not j in s:
                            res = j
                            break
                break
            if i == n-1:
                for j in a:
                    if j[0] == s[i-1][-1]:
                        if not j in s:
                            res = j
                            break
                break
            first = s[i - 1][-1]
            last = s[i + 1][0]
            break
    
    if res == '':
        for i in a:
            if i[0] == first and i[-1] == last:
                if not i in s:
                    res = i
                    break
print(res)