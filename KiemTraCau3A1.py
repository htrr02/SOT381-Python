slsn = n = int(input("Nhập số lượng phần tử :"))
slsn = []
for i in range(n):
    so = input(f"Nhập số thứ {i}:")
    slsn.append(so)
print(f"Danh sách đã tạo:{slsn}")
so_chan = [n for n in range(n) if n % 2 == 0]
print(f"Số lượng phần tử có giá trị nguyên: {so_chan}")
