from collections import Counter

def solution(X, Y):
    counter_x = Counter(X)
    counter_y = Counter(Y)

    result = []
    for digit in map(str, range(9, -1, -1)):
        min_count = min(counter_x[digit], counter_y[digit])
        result.append(digit * min_count)

    answer = ''.join(result)

    if not answer:
        return "-1"
    elif answer[0] == '0':
        return "0"
    else:
        return answer
