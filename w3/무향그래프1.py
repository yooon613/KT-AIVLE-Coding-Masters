N, M = map(int, input().split())

# NxN 인접 행렬 초기화 (0으로)
adj = [[0] * N for _ in range(N)]


for _ in range(M):
    u, v = map(int, input().split())
    adj[u-1][v-1] = 1
    adj[v-1][u-1] = 1  # 무향 그래프

# 행렬 출력 (각 줄 끝에 공백 포함)
for row in adj:
    print(' '.join(map(str, row)), end=' \n')
