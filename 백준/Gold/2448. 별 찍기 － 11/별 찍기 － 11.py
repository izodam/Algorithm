n = int(input())


def drawstar(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    star = drawstar(n // 2)
    res = []

    for i in range(len(star)):
        res.append(' ' * (n // 2) + star[i] + ' ' * (n // 2))
    for i in range(len(star)):
        res.append(star[i] + ' ' * (n % 6 + 1) + star[i])

    return res


print('\n'.join(drawstar(n)))