H,M = map(int, input().split())

if M>=30:
    M-=30
    
else:
    M+=30
    H-=1
    
    if H<0:
        H =23
    
print(H,M)
