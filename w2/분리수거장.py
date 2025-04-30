n = int(input())
apartments = []


for i in range(n):
    d, a = map(int, input().split())
    apartments.append((d, a))

min_distance_sum = float('inf')  
best_apartment = -1  


for i in range(n):
    current_d, current_a = apartments[i]
    distance_sum = 0
    
    
    for j in range(n):
        d, a = apartments[j]
        distance_sum += abs(current_d - d) * a  
    
    # 현재 계산된 거리 합이 최소값이면 업데이트
    if distance_sum < min_distance_sum:
        min_distance_sum = distance_sum
        best_apartment = i + 1  # 1-based index

print(best_apartment)
