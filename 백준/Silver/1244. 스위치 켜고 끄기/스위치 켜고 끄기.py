n=int(input())  #스위치 개수
switch=list(map(int,input().split()))
stu=int(input())    #학생 수
for i in range(stu):
    gen,num=map(int,input().split())
    if gen==1:  #남자
        for j in range(num-1,n,num):
            if switch[j]==1:
                switch[j]=0
            else:
                switch[j]=1
    else:   #여자
        j=num-1
        k=1
        if switch[j]==1:
            switch[j]=0
        else:
            switch[j]=1
        while True:
            if j-k<0 or j+k>=n:
                break
            if switch[j-k]==switch[j+k]:
                if switch[j-k]==1:
                    switch[j-k]=0
                elif switch[j-k]==0:
                    switch[j-k]=1

                if switch[j+k]==1:
                    switch[j+k]=0
                elif switch[j+k]==0:
                    switch[j+k]=1
            else:
                break
            k+=1
for i in range(n):
    print(switch[i],end=' ')
    if i%20==19:
        print()
