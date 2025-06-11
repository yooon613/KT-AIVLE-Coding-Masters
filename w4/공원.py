def solution(mats, park):
    n = len(park)
    m = len(park[0])
    
    
    mats.sort(reverse=True)

    for size in mats:
        if size > n or size > m:
            continue  

        for i in range(n - size + 1):
            for j in range(m - size + 1):
                valid = True
                for x in range(i, i + size):
                    for y in range(j, j + size):
                        if park[x][y] != "-1":
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    return size 
    return -1  
