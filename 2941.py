li = ['c=','c-','dz=','d-','lj','nj','s=','z=']

str = input()
count = 0

for a in li:
    str = str.replace(a,"0")
print(len(str))