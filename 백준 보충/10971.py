import sys

N = int(input()) #도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize #출력할 최소값 정의


def dfs_backtracking(start, next, value, visited): #시작도시번호,다음도시번호,비용,방문 도시
    global min_value

    if len(visited) == N: #만약 방문한 도시가 입력받은 도시의 개수라면
        if travel_cost[next][start] != 0: #마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
            min_value = min(min_value, value + travel_cost[next][start]) #더한 값을 저장되어있는 최소값과 비교해서 대입
        return
    
    for i in range(N): #도시의 개수 만큼 반복문을 돈다.
        #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
        if travel_cost[next][i] != 0 and i not in visited and value < min_value: 
            visited.append(i) #그 도시를 방문목록에 추가
            dfs_backtracking(start, i, value + travel_cost[next][i], visited) #그 도시를 방문한다.
            visited.pop() #방문을 완료했다면 방문목록 해제
    

    ''' 
    [함수 진행 과정]
    Test case:
    0 10 15 20
    5 0  9 10
    6 13 0  12
    8 8  9  0
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            __main__함수 시작: 모든 도시 순회

            for i in range(N):
                dfs_backtracking(i, i, 0, [i])
            i = 0 -> 0번째 도시에서 출발
            dfs_backtracking(i,i,0,[i])에 i = 0 대입 -> dfs_backtracking(0,0,0,[0])에서 시작
            ------------------------------------------------------------------------------------------------------------------------------------------------------
            for 문에서 i = 0 일 때 -> travel_cost[0][0] == 0이니 조건 만족 X -> 다음 i = 1 로 넘어감.

            i = 1 일 때 -> travel_cost[0][1]이 되고 1/ travel_cost[next][i] != 0 만족, 2/  i not in visited 만족 3/ value < min_value(현재는 maxsize이니 만족)
            -> visited: [0]인데, 여기를 [0,1]로 바꿔줌
            -> dfs_backtracking(start, i, value + travel_cost[next][i], visited)에 들어가는 인수 (0,1, 0+10, [0,1]) -> (0,1,10,[0,1])이 나오게됨.
            -> visited.pop()을 통해서 [0,1]에서 '1'을 빼서 visited를 [0]으로 만들어줌. -> [0]에서 [0,1]을 방문하는 것 말고 다른 가능성 탐색하기 위함. ex) [0,2] 경로, [0,3]경로 탐색하기 위함.

            i = 2 일 때 -> travel_cost[0][2]가 되고 1/ travel_cost[next][i] != 0 만족, 2/  i not in visited 만족 3/ value < min_value(현재는 maxsize이니 만족)
            -> visited : [0]에서 [0,2]로 바꿔줌.
            -> dfs_backtracking(start, i, value + travel_cost[next][i], visited)에 들어가는 인수 (0,2, 0+15, [0,2]) -> (0,2,15,[0,1])이 나오게됨.
            -> visited.pop()을 통해서 [0,2]에서 '2'을 빼서 visited를 [0]으로 만들어줌. -> i = 3으로 넘어가자

            i = 3 일 때 -> travel_cost[0][3]가 되고 1/ travel_cost[next][i] != 0 만족, 2/  i not in visited 만족 3/ value < min_value(현재는 maxsize이니 만족)
            -> visited : [0]에서 [0,3]로 바꿔줌.
            -> dfs_backtracking(start, i, value + travel_cost[next][i], visited)에 들어가는 인수 (0,3, 0+20, [0,3]) -> (0,3,20,[0,3])이 나오게됨.
            -> visited.pop()을 통해서 [0,3]에서 '3'을 빼서 visited를 [0]으로 만들어줌. -> 반복문이 끝남.

            -------------------------------------------------------------------------------------------------------------------------------------------------------

            아마 여기서 첫 번째 재귀가 시작되는 지점일 것이다. 
            


            그러면 이제 다시 반복문(__main__함수)으로 넘아간다.
            for i in range(N):
                dfs_backtracking(i, i, 0, [i])
            
            i = 1 -> 1번 도시에서 시작.
            dfs_backtracking(i,i,0,[i])에 i = 0 대입 -> dfs_backtracking(1, 1, 0, [1])에서 시작
            -------------------------------------------------------------------------------------------------------------------------------------------------------
            i = 0 일 때 -> travel_cost[1][0] == 5 -> 1/ travel_cost[1][0] != 0 만족, 2/  i not in visited 만족 3/ value < min_value(현재는 maxsize이니 만족)
            -> visited: [1]인데, [1,0]으로 바꿔줌.
            -> dfs_backtracking(start, i, value + travel_cost[next][i], visited)에 들어가는 인수 (1, 0 , 0 + 5, [1,0]) -> (1, 0, 5,[1,0])이 나오게됨.
            -> visited.pop()을 통해서 [1, 0]에서 '0'을 빼서 visited를 [1]으로 만들어줌. -> i = '1'으로 넘어가자

            i = 1 일 때 -> travel_cost[1][1] == 0이니 -> i = 2로 넘어가자.

            i = 2 일 때 ->  travel_cost[1][2] == 9 ->  1/ travel_cost[1][0] != 0 만족, 2/  i not in visited 만족 3/ value < min_value(현재는 maxsize이니 만족)
            -> visited: [1]인데, [1,2]으로 바꿔줌.
            -> dfs_backtracking(start, i, value + travel_cost[next][i], visited)에 들어가는 인수 (1, 2 , 0 + 9, [1,2]) -> (1, 2, 9,[1,2])이 나오게됨.
            -> visited.pop()을 통해서 [1, 2]에서 '2'을 빼서 visited를 [1]으로 만들어줌. -> i = 3으로 넘어가자

            i = 3 일 때 -> travel_cost[1][3] == 10 -> 1/ travel_cost[1][0] != 0 만족, 2/  i not in visited 만족 3/ value < min_value(현재는 maxsize이니 만족)
            -> visited: [1]인데, [1,3]으로 바꿔줌.
            -> dfs_backtracking(start, i, value + travel_cost[next][i], visited)에 들어가는 인수 (1, 3 , 0 + 10, [1,3]) -> (1, 3, 10,[1,3])이 나오게됨.
            -> visited.pop()을 통해서 [1, 3]에서 '3'을 빼서 visited를 [1]으로 만들어줌. -> 반복문이 끝남.

            -------------------------------------------------------------------------------------------------------------------------------------------------------
            
            



'''

#도시마다(0~3) 출발점을 지정
for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)