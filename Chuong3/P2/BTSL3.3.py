n=int(input("n="))
so=n
if n!=0:
    diem=0
    while n>0:
       n=int(n/10)
       print("lan",diem+1,"n=",n)
       diem+=1
else:
    diem=1
    print(so,"co",diem,"chu so")