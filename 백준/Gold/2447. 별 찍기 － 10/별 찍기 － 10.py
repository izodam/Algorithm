# 2447번
n = int(input())
def drawstar(n):
    if n == 1:
        return ['*']
    
    star = drawstar(n//3)
    line = []
    
    for i in star:
        line.append(i*3)
    for i in star:
        line.append(i+' '*(n//3)+i)
    for i in star:
        line.append(i*3)
    return line

print('\n'.join(drawstar(n)))
