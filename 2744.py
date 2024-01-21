N = input()

for i in N:
    if i>="a" and i <= "z":
        #ord -> 하나의 문자를 유니코드 정수로 변환
        #i="A"라면, ord(i)는 정수 65
        # chr 메서드는 하나의 정수를 유니코드 문자로 변환
        #i=65라면, chr(i)는 문자 A를 반환
        print(chr(ord(i) -32), end = '')
    else:
        print(chr(ord(i) + 32), end = '')