n, s = map(int,input().split())

if n>0 and s >0:
    print(1)
if n<0 and s>0:
    print(2)
if n<0 and s<0:
    print(3)
if n>0 and s<0:
    print(4)