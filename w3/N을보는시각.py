N = input()  # 숫자 N 입력

count = 0  # 등장 횟수를 셀 변수

for hour in range(24): 
    for minute in range(60):  
        for second in range(60): 
             
            if N in f"{hour:02}:{minute:02}:{second:02}":
                count += 1  

print(count)
