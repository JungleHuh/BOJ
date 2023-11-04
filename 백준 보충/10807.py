
"""""
map 함수는 두 개의 인자를 받습니다. 첫 번째 인자는 함수,
두 번째 인자는 반복 가능한(iterable) 객체(여기서는 문자열 리스트)입니다.
int 함수는 문자열을 정수로 변환하는 역할을 합니다. 
따라서map(int, input().split())는 사용자 입력을 공백으로 분할하고, 
각 분할된 문자열을 정수로 변환하여 정수 리스트를 반환합니다.

map() 함수의 결과를 list() 생성자로 묶어서 리스트로 변환합니다. 
이로써 N_list 변수에는 정수로 변환된 입력값들이 저장된 리스트가 할당됩니다.
"""

N = int(input())
N_list = list(map(int, input().split()))
V = int(input())
print(N_list.count(V))
