n = int(input())

def drawstar(n):
    if n == 1:
        return ['*']
    last_star = drawstar(n-1)
    nstar = 4 * n - 3
    res = []

    res.append('*'*nstar)
    res.append('*'+ ' '*(nstar-2) + '*')

    for i in range(len(last_star)):
        res.append('* ' + last_star[i] + ' *')

    res.append('*' + ' ' * (nstar - 2) + '*')
    res.append('*' * nstar)
    return res

res = drawstar(n)
print('\n'.join(res))