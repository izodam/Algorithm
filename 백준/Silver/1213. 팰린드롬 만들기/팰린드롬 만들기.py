import collections

hansu = input()
# 각 문자의 개수 구해줌
cheak = collections.Counter(hansu)

cnt = 0
res = ''
mid = ''
for k,v in list(cheak.items()):
    if v % 2 == 1:  # 해당 문자가 홀수개
        cnt += 1
        mid = k     # 가운데로 들어가야 함.
        if cnt >= 2:    # 홀수가 2개 이상이라면 펠린드롬이 될 수 없음
            print("I'm Sorry Hansoo")
            exit()
for  k,v in sorted(cheak.items()):
    res += (k * (v // 2))

print(res + mid + res[::-1])
