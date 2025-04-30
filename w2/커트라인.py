n, limit = map(int, input().split())
scores = list(map(int, input().split()))

best_cut = min(scores) - 1
best_count = 0

for cut in scores:
    passed = [False] * n

    for i in range(n):
        if scores[i] >= cut:
            passed[i] = True

    for i in range(n):
        if not passed[i]:
            if (i > 0 and passed[i - 1]) or (i < n - 1 and passed[i + 1]):
                passed[i] = True

    current_count = sum(passed)

    if current_count <= limit:
        if current_count > best_count or (current_count == best_count and cut > best_cut):
            best_count = current_count
            best_cut = cut

print(best_cut)
