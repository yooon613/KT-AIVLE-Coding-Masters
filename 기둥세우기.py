import sys 

# 궁전의 크기를 입력받는다
N, M = map(int, sys.stdin.readline().split())

# 궁전 상태를 저장할 이차원 리스트 생성
grid =[] 
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

# 각 행에 대해 기둥(0)이 있는지 확인
row_need = 0
for i in range(N):
    found = False
    for j in range(M):
        if grid[i][j] ==0:
            found = True
            break
    
    if not found:
        row_need +=1
        
# 각 열에 대해서도 동일하게 확인     
col_need =0
for j in range(M):
    found = False
    for i in range(N):
        if grid[i][j] ==0:
            found  =True
            break
        
    if not found:
        col_need +=1
# 행과 열 중 더 많이 부족한 쪽만큼 기둥을 세움
answer = max(row_need, col_need)

print(answer)
