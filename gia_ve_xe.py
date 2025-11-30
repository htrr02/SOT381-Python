loai = input("Nhập loại hành khách: ").lower()

if loai == "học sinh":
    gia = 3000
elif loai == "sinh viên":
    gia = 5000
elif loai == "người cao tuổi":
    gia = 0
elif loai == "thường":
    gia = 7000
else:
    print("Loại hành khách không hợp lệ!")

print("Giá vé phải trả:", gia,"đ")
