n = int(input())
for i in range(n):
    a,b,c = map(int, input().split())
    height = c % a
    if c % a == 0:
        height = 1
    if b // height == 0:
        room = (b // height)
    else:
        room = (b // height) - 1 
    if room < 10:
        print(height, end = '')
        print(0, end = '')
        print(room)
    else:
        print(height, end = '')
        print(room)

