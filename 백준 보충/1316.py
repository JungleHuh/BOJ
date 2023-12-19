import sys
input = sys.stdin.readline

n = int(input())
cnt = n

for i in range(n):
    word = input()
    for j in range(0, len(word)- 1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            #연속되지 않는 수 나오면, 바로 끊어주기
            break
print(cnt)

            
