slBH = n = int(input("Nhập số lượng bài hát:"))
dsBH=[]
for i in range(n):
    ten_bai = input(f"Nhập tên bài hát thứ {i}: ")
    dsBH.append(ten_bai)
for i in range(n):
    ten=dsBH[i]
    print(f"Bài{i}:{ten}")
for bai in dsBH:
    print(f"{bai.upper()}")
print("Các bài hát có từ yêu")
for i in range(n):
    ten=dsBH[i]
    if ( ten.find("yêu") !=-1):
        print(f"Bài {i}:{ten}")

print("Các bài tên dài nhất")
tenbaidainhat = dsBH[0]
sotucuabaidainhat= len(tenbaidainhat.split())
vitricuabai = 0
for i in range(n):
    ten=dsBH[i]
    sotu = len (ten.split())
    if sotu>sotucuabaidainhat:
        vitricuabai = i
        tenbaidainhat=ten
        sotucuabaidainhat=sotu
print(f"Bài:{tenbaidainhat}")