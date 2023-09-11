a,p = map(int,input().split())
sequence=[a]
while True:
       Dn=0
       a=str(sequence[-1])
       for i in a:
              Dn+=int(i)**p
       if Dn in sequence:
              print(sequence.index(Dn))
              break
       else:
              sequence.append(Dn)