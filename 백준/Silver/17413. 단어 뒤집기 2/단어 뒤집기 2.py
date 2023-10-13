word = list(input())

i = 0
start = 0

while i < len(word):
    # 열린 괄호를 만나면 닫힌 괄호 만날 때 까지 인덱스 증가
    if word[i] == '<':
        i += 1
        while word[i] != '>':
            i += 1
        i += 1
    elif word[i].isalnum(): #숫자나 알파벳 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        tmp = word[start:i]
        tmp.reverse()
        word[start:i] = tmp
    else:
        i += 1
print(''.join(word))