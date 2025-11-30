print("Tính phí giao hàng")

giatri = int(input("Nhập vào tổng giá trị đơn hàng(đ):"))

if giatri > 500000:
    print("Miễn phí giao hàng")
elif 100000 <= giatri <= 500000:
    print("Phí giao hàng là 20000đ")
else:
    print("Phí giao hàng là 35000đ")
