n = int(input())
word = input()

res = 0
now = ''

for i in word:
    if i.isdigit():
        now += i
        if len(now) > 6:
            now = ''
    else:
        if now:
            res += int(now)
            now = ''
if now:
    res += int(now)
print(res)