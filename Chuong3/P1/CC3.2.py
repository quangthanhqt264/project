MC1=int(input("M1=" ))
MC2=int(input("M2=" ))
MC3=int(input("M3=" ))
ĐNTT=int(input("S=" ))
if ĐNTT<=100:
    TD=MC1*ĐNTT
elif 101<=ĐNTT<=150:
    TD=((MC1*100)+(ĐNTT-100)*MC2)
else:
    TD=((MC1*100)+(MC2*50)+(ĐNTT-150)*MC3)
print("Phai tra="+str(TD))   