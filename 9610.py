T = int(input())
Q1 = []
Q2 = []
Q3 = []
Q4 = []
AXIS = []
for i in range(T):
    a,b = map(int, input().split())
    if a == 0 or b == 0:
        AXIS.append((a,b))
    elif a > 0 and b > 0:
        Q1.append((a,b))
    elif a <0 and b >0 :
        Q2.append((a,b))
    elif a < 0 and b <0 :
        Q3.append((a,b))
    elif a >0 and b <0:
        Q4.append((a,b))

print('Q1:', len(Q1))
print('Q2:', len(Q2))
print('Q3:', len(Q3))
print('Q4:', len(Q4))
print('AXIS:', len(AXIS))


        
