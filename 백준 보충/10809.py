S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end = ' ')
    else:
        print(-1, end =' ')


#ord
'''
S = input()
check = [-1]*26

for i in range(len(S)):
    if check[ord(S[i]) - 97] != -1:

'''