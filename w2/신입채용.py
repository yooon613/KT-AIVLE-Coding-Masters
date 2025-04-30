def main():
    N = int(input()) 
    scores = [tuple(map(int, input().split())) for _ in range(N)]

    ranks = [1] * N  # 각 지원자의 초기 순위는 1로 설정

    
    for i in range(N):
        for j in range(N):
            if i != j:
                # 서류 점수와 면접 점수가 모두 더 높은 경우
                if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
                    ranks[i] += 1

    
    print(" ".join(map(str, ranks)))

if __name__ == "__main__":
    main()
