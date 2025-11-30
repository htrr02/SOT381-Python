a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Không phải tam giác! Cạnh phải lớn hơn 0.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Không phải tam giác! Tổng 2 cạnh không lớn hơn cạnh còn lại.")
else:
    print("Đây là tam giác.")
