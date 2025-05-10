import math

# 입력 받기
A, B = map(int, input().split())

# 조합 계산 (math.comb() 사용)
result = math.comb(A, B)

# 결과 출력
print(result)
