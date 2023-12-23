# 11655번
s = input()
res = ''
for i in s:
    if 'a'<=i<='z':
        a = ord(i)+13
        if a>122:
            a-=26
        res+=chr(a)
    elif 'A'<=i<='Z':
        a = ord(i)+13
        if a>90:
            a-=26
        res+=chr(a)
    else:
        res+=i
print(res)