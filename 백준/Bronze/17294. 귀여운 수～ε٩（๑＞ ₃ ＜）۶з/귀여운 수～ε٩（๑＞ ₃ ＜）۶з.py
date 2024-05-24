k = input()

if len(k) == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else:
    val = int(k[1]) - int(k[0])
    for i in range(2, len(k)):
        if int(k[i]) - int(k[i-1]) == val:
            continue
        else:
            print('흥칫뿡!! <(￣ ﹌ ￣)>')
            break

    else:
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')