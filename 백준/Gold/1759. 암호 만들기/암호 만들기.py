def dfs(idx, cnt, password, consonant, vowel):
    if cnt == l:
        if consonant >= 2 and vowel >= 1:
            print(password)
        return
    
    if idx >= c:
        return
    
    if word[idx] in ('a', 'e', 'i', 'o', 'u'):
        dfs(idx+1, cnt+1, password+word[idx], consonant, vowel+1)
    else:
        dfs(idx+1, cnt+1, password+word[idx], consonant+1, vowel)
    dfs(idx+1, cnt, password, consonant, vowel)


l, c = map(int,input().split())
word = sorted(list(input().split()))
dfs(0, 0, '', 0, 0)