T=int(input())
L=int(input())
H=int(input())
ĐTB=(H+(T*2)+(L*3))/6
if ĐTB<3:
    print("Kem")
elif 3<=ĐTB<5:
    print("Yeu")
elif 5<=ĐTB<6:
    print("Trung binh")
elif 6<=ĐTB<7:
    print("Trung binh Kha")
elif 7<=ĐTB<8:
    print("Kha")
elif 8<=ĐTB<9:
    print("Gioi")
elif 9<=ĐTB<10:
    print("Xuat sac")