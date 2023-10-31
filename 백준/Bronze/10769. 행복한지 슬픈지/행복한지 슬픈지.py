sentence = input().split(':-')
happy = 0
sad = 0

for i in sentence[1:]:
    if i[0] == ')':
        happy += 1
    elif i[0] == '(':
        sad += 1
if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')