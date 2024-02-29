n = int(input())
m = input()
k=[]
p=[]

for i in m:
    if i == 'A':
        k.append(i)
    elif i == 'B':
        p.append(i)
if len(k) > len(p):
    print('A')
elif len(k) < len(p):
    print('B')
else:
    print('Tie')