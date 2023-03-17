A=float(input("a=" ))
B=float(input("b=" ))
C=float(input("c=" ))
max=A
if max<B:
    max=B
if max<C:
    max=C
print("SLN=",max)
min=A
if min>B:
    min=B
if min>C:
    min=C
print("SBN=",min)