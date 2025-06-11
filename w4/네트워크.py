def solution(n, computers):
    visited = [False] * n
    
    def dfs(computer):
        visited[computer] = True
        for neighbor in range(n):
            if not visited[neighbor] and computers[computer][neighbor] == 1:
                dfs(neighbor)
    
    network_count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_count += 1
    
    return network_count
