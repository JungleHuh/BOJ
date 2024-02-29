import sys
input = sys.stdin.readline

def dec(key,n,words):
    for i in range(26):
        temp =""
        for k in key:
            temp += chr(((ord(k)-97+i)%26)+97)

    for k in range(n):
        if words[k] in temp:
            return temp
        
def main():
    key = input()
    n = int(input())
    words = []
    for _ in range(n):
        word = input()
        words.append(word)
    
    print(dec(key,n,words))

main()
