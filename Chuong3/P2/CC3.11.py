SA=0
SD=0
for i in range(1,200):
    n=int(input(""))
    if n==0:
        break
    elif n<0:
        SA=SA+1
    else:
        SD=SD+1
print(SD,"so duong")
print(SA,"so am")