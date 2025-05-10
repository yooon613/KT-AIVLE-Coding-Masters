p, q = map(int, input().split())
n = int(input())

# 정수 부분
integer_part = str(p // q)
p %= q  # 나머지를 소수점 계산에 사용

decimal = []

# 소수점 n+1자리까지 계산
for _ in range(n + 1):
    p *= 10
    decimal.append(p // q)
    p %= q

# 반올림 처리
if decimal[-1] >= 5:
    decimal[n - 1] += 1

# 자리수 올림 처리 
for i in range(n - 1, 0, -1):
    if decimal[i] == 10:
        decimal[i] = 0
        decimal[i - 1] += 1

if decimal[0] == 10:
    decimal[0] = 0
    integer_part = str(int(integer_part) + 1)


print(f"{integer_part}." + ''.join(map(str, decimal[:n])))
