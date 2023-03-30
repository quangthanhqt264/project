KW=int(input("Tieu thu=" ))
if 1<=KW<=100:
    ĐG=KW*550
elif 101<=KW<=150:
    ĐG=((100*550)+(KW-100)*750)
elif 151<=KW<=200:
    ĐG=((100*550)+(50*750)+(KW-150)*950)
elif 201<=KW:
    ĐG=((100*550)+(50*150)+(50*950)+(KW-200)*1350)
VAT=0.1*ĐG
print("Phai tra=",VAT+ĐG,sep="")