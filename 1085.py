x,y,w,h = list(map(int, input().split()))

if x<= w/2 and y<h/2:
    print(min(x,y))
if x< w/2 and y>=h/2:
    print(min(x, h-y))
if x>= w/2 and y>h/2:
    print(min(w-x, h-y))
if x> w/2 and y<=h/2:
    print(min(w-x, y))
if x == w/2 and y== w/2:
    print(min(x,y))