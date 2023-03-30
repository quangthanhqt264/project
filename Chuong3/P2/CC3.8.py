a=str(input())
b=int(input())
if 1<=b<=20:
    for i in range(1,b+1):
        for s in range(1,i+1):
            print("*",end=" ")
        print("")