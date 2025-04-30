n = int(input())
counter = [0] * 10

for i in range(1, n + 1):
    for digit in str(i):
        counter[int(digit)] += 1

print(*counter)
