n=int(input())
a=1
while True:
    if n<0:
        break
    else:
        for i in range(0,n):
            i=i+1
            a=a*i
            continue
        print(a,sep="")
        n=int(input(""))
        a=1