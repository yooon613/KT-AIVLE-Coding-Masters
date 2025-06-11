def solution(players, callings):
    name_to_index = {name: i for i, name in enumerate(players)}
    
    for call in callings:
        cur_idx = name_to_index[call]
        front_idx = cur_idx - 1
        
        # 추월한 선수 이름
        front_name = players[front_idx]
        
        # 자리 바꾸기
        players[front_idx], players[cur_idx] = players[cur_idx], players[front_idx]
        
        # 인덱스 업데이트
        name_to_index[call] = front_idx
        name_to_index[front_name] = cur_idx

    return players
