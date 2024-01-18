# 13015번
n = int(input())
space = 2 * n - 3
print('*' * n + ' ' * space + '*' * n)
if n == 2:
    print(' ***')
else:
    for i in range(1,n-1):
        print(' '* (i) + '*' + ' '* (n - 2) + '*' + ' ' * (space - 2 * i) + '*' + ' ' * (n-2) + '*')

    print(' ' * (n-1) + '*' + ' '* (n-2) + '*' + ' '*(n-2) + '*')

    for i in range(n-2, 0, -1):
        print(' ' * (i) + '*' + ' ' * (n - 2) + '*' + ' ' * (space - 2 * i) + '*' + ' ' * (n - 2) + '*')

print('*' * n + ' ' * (2 * n - 3) + '*' * n)