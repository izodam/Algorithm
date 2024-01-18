# 10993번
n = int(input())

def drawstar(n):
    if n == 1:
        return ['*'], 1

    stars, first = drawstar(n-1)
    res = []

    len_stars = len(stars)

    if n == 2:
        first_star = 5
    else:
        first_star = first * 2 + 3

    if n%2 == 0:        # 짝수일 때
        res.append('*' * first_star)      # 띄어쓰기 없이 별만 있는 줄
        for i in range(len_stars):
            res.append(' ' * (i + 1) + '*' + ' ' * (first // 2 - i) + stars[i] +  ' ' * (first_star//2 - 2 - (2 * i)) + '*')

        for i in range(len_stars - 1):
            res.append(' ' * (len_stars + i + 1) + '*' + ' ' * (first - 2 - (2 * i)) + '*')

        res.append(' '*(first_star//2) + '*')
        
    else:
        res.append(' ' * (first_star // 2) + '*')
        for i in range(1, len_stars):
            res.append(' ' * (first_star // 2 - i) + '*' + ' ' * (1 + (i-1) * 2) + '*')
        for i in range(len_stars):
            res.append(' ' * (len_stars - i) + '*' + ' ' * i + stars[i] + ' ' * (2 * i) + '*')
        res.append('*' * first_star)



    return res, first_star

res,first = drawstar(n)
print('\n'.join(res))