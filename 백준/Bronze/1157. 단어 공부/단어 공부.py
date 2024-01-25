word = input()
word = word.upper()

word_num = {}

for k in word:
    if k in word_num:
        word_num[k] += 1
    else:
        word_num[k] = 1

max_num = max(word_num.values())

max_word = []
for k in word_num:
    if word_num[k] == max_num:
        max_word.append(k)
        
if len(max_word) == 1:
    print(max_word[0])
else:
    print("?")