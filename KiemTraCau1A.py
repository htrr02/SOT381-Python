dtb = float(input("Nhập điểm trung bình của học sinh:"))
if 0 <= dtb <= 10 :
    print("ĐIỂM HỢP LỆ")
    if 8.0 <= dtb <= 10 :
      print("Học lực: Giỏi")
    elif 6.5 <= dtb <= 8.0 :
      print("Học lực:Khá")
    elif 5.0 <= dtb <= 6.5 :
      print("Học lực:Trung bình")
    elif dtb < 3.5 :
      print("Học lực:Yếu")
else :
    print("ĐIỂM KHÔNG HỢP LỆ")
