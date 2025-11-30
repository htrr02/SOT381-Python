
def tinh_tien_phong(loaiphong, sodem):
    loaiphong = loaiphong.lower()

loaiphong = input("Nhập loại phòng:")
sodem = int(input("Nhập số ngày:"))


if loaiphong == "standard":
        gia_co_ban = 1000000
elif loaiphong == "deluxe":
        gia_co_ban = 1500000
elif loaiphong == "suite":
        gia_co_ban = 2500000
else:
       print(" Loại phòng không hợp lệ")

tong_tien = gia_co_ban * sodem

if sodem > 3:
        tong_tien = tong_tien * 0.9
else:
        tong_tien = tong_tien

print(tong_tien)

