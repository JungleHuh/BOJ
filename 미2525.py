N, M = map(int, input().split())
R = int(input())

N += R//60
M += R % 60

if M >= 60:
    N +=1
    M -=60
if N >=24:
    N -= 24

print(N,M)