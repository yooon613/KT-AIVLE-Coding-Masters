a, b = map(int, input().split())

fib = [1, 1]

while len(fib) <100:
    fib.append(fib[-1]+fib[-2])
    
ff_seq =[]

for i in range(100):
    ff_seq+=[fib[i]] * fib[i]
    if len(ff_seq) >= b:
        break
    
total = sum(ff_seq[a-1:b])
print(total)
