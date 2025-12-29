toan = float(input("Nhập điểm toán:"))
ly = float(input("Nhập điểm Lý:"))
hoa = float(input("Nhập điểm Hóa:"))

tong = toan + ly + hoa

if tong >= 15 and toan > 4 and ly > 4 and hoa > 4 :
    print("Bạn đã đậu")
    if toan > 5 and ly > 5 and hoa > 5:
         print("Học đều các môn")
    else:
         print("Chưa học đều các môn")
else :
    print("Thi hỏng")