w = float(input(" Nhập độ dài cạnh w của hình chữ nhật:"))
h = float(input("Nhập độ dài cạnh h của hình chữ nhật: "))

if 0.0 <= w <= 100.0 and 0.0 <= h <= 100.0 :
    chu_vi = (w+h)*2
    dien_tich = w*h
    print(f"Chu vi của hình chữ nhật là: {chu_vi:.2f}")
    print(f"Diện tích của hình chữ nhật là:{dien_tich:.2f}")

else:
     print("Vui lòng nhập giá trị hợp lệ")


