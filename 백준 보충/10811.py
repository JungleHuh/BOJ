import sys
input = sys.stdin.readline

a,b = map(int, input().split())
line = [i for i in range(1,a+1)]

for j in range(b):
    c,d = map(int, input().split())
    #확실히 문자열/인덱싱 하는 것에 엄청난 약점을 지니고 있음. 
    temp = line[c-1:d]
    temp.reverse()
    line[c-1:d] = temp

for j in range(a):
  print(line[j],end=" ")



