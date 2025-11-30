def may_tinh(so1, so2, phep_toan):
    if phep_toan == '+':
        return so1 + so2
    elif phep_toan == '-':
        return so1 - so2
    elif phep_toan == '*':
        return so1 * so2
    elif phep_toan == '/':
        if so2 == 0:
            return "Lỗi: Không thể chia cho 0"
        else:
            return so1 / so2
    else:
        return "Phép toán không hợp lệ"


so_a = float(input("Nhập số thứ nhất: "))
phep_toan_nhap = input("Nhập phép toán (+, -, *, /): ")
so_b = float(input("Nhập số thứ hai: "))


ket_qua = may_tinh(so_a, so_b, phep_toan_nhap)
print("Kết quả:", ket_qua)
