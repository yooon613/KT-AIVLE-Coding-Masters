year, army, mobilized, rank = input().split()
year = int(year)

if rank == "Private":
    if year ==0:
        print(0)
    elif 1<=year<=4:
        if mobilized == 'Y':
            print(28)
            
        else:
            if army == 'ROKAF':
                print(28)
            else:
                print(32)
                
    elif 5 <=year <=6:
        print(20)
        
elif rank == 'Officer':
    if year ==0:
        print(0)
    elif 1 <=year<=6:
        print(28)
