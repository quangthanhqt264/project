n=int(input(""))
a=1
b=1
while True:
    if n<0:
        break
    b=b+1
    a=a*b
    if b<n:
        continue
    print(a,sep="")
    n=int(input(""))
    b=0
    a=1