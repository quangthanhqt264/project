a=float(input("a="))
b=float(input("b="))
tt=input("Toan tu:")
if tt=="+":
    kq=a+b
elif tt=="-":
    kq=a-b
elif tt=="*":
    kq=a*b
else:
    kq=a/b
if(tt=="/") and b==0:
    print("khong thuc hien duoc!!!")
else:
    print(a,tt,b,"=",kq,sep="")
lap=input("tiep tuc:")